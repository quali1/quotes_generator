import requests

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Quote, Tag
from .forms import QuoteForm, TagForm


def homeView(request):
    # api_url = "https://api.api-ninjas.com/v1/quotes?category="
    # random_quote = requests.get(
    #     api_url, headers={"X-Api-Key": "#"}
    # ).json()[0]
    # random_title = random_quote["quote"]
    # random_author = random_quote["author"]
    # random_tag = random_quote["category"]

    tags = list(Tag.objects.values_list("tag", flat=True))
    creator = User.objects.get(username="api")

    # instance = Quote(
    #     title=random_title,
    #     author=random_author,
    #     creator=creator,
    #     hide_creator=True,
    # )
    # instance.save()
    # if random_tag not in tags:
    #     tag = Tag.objects.create(tag=random_tag)
    #     instance.tags.add(tag)

    quotes = Quote.objects.all()
    # context = {"quotes": quotes, "random_quote": random_quote}
    context = {"quotes": quotes}
    return render(request, "quotes/home.html", context)


@login_required(login_url="login")
def quoteCreateView(request):
    form = QuoteForm
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.creator = request.user
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "quotes/create-quote.html", context)


def quoteLikeView(request, pk):
    quote = get_object_or_404(Quote, id=pk)
    page = request.META.get("HTTP_REFERER")

    if request.user in quote.likes.all():
        quote.likes.remove(request.user)
    else:
        quote.likes.add(request.user)

    quote.save()

    return redirect(page)


def quoteListView(request):
    search = None
    filter_value = None
    sort_value = None
    sort_mapping = None

    quotes = Quote.objects.all().order_by("-created")
    tags = Tag.objects.all()
    form = TagForm

    if request.method == "GET":
        search = request.GET.get("search", default="")
        filter_value = request.GET.get("filter_value", default="")
        sort_value = request.GET.get("sort_value")

        sort_mapping = {
            "newest": ["-created", "Newest First"],
            "oldest": ["created", "Oldest First"],
            "most": ["-likes_count", "Most Liked First"],
            "least": ["likes_count", "Least Liked First"],
        }

        if search:
            quotes = Quote.objects.filter(
                Q(title__icontains=search)
                | Q(author__icontains=search)
                | Q(creator__username__icontains=search)
            )

        if filter_value != "-----" and filter_value:
            quotes = quotes.filter(Q(tags__tag__contains=filter_value))

        if sort_value in sort_mapping:
            quotes = quotes.order_by(sort_mapping[sort_value][0])

    context = {
        "quotes": quotes,
        "tags": tags,
        "form": form,
        "search": search,
        "filter_value": filter_value,
        "sort_value": sort_value,
        "sort_mapping": sort_mapping,
    }
    return render(request, "quotes/list-quote.html", context)


def quoteDeleteView(request):
    pass
