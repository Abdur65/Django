from django.urls import path
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, mymodel_view
from books.views import BookListView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("list/", BookListView.as_view(), name="list"),
    path('register/', RegisterView.as_view(), name='register'),
    path('restricted/', mymodel_view, name='mymodel_view'),
]
