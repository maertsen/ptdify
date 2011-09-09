from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from web.models import Action, Area, Context, Project
from web.util.search import Search



class LatestActionView(ListView):
    context_object_name='latest_action_list'
    queryset=Action.objects.all()[:5]

class ActionView(ListView):
    def get_queryset(self):
        return Action.objects.for_user(self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ActionView, self).dispatch(*args, **kwargs)

class AreaView(ListView):
    def get_queryset(self):
        return Area.objects.for_user(self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AreaView, self).dispatch(*args, **kwargs)

class ContextView(ListView):
    def get_queryset(self):
        return Context.objects.for_user(self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContextView, self).dispatch(*args, **kwargs)

class ProjectView(ListView):
    def get_queryset(self):
        return Project.objects.for_user(self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectView, self).dispatch(*args, **kwargs)

class AutocompleteView(JSONResponseMixin, View):
    pass

    #@csrf_exempt
    #@method_decorator(login_required)
    #def dispatch(request):
    #    query = simplejson.load(request['data'])
    #
    #    for  in query

def autocomplete(request):
    import pprint

    test = Search([], "abc xyz def action")
    response = pprint.pformat([[obj.__str__() for obj in l] for l in test.autoComplete(10)])

    return HttpResponse(response)
