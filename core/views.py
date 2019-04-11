'''
*@copyright   : ToXSL Technologies Pvt. Ltd. < https://toxsl.com >  
*@author      : Shiv Charan Panjeta < shiv@toxsl.com >
 '''

from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'core/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
