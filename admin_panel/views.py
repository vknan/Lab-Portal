from django.shortcuts import render
from .models import VM
from rest_framework import generics
from .models import Student, VMSize, OSImage, Region, VM, ErrorLog
from .serializers import StudentSerializer, VMSizeSerializer, VMSerializer, ErrorLogSerializer, RegionSerializer, OSImageSerializer


# def vm_list(request):
#     vms = VM.objects.all()  # Assuming you have retrieved the VM objects

#     context = {
#         'vms': vms,
#     }

#     return render(request, 'admin_panel/vm_list.html', context)



class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class VMSizeListAPIView(generics.ListAPIView):
    queryset = VMSize.objects.all()
    serializer_class = VMSizeSerializer
class VMListAPIView(generics.ListAPIView):
    queryset = VM.objects.all()
    serializer_class = VMSerializer
class OSImageListAPIView(generics.ListAPIView):
    queryset = OSImage.objects.all()
    serializer_class = OSImageSerializer

class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ErrorlogListAPIView(generics.ListAPIView):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer