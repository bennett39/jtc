from django.urls import path
import .views

urlpatterns = [
    path('sandwich/random/', views.random),
    path('sandwich/ingredients/<ingredient>/', views.list_ingredient),
]
