from django.conf.urls import patterns, url

from views import BaseParametrCreateView

urlpatterns = patterns('',
    #url(r'^$', views.list_objects),
    url(r'parametr/create$', BaseParametrCreateView.as_view(), name='Create parametr'),
)