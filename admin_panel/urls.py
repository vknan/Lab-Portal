from django.urls import path, include 

from .views import StudentListAPIView, OSImageListAPIView, VMListAPIView, VMSizeListAPIView, RegionListAPIView, ErrorlogListAPIView
urlpatterns = [
   path('studentapi/', StudentListAPIView.as_view(), name='Student-list'),
   path('OSImageapi/', OSImageListAPIView.as_view(), name='OSImage-list'),
   path('VMapi/', VMListAPIView.as_view(), name='VMapi-list'),
   path('VMSizeapi/', VMSizeListAPIView.as_view(), name='VMSize-list'),
   path('Regionapi/', RegionListAPIView.as_view(), name='Region-list'),
   path('Errorlogapi/', ErrorlogListAPIView.as_view(), name='Errorlog-list'),
]

