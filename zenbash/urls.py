from django.conf.urls import include, url
from django.contrib import admin
from zblog.views import IndexView, EntradaDetailView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),

    url(r'^$', IndexView.as_view()),
    url(r'^art/(?P<slug>[-\w]+)/$', EntradaDetailView.as_view()),
    url(r'^index2/', 'zblog.views.home', name='home'),
    #url(r'^form/', 'zblog.views.', name='form'),
]
