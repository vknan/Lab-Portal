from rest_framework import serializers
from .models import Student, VMSize, OSImage, Region, VM, ErrorLog

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class VMSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMSize
        fields = '__all__'

class OSImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSImage
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class VMSerializer(serializers.ModelSerializer):
    class Meta:
        model = VM
        fields = '__all__'

class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        # Perform any additional validation you need
        # You can also authenticate the user here if required
        return attrs
