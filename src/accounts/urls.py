from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from django.urls import path, reverse
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

from accounts.views import activation

urlpatterns = [
    url(r'^activate/(?P<key>\w+)/$', activation , name='activation'),
]
