from django.urls import path
from .views import *

app_name = 'services'

urlpatterns = [
    path('', home, name='Home'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('A-propos-de-nous/', about, name='about'),
    path('services/', nosServices, name='services'),
]
