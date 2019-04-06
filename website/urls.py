from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^about/$', views.IndexAbout.as_view(), name='about'),
    url(r'^people/$', views.IndexPeople.as_view(), name='people'),
    url(r'^activity/$', views.IndexActivity.as_view(), name='activity'),
    url(r'^activity/(?P<a_id>\d+)/$', views.each_activity, name="each_activity"),
    url(r'^archive/$', views.IndexArchive.as_view(), name='archive'),
    url(r'^sponsor/$', views.IndexSponsor.as_view(), name="sponsor"),
    url(r'^databreak2018/$', views.IndexDatabreak2018.as_view(), name='databreak2018'),
    url(r'^databreak2018/coc/$', views.IndexCoC.as_view(), name="coc"),
    url(r'^databreak2018/speech/(?P<pk>\d+)/$', views.speech, name="speech"),
    url(r'^databreak2018/sponsorship/$', views.IndexSponsorship.as_view(), name="sponsorship"),
    url(r'^databreak2018/speakers/$', views.IndexSpeakers.as_view(), name="speakers"),
    url(r'^databreak2018/notifications/$', views.IndexNotifications.as_view(), name="notifications"),
    url(r'^databreak2018/spon_ticket/$', views.IndexSponTicket.as_view(), name="spon_ticket"),
    url(r'^databreak2018/gallery/$', views.gallery, name="gallery"),
]
