from django.shortcuts import render
from django.shortcuts import render, redirect
from django.template import Context, loader
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from models import *
from django.db import connection, transaction
from django.views.decorators.csrf import csrf_exempt
import json
# from django.core.urlresolvers import reverse_lazy
# import requests
# from django.db.models import Q
import md5
import urllib, re
import hashlib
from django.db import IntegrityError
from django.contrib.auth import authenticate

def allstores(request):
	allstores = (Storedetails.objects.values('id','store_name', 'store_location'))
	return render(request, "allstores.html", {"stores":allstores})

def enterstore(request):
	if request.GET:
		a = request.GET.get('newstoreinput')
		b  =  hashlib.md5(a).hexdigest()
		c = Storedetails()
		c.store_name = a
		c.store_hash = b
		p = request.GET.get('location')
		q = request.GET.get('description')
		c.store_location = p
		c.store_description = q 
		c.save()
	return render(request,'enterstore.html',{})

def newstore(request):
	return render(request,"newstore.html",{})

def store(request):
	storeid = request.GET.get('store')
	datas = Storedetails.objects.filter(id=storeid).values('store_name','store_location','store_description')
	alldata = list(datas)
	data2 = alldata[0]
	name = data2['store_name']
	location = data2["store_location"]
	description = data2["store_description"]

	return render(request,'store.html',{"name":name,"location":location,"description":description})