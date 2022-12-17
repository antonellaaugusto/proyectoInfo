from django import forms
from .models import AgregarComentario


class PostForm(forms.ModelForm):
	class Meta:
		model= AgregarComentario
		fields = ('title', 'author', 'text')


		widgets = { 
		'title' : forms.TextInput(attrs= {'class': 'form-control'}),
		'author' : forms.TextInput(attrs= {'class': 'form-control', 'value':'', 'id':'usuario', 'type':'hidden'}),
		'text' : forms.Textarea(attrs= {'class': 'form-control'}), 
		}