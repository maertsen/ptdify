from django.conf.urls.defaults import *
from django.views.generic import ListView
from web.views import *

urlpatterns = patterns('',
    url(r'^$',                  HomeView.as_view(),             name="home"),
    url(r'^ajax/autocomplete$', AutocompleteView.as_view(),     name="autocomplete"),
)
