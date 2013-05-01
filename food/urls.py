from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('food.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^home$', 'home', name='home'),
    url(r'^dine$', 'dine', name='dine'),
)