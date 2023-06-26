from django.urls import path, include 
from admin_panel import views 

urlpatterns = [
   path('vm_list/', views.vm_list, name='vm_list'),
   # path('create_user/', views.create_user, name='create_user'),
]