from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

# Create your views here.

def index(request):
	import requests
	import json
	import time
	
	if request.method == 'POST':
		entity = request.POST['entity1']
		time.sleep(0.20);
		api_request = requests.get('https://cloud.iexapis.com/stable/stock/' + entity + '/quote?token=pk_ad7bf98f094f4195a25c3df912a3f6f6');
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'listing/index.html', {'api' : api });	
	else:
		return render(request, 'listing/index.html', {'entity': "Please type the name of stock in the search box."})
	

def about(request):
	return render(request, 'listing/about.html', {});
	
	
def add_stock(request):
	import requests
	import json
	import time
	if request.method == 'POST':
		form = StockForm(request.POST or None)
		
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Added!"))
			return redirect(add_stock)
			# return HttpResponseRedirect(reverse('listing:add_stock'))
			
	else:
		entity = Stock.objects.all()
		output = []
		for entity_item in entity:
			time.sleep(0.20);
			api_request = requests.get('https://cloud.iexapis.com/stable/stock/' + str(entity_item) + '/quote?token=pk_ad7bf98f094f4195a25c3df912a3f6f6');
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."

		return render(request, 'listing/add_stock.html', {'entity': entity, 'output': output});
		
def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted!"))
	return redirect(add_stock)
	
def delete_stock(request):
	entity = Stock.objects.all()
	return render(request, 'listing/delete_stock.html', {'entity':entity})
