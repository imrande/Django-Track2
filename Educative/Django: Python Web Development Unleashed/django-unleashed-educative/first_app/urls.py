from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	#path('<int:num>/', views.even_odd, name='even_odd'),
	# Dynamic routing without converter
	#path('<str:age>/', views.show_age, name='show_age'),
	path('forms/', views.form, name='form'),
	path('v2/', views.form_2)
]