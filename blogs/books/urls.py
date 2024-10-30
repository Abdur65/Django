from django.urls import path
from django.shortcuts import render
from books.views import (
    my_view, MyView, BookListView, ContactFormView, BookListCreate, BookCreateView, BookGetUpdateDelete)



urlpatterns = [
    path("initial/", my_view),
    path("initial_class/", MyView.as_view()),
    path("list/", BookListView.as_view(), name="book-list"),
    path("contact/add", ContactFormView.as_view()),
    path("add_book/", BookCreateView.as_view(), name="create-book"),
    path("contact_success/", lambda request: render(request, "success/contact_success.html"), name="contact_success"),
    path('rest_books/', BookListCreate.as_view(), name='rest-book-list'),
    path("rest/book/<int:pk>", BookGetUpdateDelete.as_view(), name="rest-book"),
]
