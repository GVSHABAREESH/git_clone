from django.conf.urls import url,include
from django.contrib import admin
from appname.viewsets import classnameviewsets
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'^world',classnameviewsets)

urlpatterns = [
    url(r'^', include(route.urls)),
]