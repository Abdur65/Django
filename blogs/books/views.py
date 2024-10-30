# From Django 
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, FormView, CreateView
from django.urls import reverse_lazy

# From books
from books.models import Book
from books.forms import ContactForm, BookForm
from books.serializers import BookSerializer, AuthorSerializer, PublisherSerializer

# From rest_framework
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView


# General Views
def my_view(request):
    return HttpResponse("Welcome to Django!")

class MyView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django from class.")


# Book views
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
    template_name = 'book_form.html'
    success_url = reverse_lazy("book-list")
    
    # def price_valid(self, form) -> HttpResponse:
    #     return super().form_valid(form)   

# Rest_framework APIs   
class BookListCreate(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class AuthorListCreate(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = AuthorSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class PublisherListCreate(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = PublisherSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
class BookGetUpdateDelete(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ('get', 'post', 'put', 'delete')
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, *kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, *kwargs)
