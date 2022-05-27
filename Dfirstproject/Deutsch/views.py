from distutils.command.upload import upload
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import HashTag, Posting, Comment

# Create your views here.
from Deutsch.models import Posting
from django.utils import timezone
from .forms import PostingForm, CommentForm

def List(request):
    posts = Posting.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    post_hashtag = post.hashtag.all()
    return render(request, 'detail.html', {'post':post, 'hashtags':post_hashtag})

def new(request):
    form = PostingForm()
    return render(request, 'new.html',{'form':form})

def create(request):
    form = PostingForm(request.POST,request.FILES)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.upload_time = timezone.now()
        new_post.save()
        hashtags = request.POST['hashtags']
        hashtag = hashtags.split(", ")
        for tag in hashtag:
            new_hashtag = HashTag.objects.get_or_create(hashtag=tag)
            new_post.hashtag.add(new_hashtag[0])
        return redirect('detail',new_post.id)
    return redirect('list')

def delete(request, post_id):
    post_delete = get_object_or_404(Posting,pk=post_id)
    post_delete.delete()
    return redirect('list')

def edit(request, post_id):
    post = get_object_or_404(Posting,pk=post_id)
    return render(request, 'edit.html', {'post':post})

def update(request, post_id):
    post_updated = get_object_or_404(Posting,pk=post_id)
    post_updated.title = request.POST['title']
    post_updated.content = request.POST['content']
    post_updated.save()
    return redirect('detail',post_updated.id)

def add_comment(request, post_id):
    post = get_object_or_404(Posting, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail',post_id)

    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form':form})

def delete_comment(request,post_id,comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    comment.delete()
    return redirect('detail',post_id)