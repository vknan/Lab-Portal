from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework import generics
from .models import Student, VMSize, OSImage, Region, VM, ErrorLog
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout



# def vm_list(request):
#     vms = VM.objects.all()  # Assuming you have retrieved the VM objects

#     context = {
#         'vms': vms,
#     }

#     return render(request, 'admin_panel/vm_list.html', context)



class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            # Process the deserialized student object
            return Response({'success': True, 'message': 'Student created successfully'})
        else:
            errors = serializer.errors
            # Handle validation errors
            return Response(errors, status=400)








@api_view(['POST'])
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})



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