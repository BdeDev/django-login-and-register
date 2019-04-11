'''
*@copyright   : ToXSL Technologies Pvt. Ltd. < https://toxsl.com >  
*@author      : Shiv Charan Panjeta < shiv@toxsl.com >
 '''

from django.db import models
from accounts.models import *
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
import sys
from django.forms import ValidationError

from django.utils.translation import gettext_lazy as _
import imghdr

class ContactUs(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    message = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return str(self.name) + str(self.email)
    
    class Meta:
        managed = True
        verbose_name_plural = 'Contact Us'