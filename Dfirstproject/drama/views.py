from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from drama.models import *
from .forms import *



def List2(request):
    R_posts2=Romance.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    M_posts2=Mystery.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    D_posts2=Disaster.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    contexts={'R_posts2':R_posts2, 'M_posts2':M_posts2, 'D_posts2':D_posts2}
    return render(request, 'list2.html', contexts)


'''Romance의 CRUD'''

def R_edit2(request, pk):
    R_edit2 = get_object_or_404(Romance,pk=pk)
    return render(request, 'R_update2.html',{'R_edit2':R_edit2})

def R_update2(request, pk):
    R_update2= get_object_or_404(Romance,pk=pk)
    R_update2.title=request.POST['title']
    R_update2.author=request.POST['author']
    R_update2.content=request.POST['content']
    R_update2.save()
    return redirect('list2')

def R_detail2(request, pk):
    R_post2=get_object_or_404(Romance,pk=pk)
    R_hashtag2=R_post2.hashtag.all()
    return render(request,'R_detail2.html',{'R_post2':R_post2, 'R_hashtags2':R_hashtag2})

def R_new2(request):
    form=R_Form()
    return render(request, 'R_new2.html',{'form':form})

def R_create2(request):
    form=R_Form(request.POST, request.FILES)
    if form.is_valid():
        R_post2=form.save(commit=False)
        R_post2.upload_time=timezone.now()
        R_post2.save()
        hashtags2=request.POST['hashtags']
        hashtag2=hashtags2.split(", ")
        for tag in hashtag2:
            new_hashtag=R_HashTag.objects.get_or_create(hashtag=tag)
            R_post2.hashtag.add(new_hashtag[0])
        return redirect('R_detail2',R_post2.id)
    return redirect('list')

def R_delete2(request, pk):
    R_delete2=get_object_or_404(Romance,pk=pk)
    R_delete2.delete()
    return redirect('list2')

def R_add_comment2(request, pk):
    romance=get_object_or_404(Romance, pk=pk)

    if request.method=='POST':
        form=R_CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=romance
            comment.save()
            return redirect('R_detail2', pk)
    else:
        form=R_CommentForm()
    
    return render(request, 'add_comment2.html', {'form':form})

def R_delete_comment2(request,R_post2_id, comment_id):
    comment=get_object_or_404(R_Comment, pk=comment_id)
    comment.delete()

    return redirect('R_detail2',R_post2_id)


'''Mystery의 CRUD'''

def M_edit2(request, pk):
    M_edit2 = get_object_or_404(Mystery,pk=pk)
    return render(request, 'M_update2.html',{'M_edit2':M_edit2})

def M_update2(request, pk):
    M_update2 = get_object_or_404(Mystery,pk=pk)
    M_update2.title=request.POST['title']
    M_update2.author=request.POST['author']
    M_update2.content=request.POST['content']
    M_update2.save()
    return redirect('list2')

def M_detail2(request, pk):
    M_post2=get_object_or_404(Mystery,pk=pk)
    M_hashtag2=M_post2.hashtag.all()
    return render(request,'M_detail2.html',{'M_post2':M_post2,'M_hashtags2':M_hashtag2})

def M_new2(request):
    form=M_Form()
    return render(request, 'M_new2.html',{'form':form})

def M_create2(request):
    form=M_Form(request.POST, request.FILES)
    if form.is_valid():
        M_post2=form.save(commit=False)
        M_post2.upload_time=timezone.now()
        M_post2.save()
        hashtags2=request.POST['hashtags']
        hashtag2=hashtags2.split(", ")
        for tag in hashtag2:
            new_hashtag=M_HashTag.objects.get_or_create(hashtag=tag)
            M_post2.hashtag.add(new_hashtag[0])
        return redirect('M_detail2',M_post2.id)

def M_delete2(request, pk):
    M_delete2=get_object_or_404(Mystery,pk=pk)
    M_delete2.delete()
    return redirect('list2')

def M_add_comment2(request, pk):
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
    
    return render(request, 'add_comment2.html', {'form':form})

def M_delete_comment2(request,M_post2_id, comment_id):
    M_comment=get_object_or_404(M_Comment, pk=comment_id)
    M_comment.delete()

    return redirect('M_detail2',M_post2_id)

'''Disaster의 CRUD'''

def D_edit2(request, pk):
    D_edit2 = get_object_or_404(Disaster,pk=pk)
    return render(request, 'D_update2.html',{'D_edit2':D_edit2})

def D_update2(request, pk):
    D_update2 = get_object_or_404(Disaster,pk=pk)
    D_update2.title=request.POST['title']
    D_update2.author=request.POST['author']
    D_update2.content=request.POST['content']
    D_update2.save()
    return redirect('list2')

def D_detail2(request, pk):
    D_post2=get_object_or_404(Disaster,pk=pk)
    D_hashtag2=D_post2.hashtag.all()
    return render(request,'D_detail2.html',{'D_post2':D_post2,'D_hashtags2':D_hashtag2})

def D_new2(request):
    form=D_Form()
    return render(request, 'D_new2.html',{'form':form})

def D_create2(request):
    form=D_Form(request.POST, request.FILES)
    if form.is_valid():
        D_post2=form.save(commit=False)
        D_post2.upload_time=timezone.now()
        D_post2.save()
        hashtags2=request.POST['hashtags']
        hashtag2=hashtags2.split(", ")
        for tag in hashtag2:
            new_hashtag=D_HashTag.objects.get_or_create(hashtag=tag)
            D_post2.hashtag.add(new_hashtag[0])
        return redirect('D_detail2',D_post2.id)
        
def D_delete2(request, pk):
    D_delete2=get_object_or_404(Disaster,pk=pk)
    D_delete2.delete()
    return redirect('list2')

def D_add_comment2(request, pk):
    disaster=get_object_or_404(Disaster, pk=pk)

    if request.method=='POST':
        form=D_CommentForm(request.POST)

        if form.is_valid():
            D_comment=form.save(commit=False)
            D_comment.post=disaster
            D_comment.save()
            return redirect('D_detail2', pk)
    else:
        form=D_CommentForm()
    
    return render(request, 'add_comment.html', {'form':form})

def D_delete_comment2(request,D_post2_id, comment_id):
    D_comment=get_object_or_404(D_Comment, pk=comment_id)
    D_comment.delete()

    return redirect('D_detail2',D_post2_id)