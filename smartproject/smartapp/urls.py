from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    path ('ok/',views.test,name='test'),

]


