from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class recipe_list(ListView):
    model = Recipe
    template_name = "recipe_list.html"

class recipe(DetailView):
    model = Recipe
    template_name = "recipe_info.html"
