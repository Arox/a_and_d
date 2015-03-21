from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd_and_d.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^myadmin/', include(myadmin.site.urls)),
    url(r'^admin/editor', include('myadmin.urls', namespace='admin/editor', app_name='myadmin')),
    #url(r'^admin/editor', views.BaseParametrCreateView.as_view()),
)
