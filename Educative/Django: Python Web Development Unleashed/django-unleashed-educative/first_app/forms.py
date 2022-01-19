from django import forms
from . import models

class SearchForm(forms.Form):
	INTS_CHOICES = [tuple([x,x]) for x in range(10)]
	RADIO_CHOICES = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
	q = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'text-input'}))
	v = forms.EmailField(label='Email')
	w = forms.CharField(label='Password', widget=forms.PasswordInput)
	x = forms.BooleanField(label='Watched', initial=True)
	y = forms.CharField(label='Message', widget=forms.Textarea)
	z = forms.IntegerField(label='Select', widget=forms.Select(choices=INTS_CHOICES), initial=5)
	a = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=RADIO_CHOICES), initial='male')

	# custom validation
	def clean_q(self): # django always looking clean_attributrName
		name = self.cleaned_data['q']
		if len(name) <= 5:
			raise forms.ValidationError("Name Must be 6 Chars or long")
		return name


class PostModelForm(forms.ModelForm):
	class Meta:
		model = models.Post
		fields= ["user","title","slug","image","content","draft","publish"]
		exclude = ['user', 'slug']