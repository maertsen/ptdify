from django.conf.urls.defaults import *
from django.views.generic import ListView
from web.models import Action, Area, Context, Project

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Action.objects.all()[:5],
            context_object_name='latest_action_list')),
    url(r'^view/actions$',
        ListView.as_view(
            queryset=Action.objects.all()),
        name="action_list"),
    url(r'^view/areas$',
        ListView.as_view(
            queryset=Area.objects.all()),
        name="area_list"),
    url(r'^view/contexts$',
        ListView.as_view(
            queryset=Context.objects.all()),
        name="context_list"),
    url(r'^view/projects$',
        ListView.as_view(
            queryset=Project.objects.all()),
        name="project_list"),
)
