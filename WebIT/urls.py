from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path

from python_test.views import MainPage, AddClient, SearchClient, ShowClientDetails, ModifyClient, DeleteClient

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', MainPage.as_view(), name="home"),
    re_path(r'^add/', AddClient.as_view(), name="add"),
    re_path(r'^search/', SearchClient.as_view(), name="search"),
    re_path(r'^delete/(?P<id>[0-9]+)$', DeleteClient.as_view(), name="delete"),
    re_path(r'^modify/(?P<id>[0-9]+)$', ModifyClient.as_view(), name = "modify"),
re_path(r'^details/(?P<id>[0-9]+)$', ShowClientDetails.as_view(), name = "ClientDetails"),

]
