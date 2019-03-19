from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from python_test.views import MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', MainPage.as_view(), name="home"),
]
