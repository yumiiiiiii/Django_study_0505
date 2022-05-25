"""secondProject URL Configuration

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
from main.views import List, Detail, create, delete, update, SearchResultsView, comment_create, comment_delete

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List, name="main"),
    path('<int:pk>', Detail, name="detail"),
    path('create/', create, name="create"),
    path('delete/<int:pk>', delete, name="delete"),
    path('update/<int:pk>', update, name="update"),
    path('search/', SearchResultsView.as_view(), name="search"),
    path('<int:pk>/comment', comment_create, name="comment_create"),
    path('<int:recipe_pk>/create/<int:comment_pk>', comment_delete, name="comment_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
