# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.core.mail import mail_admins
from django.contrib.sessions.backends.db import SessionStore
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from models import Restaurant, Order
import json, datetime, random, string



def check_user(request):
    if "loggeduser_email" in request.session:
        return render_to_response("main.html",
                                      "",
                                      context_instance=RequestContext(request))
    else:
        return render_to_response("index.html",
                                      "",
                                      context_instance=RequestContext(request))

def home(request):
    return render_to_response("main.html",
                                      "",
                                      context_instance=RequestContext(request))

def dine(request):
    if request.method == "POST":
        data_dict = dict(request.POST)
        orderObj = Order(restaurant_name=request.POST.get("restaurant_name"),
                         email=request.session['loggeduser_email'],
                         fooditem=json.dumps(data_dict),
                         date=datetime.datetime.now(),
                         comment="",
                         cost=0,
                         total_cost=0)
        orderObj.save()
    restaurants = {}
    orderObjects = Order.objects.all()
    restaurant_obj =  Restaurant.objects.all()
    for restaurant in restaurant_obj:
        restaurants[restaurant.restaurant_name] = restaurant.id
    data = {"restaurants":  restaurants,
            "orders": orderObjects}
    return render_to_response("dine.html",
                                      data,
                                      context_instance=RequestContext(request))

def food_items(request):
    resturant_id = request.GET.get('id')
    restaurant_obj =  Restaurant.objects.get(id = resturant_id)
    food_items = eval(restaurant_obj.fooditems)
    return HttpResponse(json.dumps({"food_items":food_items}), mimetype="application/json")
    



