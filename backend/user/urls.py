from django.urls import path
from . import views

urlpatterns = [
    path("profile/<int:pk>", views.userProfileView, name="user-profile"),
    path("logout/", views.userLogout, name="logout"),
    path("login/", views.userLogin, name="login"),
    path("register/", views.userRegister, name="register"),
]
