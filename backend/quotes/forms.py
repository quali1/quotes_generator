from django import forms
from .models import Quote, Tag


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["title", "author", "hide_creator", "tags"]

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class TagForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["tags"]
