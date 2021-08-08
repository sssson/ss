from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blog

# Create your views here.

def main(request):
    return render(request, 'blog/main.html')

def signup(request):
    return render(request, 'blog/signup.html')

def siteMain(reqeust):
    return render(request, 'siteMain.html')

def detail(request):
    return render(request, 'blog/detail.html')

def credit(request):
    return render(request, 'blog/credit.html')

def main_map(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/map.html', context)

def login(request):
    return render(request, 'blog/login.html')

def post(request):
    return render(request, 'blog/post.html')