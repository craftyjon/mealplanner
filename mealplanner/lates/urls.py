from django.conf.urls.defaults import *

from mealplanner.lates.views import *

urlpatterns = patterns('',
    # Example:
    (r'^dashboard/$', dashboard),
    (r'^$', overview),
    (r'^signup/$', signup),
    (r'^broadcast/$', broadcast),
    (r'^signup-complete/$', signupcomplete),
    (r'^signup-complete/(\d+)$', signupcomplete),

)
