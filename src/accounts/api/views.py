from django.db.models import Q
from django.contrib.auth import get_user_model


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from . import serializers
from rest_framework.permissions import IsAuthenticated 

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

# from posts.api.permissions import IsOwnerOrReadOnly
# from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination


#reset password

# from django.dispatch import receiver
# from django_rest_passwordreset.signals import reset_password_token_created
# from django.template.loader import render_to_string, get_template

# from django.core.mail import EmailMessage
# from django.template import Context, Template, RequestContext
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect


User = get_user_model()


from .serializers import (
    UserCreateSerializer,
    IsUsernameExistSerializer,
    IsEmailExistSerializer,
    ChangePasswordSerializer,
    CurrentUserDetailsSerializer,
    CurrentUserUpdateSerializer,
    # AuthCustomTokenSerializer
    )

import hashlib
import random

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    
        
class IsUsernameExistAPIView(APIView):
    serializer_class = IsUsernameExistSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = IsUsernameExistSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class IsEmailExistAPIView(APIView):
    serializer_class = IsEmailExistSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = IsEmailExistSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

class CurrentUserDetails(RetrieveAPIView) : 
    serializer_class = CurrentUserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

class UserUpdate(UpdateAPIView) : 
    serializer_class = CurrentUserUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user



# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
#     """
#     Handles password reset tokens
#     When a token is created, an e-mail needs to be sent to the user
#     :param sender:
#     :param reset_password_token:
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     # send an e-mail to the user
#     context = {
#         'current_user': reset_password_token.user,
#         'username': reset_password_token.user.username,
#         'email': reset_password_token.user.email,
#         # ToDo: The URL can (and should) be constructed using pythons built-in `reverse` method.
#         'reset_password_url': "http://127.0.0.1:8000/reset-password/?token={token}".format(token=reset_password_token.key)
#     }

#     # render email text
#     email_html_message = render_to_string('user_reset_password.html', context)
#     email_plaintext_message = render_to_string('user_reset_password.txt', context)

#     msg = EmailMultiAlternatives(
#         # title:
#         _("Password Reset for {title}".format(title="Brawl Street")),
#         # message:
#         email_plaintext_message,
#         # from:
#         "devtek.firsttek@gmail.com",
#         # to:
#         [reset_password_token.user.email]
#     )
#     msg.attach_alternative(email_html_message, "text/html")
#     msg.send()
 
 
# class Logout(APIView):
#     permission_classes = (IsAuthenticated,)
    
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)












