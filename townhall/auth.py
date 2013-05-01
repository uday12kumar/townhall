from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from openid.consumer.consumer import SUCCESS
from django.core.mail import mail_admins
from food.models import Food
from townhall import settings
import datetime


class GoogleBackend:  
  def authenticate(self, openid_response):
    if openid_response is None:
      return None
    if openid_response.status != SUCCESS:
      return None
    google_email = openid_response.getSigned('http://openid.net/srv/ax/1.0', 'value.email')
    google_firstname = openid_response.getSigned('http://openid.net/srv/ax/1.0', 'value.firstname')
    google_lastname = openid_response.getSigned('http://openid.net/srv/ax/1.0', 'value.lastname')

    try:
      user = User.objects.get(email = google_email)
      return user
    except User.DoesNotExist:
      return None

  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None


def login_complete(request):
    request.session['loggeduser_email'] = request.GET['openid.ext1.value.old_email']
    request.session['loggeduser_name'] = request.GET['openid.ext1.value.firstname']
    data = ''
    return HttpResponseRedirect('/')
    # return render_to_response("main.html",
    #                                 data,context_instance=RequestContext(request))

