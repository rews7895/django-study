from django.views.generic.base import TemplateView
from django.apps import apps
from django.http import HttpResponseRedirect
from django.urls import reverse


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['app_list'] = ['polls', 'books']
        dictVerbose = {}
        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
        context['verbose_dict'] = dictVerbose
        return context


def home(request):
    return HttpResponseRedirect(reverse('posts:index'))
