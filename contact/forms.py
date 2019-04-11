# -*- coding: utf-8 -*-
'''
*@copyright   : ToXSL Technologies Pvt. Ltd. < https://toxsl.com >  
*@author      : Shiv Charan Panjeta < shiv@toxsl.com >
 '''
from smtplib import SMTPException

from django import forms
from django.core.mail import EmailMessage

from django.conf import settings
from contact.models import *


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = ['message','name','email']
