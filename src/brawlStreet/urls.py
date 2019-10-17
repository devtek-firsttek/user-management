"""brawlStreet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, reverse
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
admin.site.site_header = 'User Management Administration' 
admin.site.site_title = 'User Management' 
admin.site.index_title = 'Dashboard' 
 
urlpatterns = [
    
    #swagger link
    url(r'^$', schema_view),
    
    #admin link
    path('admin/', admin.site.urls),
    
    #api's
    url(r'^api/accounts/', include(("accounts.api.urls", "accounts"), namespace='accounts-api')),
    
    #view
    url(r'^accounts/', include(("accounts.urls", "accounts"), namespace='accounts-view')),
]
