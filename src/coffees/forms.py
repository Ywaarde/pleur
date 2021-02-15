from django import forms

from .models import Coffee

from roasters.models import Roaster

class CoffeeModelForm(forms.ModelForm):

	forms.ModelChoiceField(queryset=Roaster.objects.all(), required=True)

	class Meta:
		model = Coffee
		fields =[
			'name',
			'roaster',
			'roast_date',
            'best_by_date',
            'notes',
		]
