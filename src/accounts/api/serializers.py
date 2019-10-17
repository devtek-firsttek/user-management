from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import  serializers
import datetime
from django.conf import settings
from rest_framework.authtoken.models import Token

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    Serializer
    )
import json

User = get_user_model()
import hashlib
import random
from django.core.mail import send_mail
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=30)
    confirmed_password = serializers.CharField(required=True, max_length=30)

    def validate(self, data):
        # add here additional check for password strength if needed
        if not self.context['request'].user.check_password(data.get('old_password')):
            raise serializers.ValidationError({'old_password': 'Wrong old password.'})

        if data.get('confirmed_password') != data.get('password'):
            raise serializers.ValidationError({'password': 'Password must be confirmed correctly.'})

        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    @property
    def data(self):
        # just return success dictionary. you can change this to your need, but i dont think output should be user data after password change
        return {'Success': True}


class UserCreateSerializer(serializers.ModelSerializer):
    email = EmailField(label='Email Address')
    dob = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'timeZone',
            'state',
            'dob'
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        return data


    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email")
        
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value



    def create(self, validated_data):
        data = self.get_initial()
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username = username,
                email = email,
                timeZone = data.get("timeZone"),
                state = data.get("state"),
                dob = data.get("dob")
            )
        user_obj.set_password(password)
        
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        usernamesalt = username
        if isinstance(usernamesalt, bytes):
            usernamesalt = usernamesalt.encode('utf8')
        secretKey = hashlib.sha1((salt+usernamesalt).encode('utf-8')).hexdigest()
        user_obj.emailSecretKey = secretKey
        user_obj.emailSecretKeyExpirationDTTM = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
        user_obj.save()
        
        link= settings.BASE_URL+"accounts/activate/"+secretKey
        message = "Thank you for joining with Brawl Street \n \n Please verify you email id to continue login. \n \n URL : "+ link
        send_mail("Brawl Street Activation Link", message, 'Brawl Street <devtek.firsttek@gmail.com>', [email], fail_silently=False)
        
        return validated_data
        


    @property
    def data(self):
        data = self.get_initial()
        # just return success dictionary. you can change this to your need, but i dont think output should be user data after password change
        return {'status': True, "message" : "Please confirm your email address to complete the registration", "response" : data}






class IsUsernameExistSerializer(ModelSerializer) :
    username = CharField()
    class Meta:
        model = User
        fields = [
            'username'
        ]
    def validate(self, data):
        # username = data['username']
        # user_qs = User.objects.filter(username=username)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data


    def validate_username(self, value):
        data = self.get_initial()
        username = data.get("username")
        user_qs = User.objects.filter(username=username)
        if user_qs.exists():
            raise ValidationError("This username has already registered.")

        return value

class IsEmailExistSerializer(ModelSerializer) : 
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'email'
        ]
    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data


    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email")
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This email has already registered.")

        return value

class CurrentUserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "last_login",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "date_joined",
            "address",
            "city",
            "region",
            "postalCode",
            "timeZone",
            "state",
            "phone",
            "dob"
        ]

    # @property
    # def data(self):
    #     # just return success dictionary. you can change this to your need, but i dont think output should be user data after password change
    #     return {'Success': True}

class CurrentUserUpdateSerializer(ModelSerializer) :
    # email = EmailField(label='Email Address')
    # dob = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "address",
            "city",
            "region",
            "postalCode",
            "timeZone",
            "state",
            "phone",
            "dob"
        ]
