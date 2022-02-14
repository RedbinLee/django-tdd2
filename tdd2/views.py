# index view. Not blog application view.

from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'