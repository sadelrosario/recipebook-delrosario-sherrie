from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

# Register your models here.
class RecipeInLine(admin.StackedInline):
    model = Recipe

class RecipeIngredients(admin.ModelAdmin):
    model = Recipe 
    inlines = [RecipeInLine]

admin.site.register(RecipeInLine, RecipeIngredients)