"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from book.views import List, M_detail, D_detail, detail
from drama.views import List2, M_detail2, D_detail2, detail2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book',List,name='main'),
    path('book/r/<int:pk>',detail,name='detail'),
    path('book/m/<int:pk>',M_detail,name='M_detail'),
    path('book/d/<int:pk>',D_detail,name='D_detail'),
    path('drama',List2,name='main2'),
    path('drama/r/<int:pk>',detail2,name='detail2'),
    path('drama/m/<int:pk>',M_detail2,name='M_detail2'),
    path('drama/d/<int:pk>',D_detail2,name='D_detail2'),
]
