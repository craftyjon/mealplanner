from django.conf.urls.defaults import *

from mealplanner.menu.views import *

urlpatterns = patterns('',
    (r'^$', DisplayMenu),
    (r'^edit/$', EditMenu),

)
