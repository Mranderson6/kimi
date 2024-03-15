from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', home, name='Home'),
    path('blog/<int:id>/', blogDetails, name='detail-post'),
    path('categorie-details/<int:id>/', categoryDetails, name='categorieDetails')
]
