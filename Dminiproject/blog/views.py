from django.shortcuts import *
from .models import Blog, Comment
from django.utils import timezone
from .forms import BlogForm, CommentForm
# Create your views here.


def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})


def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form': form})


def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.date = timezone.now()
        new_blog.save()
    return redirect('home')


def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('home')


def edit(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog': post})


def update(request, blog_id):
    blog_updated = get_object_or_404(Blog, pk=blog_id)
    blog_updated.title = request.POST['title']
    blog_updated.content = request.POST['content']
    blog_updated.save()
    return redirect("home")


def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('detail', blog_id)

    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})


def delete_comment(request, blog_id, comment_id):

    comment_delete = get_object_or_404(Comment, pk=comment_id)
    comment_delete.delete()
    return redirect('detail', blog_id)
