from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', views.EntryDetail.as_view(), name='entry_detail'),
]