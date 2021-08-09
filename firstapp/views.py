from django.contrib.auth.models import User
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

def siteMain(request):
    return render(request, 'siteMain.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'blog/detail.html', {'blog' :blog})

def credit(request):
    return render(request, 'blog/credit.html')

def main_map(request):
    blogss = Blog.objects.all()
    context = {
        'blogss': blogss,
    }
    return render(request, 'blog/map.html', context)

def login(request):
    return render(request, 'blog/login.html')


def new(request):
    return render(request, 'blog/new.html')

def post(request):
    return render(request, 'blog/post.html')

def create(request):
    post_blog = Blog()
    post_blog.body = request.POST['body']
    post_blog.hashtag = request.POST['hashtag']
    post_blog.author = aa
    post_blog.created_at = timezone.now()
    post_blog.images = request.FILES['images']
    post_blog.save()
    return redirect('main')


def search(request):
    blog_list = Blog.objects.all()
    
    search_key = request.GET.get('search_key') # 검색어 가져오기
    if search_key: # 만약 검색어가 존재하면
        blog_list = blog_list.filter(hashtag__icontains=search_key) # 해당 검색어를 포함한 queryset 가져오기
    return render(request, 'blog/search.html', {'blog_list':blog_list})
    
