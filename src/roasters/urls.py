from django.urls import path
from .views import (
	RoasterListView,
	RoasterCreateView,
	RoasterDetailView,
	RoasterUpdateView,
	RoasterDeleteView
)

app_name = 'roasters'
urlpatterns = [
	path('', RoasterListView.as_view(), name='roaster-list'),
	path('create/', RoasterCreateView.as_view(), name='roaster-create'),
	path('<int:id>/', RoasterDetailView.as_view(), name='roaster-detail'),
	path('<int:id>/update/', RoasterUpdateView.as_view(), name='roaster-update'),
	path('<int:id>/delete/', RoasterDeleteView.as_view(), name='roaster-delete'),
]