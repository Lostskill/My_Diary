from django.urls import path,include
from .views import * 

urlpatterns =[
    path('',Page.as_view(),name='pages'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',logout_user,name='logout_user')
]