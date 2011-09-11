from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from web.genericviews import LoggedInView
from web.mixins import JSONResponseMixin
from web.util.search import Search

class HomeView(LoggedInView, TemplateView):
    template_name = "home.html"

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
