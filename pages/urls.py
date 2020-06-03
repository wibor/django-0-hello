from django.urls import path
#from .views import homePage
from .views import HomePageView, AboutPageView

urlpatterns = [
    #path('', homePage, name='home')
    path('',        HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
