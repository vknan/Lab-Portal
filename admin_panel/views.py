from django.shortcuts import render
from .models import VM

def vm_list(request):
    vms = VM.objects.all()  # Assuming you have retrieved the VM objects

    context = {
        'vms': vms,
    }

    return render(request, 'admin_panel/vm_list.html', context)

