from django.contrib import admin
from django.urls import path
from .views import sign_up, log_in, logout_request #index, 

app_name="accounts"
urlpatterns = [
    # path('',index,name="home"),
    path('',log_in,name="home"),
    path('accounts/sign_up/',sign_up,name="sign-up"),
    path('logout/',logout_request,name="logout")
]