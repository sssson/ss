from django.http import request
from django.http.response import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
=======
from django.shortcuts import render
>>>>>>> ee2e617dd1893e265564a56d430c9108dab303b2
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
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/map.html', context)

def login(request):
    return render(request, 'blog/login.html')

<<<<<<< HEAD

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    new_blog = Blog()
    new_blog.body = request.POST['body']
    new_blog.created_at = timezone.now()
    
    new_blog.images = request.FILES['images']
    new_blog.save()
    return redirect('detail', new_blog.id)


=======
def search(request):
    blog_list = Blog.objects.all()
    
    search_key = request.GET.get('search_key') # 검색어 가져오기
    if search_key: # 만약 검색어가 존재하면
        blog_list = blog_list.filter(hashtag__icontains=search_key) # 해당 검색어를 포함한 queryset 가져오기
    return render(request, 'blog/search.html', {'blog_list':blog_list})
    
def post(request):
    return render(request, 'blog/post.html')
>>>>>>> ee2e617dd1893e265564a56d430c9108dab303b2
