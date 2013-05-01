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
	return render_to_response("dine.html",
                                      "",
                                      context_instance=RequestContext(request))