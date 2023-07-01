from django.urls import path, include 
from students import views 

urlpatterns = [
   path('', views.index1, name='login'),
   path('dashboard/', views.dashboard1, name='dashboard'),
   path('dashboard/vm', views.vm, name='vm'),
   path('dashboard/profile', views.profile, name='profile'),
   path('login/', views.student_login, name='student_login'),
   path('logout', views.logout1, name='logout'),
]
