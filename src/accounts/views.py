from django.shortcuts import render

# from datetime import timezone
from django.utils import timezone
# Create your views here.

#View called from activation email. Activate user if link didn't expire (48h default), or offer to
#send a second link if the first expired.

from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

def activation(request, key):
    # activation_expired = False
    # already_active = False
    profile = get_object_or_404(User, emailSecretKey=key)
    if profile.is_active == False:
        if timezone.now() > profile.emailSecretKeyExpirationDTTM:
            # activation_expired = True #Display: offer the user to send a new activation link
            # id_user = profile.id
            return HttpResponse("Activation link expired.")
        else: #Activation successful
            profile.is_active = True
            profile.emailSecretKey = 'NULL',
            profile.emailSecretKeyExpirationDTTM = timezone.now()
            profile.save()

    #If user is already active, simply display error message
    else:
        # already_active = True #Display : error message
        return HttpResponse("Email Already Verified")
    return HttpResponse("Email successfully verified.")
