"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
<<<<<<< HEAD
from firstapp.views import helloworld,signup
=======
from firstapp.views import main, detail, credit
>>>>>>> 9dd2c4d46e263801f8867362a4fe190c2aab708e
import firstapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', helloworld),
    path('signup/', signup),
=======
    path('', main, name='main'),
    path('detail/', detail, name='detail'),
    path('credit/', credit, name='credit'),
>>>>>>> 9dd2c4d46e263801f8867362a4fe190c2aab708e
]
