from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Guess what?</h1>")
	return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"my_name": "Bob",
		"my_number": 666,
		"my_list": [1,2,4]
	}
	return render(request, "about.html", my_context)