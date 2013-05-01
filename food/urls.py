from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('food.views',
    # Examples:
    url(r'^$', 'check_user', name='check_user'),
    url(r'^home$', 'home', name='home'),
    url(r'^dine$', 'dine', name='dine'),
    url(r'^get_items_list$', 'get_items_list', name='get_items_list'),
    
)
