from django.urls import path, include
from .views import recipe_list, recipe

urlpatterns = [
    path('recipes/list', recipe_list.as_view(), name='list'),
    path('recipe/<int:pk>',recipe.as_view(), name='recipe'),
    path('accounts/', include('django.contrib.auth.urls'))
]

app_name = 'ledger'