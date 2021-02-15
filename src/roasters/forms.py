from django import forms

from .models import Roaster

class RoasterModelForm(forms.ModelForm):
	class Meta:
		model = Roaster
		fields = [
			'name',
			'city',
			'country',
			'website',
		]