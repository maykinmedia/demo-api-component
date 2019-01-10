from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    url(r'^v(?P<version>(1))/', include('demo_api.api.v1.urls')),
]
