from django.conf.urls.defaults import *
from django.contrib import admin
from local_settings import MEDIA_URL

from mealplanner.home.views import homepage

admin.autodiscover()

urlpatterns = patterns('',
    (r'^lates/', include('mealplanner.lates.urls')),
    (r'^menu/', include('mealplanner.menu.urls')),
    #(r'^cook/', include('mealplanner.cook.urls')),
    #(r'^clean/', include('mealplanner.clean.urls')),
    (r'^cook/', 'django.views.generic.simple.direct_to_template', {'template': 'comingsoon.htm', 'extra_context': {'media_url':MEDIA_URL}}),
    (r'^clean/', 'django.views.generic.simple.direct_to_template', {'template': 'comingsoon.htm', 'extra_context': {'media_url':MEDIA_URL}}),
    ('^$', homepage),


    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
