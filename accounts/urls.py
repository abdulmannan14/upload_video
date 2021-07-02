from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [

    path('', home,name='home'),
    path('login', login_attempt,name='login'),
    path('register', register_attempt,name='register'),
    path('token', token_send,name='token'),
    path('success', success,name='success'),
    path('verify<auth_token>', verify,name='verify'),
    path('error', error,name='error'),
    path('logout/', logout_task,name='logout'),

]