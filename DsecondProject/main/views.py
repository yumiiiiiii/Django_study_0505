from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.db.models import Q
from .models import Ingredient

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

def delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('main')

def update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = Form(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            #form.save_m2m() save(commit=False)를 사용할 경우 -> 다대다 모델은 ID가 없으면 생성 못해서 부모 모델이 생긴 뒤에 저장한다. 
            return redirect('detail', pk=recipe.id)
        else:
            return redirect('main')
    else:
        form = Form(instance=recipe)
        return render(request, 'update.html', {'form':form})

class SearchResultsView(ListView):
    model=Recipe
    template_name="search_results.html"

    def get_queryset(self):  #get_queryset은 모든 request마다 동작, query_set은 앱이 시작할 때 한번만 동작. 필터값이 동적일 경우 get_queryset이 적합
        query=self.request.GET.get("q")
        object_list=Recipe.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)|
            Q(ingredients__name__contains=query)
        ).distinct

        return object_list