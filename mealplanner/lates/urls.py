from django.conf.urls.defaults import *

from mealplanner.lates.views import dashboard, signup, signupcomplete, overview

urlpatterns = patterns('',
    # Example:
    (r'^dashboard/$', dashboard),
    (r'^$', overview),
    (r'^signup/$', signup),
    (r'^signup-complete/$', signupcomplete),
    (r'^signup-complete/(\d+)$', signupcomplete),

)
