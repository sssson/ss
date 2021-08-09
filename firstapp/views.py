from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.

def main(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/main.html', {'blogs':blogs})

def signup(request):
    return render(request, 'blog/signup.html')

def siteMain(reqeust):
    return render(request, 'siteMain.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'blog/detail.html', {'blog' :blog})

def credit(request):
    return render(request, 'blog/credit.html')

def main_map(request):
    return render(request, 'blog/map.html')

def login(request):
    return render(request, 'blog/login.html')


def new(request):
    return render(request, 'blog/new.html')

def create(request):
    new_blog = Blog()
    new_blog.body = request.POST['body']
    new_blog.created_at = timezone.now()
    
    new_blog.images = request.FILES['images']
    new_blog.save()
    return redirect('detail', new_blog.id)


