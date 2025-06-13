from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('request/', views.request_assistance, name='request_assistance'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('all-requests/', views.all_requests, name='all_requests'),
]