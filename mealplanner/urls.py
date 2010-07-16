from django.conf.urls.defaults import *
from django.contrib import admin

from mealplanner.lates.views import overview

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^lates/', include('mealplanner.lates.urls')),
    ('^$', overview),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
