from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Players(AbstractUser):
    PLAYER_STATUS_TYPE = (
       ("1" , "Active"),
       ("0" , "Inactive"),
       ("2" , "Suspended")
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_active = models.IntegerField(_('is_active'), choices = PLAYER_STATUS_TYPE, default=0, help_text="Player Status Ind")
    email = models.EmailField(max_length=254, unique=True, null=False)
    address = models.TextField (_('address'), blank=True, null=True, help_text="Address")
    city = models.CharField (_('city'), max_length=255, blank=True, null=True, help_text="City")
    region = models.CharField (_('region'), max_length=255, blank=True, null=True, help_text="Region")
    postalCode = models.CharField (_('postalCode'), max_length=255, blank=True, null=True, help_text="Postal Code")
    timeZone = models.CharField (_('timeZone'), max_length=255, null=False, help_text="Time Zone")
    state = models.CharField (_('state'), max_length=255, null=False, help_text="State")
    phone = models.BigIntegerField(_('phone'), null=True, blank=True, help_text="Phone Number")
    dob = models.DateField(_("dob"), auto_now_add=True, help_text="Date of Birth")
    
    # playerStatusId = models.CharField(_('playerStatusId'),max_length=5 , choices = PLAYER_STATUS_TYPE, default=1, help_text="Player Status Ind")

    # password key and token moved to another table
    # PWDSecretKey = models.TextField (_('PWDSecretKey'), blank=True, null=True, help_text="Password Secret Key")
    # PWDSecretKeyExpirationDTTM = models.DateTimeField(_('PWDSecretKeyExpirationDTTM'), blank=True, null=True, help_text="Password Secret Key Expiration Date Time")

    emailSecretKey = models.TextField (_('EmailSecretKey'), blank=True, null=True, help_text="Email Secret Key")
    emailSecretKeyExpirationDTTM = models.DateTimeField(_('EmailSecretKeyExpirationDTTM'), blank=True, null=True, help_text="Email Secret Key Expiration Date Time")

    # def __str__(self):
    #     return self.username
    
    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})










