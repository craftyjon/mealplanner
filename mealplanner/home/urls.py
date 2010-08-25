from django.conf.urls.defaults import *

from mealplanner.main.views import *

urlpatterns = patterns('',
    (r'^$', homepage),
)
