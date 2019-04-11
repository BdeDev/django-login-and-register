'''
*@copyright   : ToXSL Technologies Pvt. Ltd. < https://toxsl.com >  
*@author      : Shiv Charan Panjeta < shiv@toxsl.com >
 '''
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from core.views import IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
