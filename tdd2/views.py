# index view. Not blog application view.

from django.views.generic import ListView

from blog.models import Entry

# TemplateView needs to be ListView 
# from django.views.generic.base import TemplateView


class HomeView(ListView):
    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')