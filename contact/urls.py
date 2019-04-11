# -*- coding: utf-8 -*-
'''
*@copyright   : ToXSL Technologies Pvt. Ltd. < https://toxsl.com >  
*@author      : Shiv Charan Panjeta < shiv@toxsl.com >
 '''
from django.conf.urls import url

from .views import ContactView

app_name='contact'

urlpatterns = [
    url(r'^$', ContactView.as_view(), name='contact'),
]
