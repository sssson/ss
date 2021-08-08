from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'blog/main.html')

<<<<<<< HEAD
def siteMain(request):
    return render(request, 'siteMain.html')

def signup(request):
    return render(request, 'blog/signup.html')
=======
def siteMain(reqeust):
    return render(request, 'siteMain.html')

def detail(request):
    return render(request, 'blog/detail.html')

def credit(request):
    return render(request, 'blog/credit.html')
>>>>>>> 9dd2c4d46e263801f8867362a4fe190c2aab708e
