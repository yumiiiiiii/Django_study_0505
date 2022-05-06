from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from drama.models import Romance, Mystery, Disaster

def List2(request):
    posts2=Romance.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    M_posts2=Mystery.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    D_posts2=Disaster.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time')
    contexts={'posts2':posts2, 'M_posts2':M_posts2, 'D_posts2':D_posts2}
    return render(request, 'list2.html', contexts)

def detail2(request, pk):
    post2=get_object_or_404(Romance,pk=pk)
    return render(request,'detail2.html',{'post2':post2})

def M_detail2(request, pk):
    M_post2=get_object_or_404(Mystery,pk=pk)
    return render(request,'M_detail2.html',{'M_post2':M_post2})

def D_detail2(request, pk):
    D_post2=get_object_or_404(Disaster,pk=pk)
    return render(request,'D_detail2.html',{'D_post2':D_post2})