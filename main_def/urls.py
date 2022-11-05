from django.urls import path,include
from .views import * 
from . import views

urlpatterns =[
    path('',Page.as_view(),name='pages'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',logout_user,name='logout_user'),
    path('create/',views.page_new,name='create'),
]