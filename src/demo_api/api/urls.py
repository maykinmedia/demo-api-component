from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    # TODO: Using a version-kwarg and an app_name seems redundant. Might want to
    # switch to namespace versioning.

    url(r'^v(?P<version>(1))/', include('demo_api.api.v1.urls')),
    # Explicitly set the `app_name` to `v2` so we can reverse views
    url(r'^v(?P<version>(2))/', include(('demo_api.api.v2.urls', 'v2'))),
]
