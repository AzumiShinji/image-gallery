from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^imgup/', include('imgup.urls')),
    url(r'^admin/', admin.site.urls),
]
