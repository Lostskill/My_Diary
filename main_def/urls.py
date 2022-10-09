from django.urls import path,include
from .views import * 

urlpatterns =[
    path('',Main.as_view(),name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('page/',Page.as_view(),name='page')
]