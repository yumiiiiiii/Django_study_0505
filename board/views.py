from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from board.models import HashTag
from board.forms import BoardForm, CommentForm

# Create your views here.
from board.models import Posting

def home(request):
    posts = Posting.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'home.html', {'posts':posts})

def detail(request, pk):
    post_detail = get_object_or_404(Posting, pk = pk)
    post_hashtag = post_detail.hashtag.all()
    return render(request, 'detail.html', {'post':post_detail, 'hashtags': post_hashtag})

def new(request):
    form = BoardForm()
    return render(request, 'new.html',{'form':form})

def create(request):
    form = BoardForm(request.POST, request.FILES)
    if form.is_valid():
        new_post = form.save(commit = False)
        new_post.date = timezone.now()
        new_post.save()
        hashtags = request.POST['hashtags']
        hashtag = hashtags.split(",")
        for tag in hashtag:
            new_hashtag = HashTag.objects.get_or_create(hashtag = tag)
            new_post.hashtag.add(new_hashtag[0])
        return redirect('detail', new_post.id)
    return redirect('home')

def delete(request, post_id):
    post_delete = get_object_or_404(Posting, pk = post_id)
    post_delete.delete()
    return redirect('home')

def add_comment(request, post_id):
    post = get_object_or_404(Posting, pk = post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', post_id)
    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form':form})