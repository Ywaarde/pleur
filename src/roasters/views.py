from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)

from .forms import RoasterModelForm
from .models import Roaster

# Roaster views

class RoasterCreateView(CreateView):
	template_name = 'roasters/roaster_create.html'
	form_class = RoasterModelForm
	queryset = Roaster.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class RoasterListView(ListView):
	template_name = 'roasters/roaster_list.html'
	queryset = Roaster.objects.all()


class RoasterDetailView(DetailView):
	template_name = 'roasters/roaster_detail.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Roaster, id=id_)

class RoasterUpdateView(UpdateView):
	template_name = 'roasters/roaster_create.html'
	form_class = RoasterModelForm

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Roaster, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class RoasterDeleteView(DeleteView):
	template_name = 'roasters/roaster_delete.html'
	
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Roaster, id=id_)

	def get_success_url(self):
		return reverse('roasters:roaster-list')