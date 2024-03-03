from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

# def recipe_list(request):
#     list_links = Recipe.objects.all()
#     ctx = { "links": list_links }
#     return render(request, 'recipe_list.html', ctx)
    

# def recipe(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     ctx = { "recipe" : recipe }
#     return render(request, 'recipe_info.html', ctx)
    

class recipe_list(ListView):
    model = Recipe
    template_name = "recipe_list.html"

class recipe(DetailView):
    model = Recipe
    template_name = "recipe_info.html"
