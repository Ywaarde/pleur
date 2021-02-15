from django.urls import path
from .views import (
    CoffeeCreateView,
    CoffeeDeleteView,
    CoffeeDetailView,
    CoffeeListView,
    CoffeeUpdateView
)

app_name = 'coffees'
urlpatterns = [
    path('', CoffeeListView.as_view(), name='coffee-list'),
    path('create/', CoffeeCreateView.as_view(), name='coffee-create'),
    path('<int:id>/', CoffeeDetailView.as_view(), name='coffee-detail'),
    path('<int:id>/update/', CoffeeUpdateView.as_view(), name='coffee-update'),
    path('<int:id>/delete/', CoffeeDeleteView.as_view(), name='coffee-delete'),
]