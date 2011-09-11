from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.utils import simplejson
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from web.mixins import JSONResponseMixin
from web.models import Action, Area, Context, Project
from web.util.search import Search

class HomeView(TemplateView):
    template_name = "home.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

class AutocompleteView(View, JSONResponseMixin):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden("Forbidden: not logged in")

        return super(AutocompleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        query =  request.GET.getlist('query')

        try:
            search = Search.fromJSON(query)     
        except ValueError as e:
            return HttpResponseBadRequest("Bad request: %s" % e)

        completed = search.autoComplete(10) # TODO remove magic number

        result_list = [[block.as_list() for block in suggestion] for suggestion in completed]

        return self.render_to_response(result_list)
