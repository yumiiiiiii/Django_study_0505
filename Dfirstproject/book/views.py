from pickle import FALSE
from re import M
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import *

# Create your views here.
from book.models import *

def List(request):
    R_posts=Romance.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    M_posts=Mystery.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    D_posts=Disaster.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    contexts={'R_posts':R_posts, 'M_posts':M_posts, 'D_posts':D_posts}
    return render(request, 'list.html', contexts)

'''Romance의 CRUD'''

def R_edit(request, pk):
    R_edit = get_object_or_404(Romance,pk=pk)
    return render(request, 'R_update.html',{'R_edit':R_edit})

def R_update(request, pk):
    R_update = get_object_or_404(Romance,pk=pk)
    R_update.title=request.POST['title']
    R_update.content=request.POST['content']
    R_update.save()
    return redirect('list')

def R_detail(request, pk):
    R_post=get_object_or_404(Romance,pk=pk)
    R_hashtag=R_post.hashtag.all()
    return render(request,'R_detail.html',{'R_post':R_post,'hashtags':R_hashtag})

def R_new(request):
    form=R_Form()
    return render(request, 'R_new.html',{'form':form})

def R_create(request):
    form=R_Form(request.POST, request.FILES)
    if form.is_valid():
        R_post=form.save(commit=False)
        R_post.upload_time=timezone.now()
        R_post.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            R_post.hashtag.add(new_hashtag[0])
        return redirect('R_detail',R_post.id)
    return redirect('list')

def R_delete(request, pk):
    R_delete=get_object_or_404(Romance,pk=pk)
    R_delete.delete()
    return redirect('list')

def R_add_comment(request, pk):
    romance=get_object_or_404(Romance, pk=pk)

    if request.method=='POST':
        form=R_CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=romance
            comment.save()
            return redirect('R_detail', pk)
    else:
        form=R_CommentForm()
    
    return render(request, 'add_comment.html', {'form':form})

def R_delete_comment(request,R_post_id, comment_id):
    comment=get_object_or_404(R_Comment, pk=comment_id)
    comment.delete()

    return redirect('R_detail',R_post_id)


'''Mystery의 CRUD'''

def M_edit(request, pk):
    M_edit = get_object_or_404(Mystery,pk=pk)
    return render(request, 'M_update.html',{'M_edit':M_edit})

def M_update(request, pk):
    M_update = get_object_or_404(Mystery,pk=pk)
    M_update.title=request.POST['title']
    M_update.content=request.POST['content']
    M_update.save()
    return redirect('list')

def M_detail(request, pk):
    M_post=get_object_or_404(Mystery,pk=pk)
    M_hashtag=M_post.hashtag.all()
    return render(request,'M_detail.html',{'M_post':M_post, 'M_hashtags':M_hashtag})

def M_new(request):
    form=M_Form()
    return render(request, 'M_new.html',{'form':form})

def M_create(request):
    form=M_Form(request.POST, request.FILES)
    if form.is_valid():
        M_post=form.save(commit=False)
        M_post.upload_time=timezone.now()
        M_post.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=M_HashTag.objects.get_or_create(hashtag=tag)
            M_post.hashtag.add(new_hashtag[0])
        return redirect('M_detail',M_post.id)
    return redirect('list')

def M_delete(request, pk):
    M_delete=get_object_or_404(Mystery,pk=pk)
    M_delete.delete()
    return redirect('list')

def M_add_comment(request, pk):
    mystery=get_object_or_404(Mystery, pk=pk)

    if request.method=='POST':
        form=M_CommentForm(request.POST)

        if form.is_valid():
            M_comment=form.save(commit=False)
            M_comment.post=mystery
            M_comment.save()
            return redirect('M_detail', pk)
    else:
        form=M_CommentForm()
    
    return render(request, 'add_comment.html', {'form':form})

def M_delete_comment(request,M_post_id, comment_id):
    M_comment=get_object_or_404(M_Comment, pk=comment_id)
    M_comment.delete()

    return redirect('M_detail',M_post_id)


'''Disaster의 CRUD'''

def D_edit(request, pk):
    D_edit = get_object_or_404(Disaster,pk=pk)
    return render(request, 'D_update.html',{'D_edit':D_edit})

def D_update(request, pk):
    D_update = get_object_or_404(Disaster,pk=pk)
    D_update.title=request.POST['title']
    D_update.content=request.POST['content']
    D_update.save()
    return redirect('list')

def D_detail(request, pk):
    D_post=get_object_or_404(Disaster,pk=pk)
    D_hashtag=D_post.hashtag.all()
    return render(request,'D_detail.html',{'D_post':D_post, 'D_hashtags':D_hashtag})

def D_new(request):
    form=D_Form()
    return render(request, 'D_new.html',{'form':form})

def D_create(request):
    form=D_Form(request.POST, request.FILES)
    if form.is_valid():
        D_post=form.save(commit=False)
        D_post.upload_time=timezone.now()
        D_post.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=D_HashTag.objects.get_or_create(hashtag=tag)
            D_post.hashtag.add(new_hashtag[0])
        return redirect('D_detail',D_post.id)
    return redirect('list')

def D_delete(request, pk):
    D_delete=get_object_or_404(Disaster,pk=pk)
    D_delete.delete()
    return redirect('list')

def D_add_comment(request, pk):
    disaster=get_object_or_404(Disaster, pk=pk)

    if request.method=='POST':
        form=D_CommentForm(request.POST)

        if form.is_valid():
            M_comment=form.save(commit=False)
            M_comment.post=disaster
            M_comment.save()
            return redirect('D_detail', pk)
    else:
        form=D_CommentForm()
    
    return render(request, 'add_comment.html', {'form':form})

def D_delete_comment(request,D_post_id, comment_id):
    D_comment=get_object_or_404(D_Comment, pk=comment_id)
    D_comment.delete()

    return redirect('D_detail',D_post_id)

