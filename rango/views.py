from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }}
	category_list = Category.objects.order_by('-likes')[:5]
	pageviews_list = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': category_list,
					'pageviews': pageviews_list}

	# Return a rendered response to send to the client
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'aboutmessage': 'This page is brought to you by Alex'}
	return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['pages'] = None

	return render(request, 'rango/category.html', context_dict)

