from django.conf.urls.defaults import *
from mealplanner.lates.views import dashboard, signup, signupcomplete

urlpatterns = patterns('',
    # Example:
    (r'^dashboard/$', dashboard),
    (r'^$', dashboard),
    (r'^signup/$', signup),
    (r'^signup-complete/$', signupcomplete),
    (r'^signup-complete/(\d+)$', signupcomplete),

)
