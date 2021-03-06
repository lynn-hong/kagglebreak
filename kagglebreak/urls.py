from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin', admin.site.urls),
    url(r'', include('website.urls')),
]

handler404 = 'website.views.not_found'
