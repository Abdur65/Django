from django.urls import path
from django.shortcuts import render
from books.views import my_view, MyView, BookListView, ContactFormView


urlpatterns = [
    path("initial/", my_view),
    path("initial_class/", MyView.as_view()),
    path("list/", BookListView.as_view()),
    path("contact/add", ContactFormView.as_view()),
    path("contact_success/", lambda request: render(request, "success/contact_success.html"), name="contact_success"),
]
