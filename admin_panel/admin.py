from django.contrib import admin

# Register your models here.
from .models import Student, CustomImage, VMSize, OSType, Region, VM

admin.site.register(Student)
admin.site.register(CustomImage)
admin.site.register(VMSize)
admin.site.register(OSType)
admin.site.register(Region)
admin.site.register(VM)

