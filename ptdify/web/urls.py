from django.conf.urls.defaults import *
from django.views.generic import ListView
from web.views import *

urlpatterns = patterns('',
    url(r'^$',              LatestActionView.as_view()),
    url(r'^view/actions$',  ActionView.as_view(),     name="action_list"),
    url(r'^view/areas$',    AreaView.as_view(),       name="area_list"),
    url(r'^view/contexts$', ContextView.as_view(),    name="context_list"),
    url(r'^view/projects$', ProjectView.as_view(),    name="project_list"),
)
