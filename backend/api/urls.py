from django.urls import path
from . import views

urlpatterns = [
    path("quotes/", views.QuoteListCreateAPIView.as_view()),
    path("quotes/<int:pk>", views.QuoteDetailAPIView.as_view()),
    path("quotes/update/<int:pk>", views.QuoteUpdateAPIView.as_view()),
    path("quotes/delete/<int:pk>/", views.QuoteDestroyAPIView.as_view()),
]
