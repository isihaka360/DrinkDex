from django.urls import path
from .views import AddingDrinkView, DeleteDrinkView, DrinkListView, UpdateDrinkView

urlpatterns = [
    path('Drinks/Add', AddingDrinkView.as_view(), name='AddDrinkView'),
    path('Drinks/Delete/<int:pk>', DeleteDrinkView.as_view(), name='DeleteDrinkView'),
    path('Drinks/List', DrinkListView.as_view(), name='DrinkListView'),
    path('Drinks/Update/<int:pk>', UpdateDrinkView.as_view(), name='UpdateDrinkView'),
]
