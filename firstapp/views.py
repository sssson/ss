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

def search(request):
    blog_list = Blog.objects.all()
    
    search_key = request.GET.get('search_key') # 검색어 가져오기
    if search_key: # 만약 검색어가 존재하면
        blog_list = blog_list.filter(hashtag__icontains=search_key) # 해당 검색어를 포함한 queryset 가져오기
    return render(request, 'blog/search.html', {'blog_list':blog_list})
    
def post(request):
    return render(request, 'blog/post.html')
