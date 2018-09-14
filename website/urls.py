from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^databreak2018$', views.IndexDatabreak2018.as_view(), name='databreak2018'),
]