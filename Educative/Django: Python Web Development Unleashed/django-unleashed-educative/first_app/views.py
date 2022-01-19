from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms

def index(request):
	""" """
	return HttpResponse('<h1>Hello World</h1>')

def show_age(request, age):
	return HttpResponse(f'<h2>I am {age} years old</h2>')

def even_odd(request, num):
	if num & 1:
		output = f'{num} is odd'
	else:
		output = f'{num} is even'
	return HttpResponse(output)

def list_of_books(request):
	my_data = {
		'user': 'Imran',
		'books': ['The Kite Runner', 'The Forty Rules of Love', 'Honour', 'A Christmas Carol'],
		'value': 'We are learning Filters',
	}
	return render(request, 'first_app/index.html', context=my_data)

def form(req):
	# send default value
	initial_data = {
		'q': 'Imran Potter',
		'v': 'imran-dev@yandex.com',
		'y': 'Hello WOrld',
	}
	form = forms.SearchForm(initial=initial_data)

	if req.method == 'POST':
		form = forms.SearchForm(req.POST, initial=initial_data)
		if form.is_valid():
			print('Forms have been Submitted & printing Info')
			print(f"Name {form.cleaned_data['q']}")
			print(f"Email {form.cleaned_data['v']}")
			print(f"Password {form.cleaned_data['w']}")
			print(f"Is Watched {form.cleaned_data['x']}")
			print(f"Message {form.cleaned_data['y']}")
			return HttpResponseRedirect("/fav-books/")

	return render(req, 'first_app/forms.html', {'forms': form})


def form_2(req):
	x = forms.PostModelForm()
	return render(req, 'first_app/x.html', {'x': x})