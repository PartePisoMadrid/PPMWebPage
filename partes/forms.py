from django import forms

from .models import Parte

class ParteForm(forms.ModelForm):
	class Meta:
		model = Parte
		fields = [
			'title',
			'shareMessage',
			'shared'
		]

	def clean_title(self, *args, **kwargs):
# 		monthsList = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
		title = self.cleaned_data.get('title')
		if not ("Semana " == title[:7]):
 			raise forms.ValidationError('The title must start by "Semana de nº de (month)"')
# 		if not ("Semana " == title[:7] and title[7:9].isnumeric() and title[9:]=" "):
# 			raise forms.ValidationError('The title must start by "Semana de nº de (month)"')
# 		if not any(month == title[10:] for month in monthsList):
# 			raise forms.ValidationError('The title must contain a month')
		return title
