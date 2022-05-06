from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

# Create your views here.

from main.models import Recipe
from main.forms import Form

def List(request):
    recipes = Recipe.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'main.html', {'recipes': recipes})

def Detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'detail.html', {'recipe': recipe})

def create(request):
    if request.method == 'POST': # method가 post일때
        form = Form(request.POST) # form 에 ReviewForm 할당
        if form.is_valid(): # form 유효성 검증
            form.save() # 저장
            return redirect('main') # 다시 main으로
    else:
        form = Form() # 빈 form 열기
    return render(request, 'create.html', {'form' :form})