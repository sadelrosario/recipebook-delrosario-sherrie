from django.urls import path
from .views import recipe_list, recipe

urlpatterns = [
    path('recipes/list', recipe_list.as_view(), name='list'),
    path('recipe/<int:pk>',recipe.as_view(), name='recipe'),
]

app_name = 'ledger'