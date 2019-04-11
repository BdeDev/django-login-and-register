# -*- coding: utf-8 -*-
'''
*@copyright   : ToXSL Technologies Pvt. Ltd. < https://toxsl.com >  
*@author      : Shiv Charan Panjeta < shiv@toxsl.com >
 '''
from django.views.generic.edit import View
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from contact.models import ContactUs

from .forms import ContactForm
from smtplib import SMTPException
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from accounts.tokens import account_activation_token
from django.core.mail import EmailMultiAlternatives


class ContactView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/core/index.html')

    def post(self, request, *args, **kwargs):
        initial = None

        form = ContactForm(initial=initial, data=request.POST)
        
        if form.is_valid():
            form.save()
            current_site = get_current_site(request)
            
            mail_subject = '[Contact form] ' + ''.join(request.POST['subject'].splitlines())
            to_email = request.POST['email']            
            
            context = {
                'email':request.POST['email'], 'message':request.POST['message'],
            }

                
            email_message = EmailMultiAlternatives(mail_subject, '', settings.EMAIL_HOST_USER, [to_email])
            html_email = render_to_string('frontend/core/contact_email.html',context)
            email_message.attach_alternative(html_email, 'text/html')
            
            try:
                email_message.send()
                messages.info(self.request, 'Thank you for your message. We will be in touch shortly.')
            except SMTPException:
                messages.error(self.request, "There is error processing yor request. Please try again.")
            return redirect('core:index')
        
        messages.error(self.request, "There is error processing yor request. Please try again.")
        return redirect('core:index')
