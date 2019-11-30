from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('registration',views.registration,name='registration'),
    path('test',views.test,name='test'),
    path('terminal',views.terminal,name='terminal')
]