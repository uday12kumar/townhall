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
import json
import datetime
import random
import string



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
    restaurants = {}
    restaurant_obj =  Restaurant.objects.all()
    for restaurant in restaurant_obj:
        restaurants[restaurant.restaurant_name] = restaurant.id
    data = { "restaurants":  restaurants}
    return render_to_response("dine.html",
                                      data,
                                      context_instance=RequestContext(request))

def food_items(request):
    resturant_id = request.GET.get('id')
    restaurant_obj =  Restaurant.objects.get(id = resturant_id)
    food_items = eval(restaurant_obj.fooditems)
    return HttpResponse(json.dumps({"food_items":food_items}), mimetype="application/json")
    



