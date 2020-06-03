from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return HttpResponse('Hello world')

from  django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
