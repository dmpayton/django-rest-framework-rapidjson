from django.conf.urls import url, include

urlpatterns = [
    url(r'^test/', include('testapp.urls')),
]
