from django.conf.urls.defaults import *
from django.views.generic import ListView
from web.models import Action

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Action.objects.all()[:5],
            context_object_name='latest_action_list')),
)
