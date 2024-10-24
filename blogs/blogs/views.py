# from django.http import HttpResponse

# def hello_html(request):
#     return HttpResponse("Hello, Django!")

from django.shortcuts import render

def hello_django(request):
    return render(request, "hello.html")