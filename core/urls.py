# -*- coding: utf-8 -*-

'''
*@copyright   : ToXSL Technologies Pvt. Ltd. < https://toxsl.com >  
*@author      : Shiv Charan Panjeta < shiv@toxsl.com >
 '''
from django.conf.urls import url

from .views import *

app_name='core'

urlpatterns = [

    url(r'^$', IndexPageView.as_view(), name='index'),
]
