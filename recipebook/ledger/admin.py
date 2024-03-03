from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

# Register your models here.
class RecipeIngreidentsInLine(admin.StackedInline):
    model = RecipeIngredient

class RecipeDetails(admin.ModelAdmin):
    model = Recipe 
    inlines = [RecipeIngreidentsInLine]


admin.site.register(Recipe, RecipeDetails)