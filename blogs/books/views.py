from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, FormView, CreateView
from books.models import Book
from django.urls import reverse_lazy
from books.forms import ContactForm, BookForm
# Create your views here.

def my_view(request):
    return HttpResponse("Welcome to Django!")

class MyView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django from class.")

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
    
class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_success")
    
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)
    
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books_form.html'
    success_url = reverse_lazy("book_list")
    
    def price_valid(self, form) -> HttpResponse:
        return super().form_valid(form)   