from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('hello1/', hello1, name="hello1"),
    path('', newhomepage, name='newhomepage'),
    path('travelpackage/', travelpackage, name='travelpackage'),
    path('print_to_console/',print_to_console,name='print_to_console'),
    path('print1/', print1, name='print1'),
    path('randomcall/',randomcall,name='randomcall'),
    path('randomlogic/',randomlogic, name='randomlogic'),
    path('getdate1/',getdate1,name='getdate1'),
    path('get_date/',get_date,name='get_date'),
    path('registerloginfunction1/',registerloginfunction1,name='registerloginfunction1'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),
    path('feedback/', feedback, name='feedback'),
    path('feedbackform/', mainfeedback, name='mainfeedback'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('login1/', login1, name='login1'),
    path('signup1/', signup1, name='signup1'),


]

