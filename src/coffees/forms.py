from django import forms

from .models import Coffee


class CoffeeModelForm(forms.ModelForm):
	class Meta:
		model = Coffee
		fields =[
			'name',
			'roaster',
			'roast_date',
            'best_by_date',
            'notes',
		]