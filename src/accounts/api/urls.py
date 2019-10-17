from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from django.urls import path, reverse
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

from .views import (
    UserCreateAPIView,
    IsUsernameExistAPIView,
    IsEmailExistAPIView,
    ChangePasswordView,
    CurrentUserDetails,
    UserUpdate,
    # Logout
    # ResetPasswordRequest
    )

urlpatterns = [
    # url(r'^', include('rest_registration.api.urls'))
    url(r'^login/$', obtain_jwt_token),
    url(r'^tokenRefresh/', refresh_jwt_token),
    url(r'^register/', UserCreateAPIView.as_view(), name='register'),
    url(r'^isUsernameExist/', IsUsernameExistAPIView.as_view(), name='isUsernameExist'),
    url(r'^isEmailExist/', IsEmailExistAPIView.as_view(), name='isEmailExist'),
    url(r'^changePassword/', ChangePasswordView.as_view(), name='forgotPassword'),
    url(r'^me/', CurrentUserDetails.as_view(), name='me'),
    url(r'^update/', UserUpdate.as_view(), name='update'),
    url(r'^passwordReset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
