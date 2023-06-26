from django.contrib import admin

# Register your models here.
from .models import Student, VMSize, OSImage, Region, VM, ErrorLog


admin.site.register(Student)
# admin.site.register(CustomImage)
admin.site.register(VMSize)
admin.site.register(OSImage)
admin.site.register(Region)
admin.site.register(VM)
admin.site.register(ErrorLog)

