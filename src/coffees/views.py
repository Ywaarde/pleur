from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)

from .forms import CoffeeModelForm
from .models import Coffee

# Coffee views

class CoffeeCreateView(CreateView):
	template_name = 'coffees/coffee_create.html'
	form_class = CoffeeModelForm
	queryset = Coffee.objects.all() # <blog>/<modelname>_list.html
	#success_url = '/'

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	#def get_success_url(self):
	#    return '/'

class CoffeeListView(ListView):
	template_name = 'coffees/coffee_list.html'
	queryset = Coffee.objects.all() # <blog>/<modelname>_list.html


class CoffeeDetailView(DetailView):
	template_name = 'coffees/coffee_detail.html'
	#queryset = Coffee.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Coffee, id=id_)


class CoffeeUpdateView(UpdateView):
	template_name = 'coffees/coffee_create.html'
	form_class = CoffeeModelForm

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Coffee, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class CoffeeDeleteView(DeleteView):
	template_name = 'coffees/coffee_delete.html'
	
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Coffee, id=id_)

	def get_success_url(self):
		return reverse('coffees:coffee-list')