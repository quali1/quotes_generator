from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeView, name="home"),
    path("quotes/", views.quoteListView, name="list-quote"),
    path("quotes/create", views.quoteCreateView, name="create-quote"),
    path("like/<int:pk>", views.quoteLikeView, name="like-quote"),
]
