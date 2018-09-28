from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^databreak2018$', views.IndexDatabreak2018.as_view(), name='databreak2018'),
    url(r'^databreak2018/coc$', views.IndexCoC.as_view(), name="coc"),
    url(r'^databreak2018/speech/(?P<pk>\d+)/$', views.speech, name="speech"),
    url(r'^databreak2018/sponsorship$', views.IndexSponsorship.as_view(), name="sponsorship"),
    url(r'^databreak2018/speakers', views.IndexSpeakers.as_view(), name="speakers"),
]

