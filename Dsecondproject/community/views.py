from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Posting

# Create your views here.
from community.models import Posting


def List(request):
    posts = Posting.objects.all().order_by('country', 'upload_time')
    return render(request, 'list.html', {'posts': posts})


def detail(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    return render(request, 'detail.html', {'post': post})


# velog https://velog.io/@hidaehyunlee/Django-%EC%83%88-%EA%B8%80-%EC%9E%91%EC%84%B1-%EA%B8%B0%EB%8A%A5-%EB%A7%8C%EB%93%A4%EA%B8%B0-CR


def new(request):
    return render(request, 'new.html')

# hello/views.py


def home(request):
    blogs = Posting.objects
    return render(request, 'home.html', {'blogs': blogs})


def create(request):
    if(request.method == 'POST'):
        post = Posting()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('home')
