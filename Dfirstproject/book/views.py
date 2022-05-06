from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from book.models import Romance, Mystery, Disaster

def List(request):
    posts=Romance.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    M_posts=Mystery.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    D_posts=Disaster.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    contexts={'posts':posts, 'M_posts':M_posts, 'D_posts':D_posts}
    return render(request, 'list.html', contexts)

def detail(request, pk):
    post=get_object_or_404(Romance,pk=pk)
    return render(request,'detail.html',{'post':post})

def M_detail(request, pk):
    M_post=get_object_or_404(Mystery,pk=pk)
    return render(request,'M_detail.html',{'M_post':M_post})

def D_detail(request, pk):
    D_post=get_object_or_404(Disaster,pk=pk)
    return render(request,'D_detail.html',{'D_post':D_post})