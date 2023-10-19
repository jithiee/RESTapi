from django.shortcuts import render
from django.http import JsonResponse ,HttpResponse
from . models import Product
from django.forms.models import model_to_dict
import json
# Create your views here.

def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.title
        # data['price'] = model_data.price
        data = model_to_dict(model_data,fields=['id','title','price'])
        json_data = json.dumps(data)
    return HttpResponse (json_data, headers={"content-type":"application/json"})

        
    
