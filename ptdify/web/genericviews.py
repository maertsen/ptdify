from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator

class LoggedInView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.username = request.user.username
        return super(LoggedInView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LoggedInView, self).get_context_data(**kwargs)
        context['username'] = self.username
        return context
