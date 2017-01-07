from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }}
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
					'ballmessage': 'Sweaty, beautiful, sweet balls'}

	# Return a rendered response to send to the client
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'aboutmessage': 'This page is brought to you by Alex'}
	return render(request, 'rango/about.html', context=context_dict)
