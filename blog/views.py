from django.views.generic.detail import DetailView

from .models import Entry

# show the details of Entry and render it to a template.
class EntryDetail(DetailView) :
    model = Entry