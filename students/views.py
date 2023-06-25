
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index1(request):
    error_message = ''
    if request.user.is_authenticated:
        return redirect('dashboard')  # Replace 'dashboard' with the desired URL name of your dashboard view
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with the desired URL name of your dashboard view
        else:
            error_message = 'Invalid username or password.'

    return render(request, 'login.html', {'error_message': error_message})


@login_required
def dashboard1(request):
    if request.user.is_staff or request.user.is_superuser:
        #return redirect('admin:index')
        logout(request)
        return redirect('login') 
    user = request.user
    # Access user data
    username = user.username
    email = user.email
    user_profile = user.userprofile
    name = user_profile.name

    context = {
        'username': username,
        'email': email,
        'name': name,
        # ... Add other user data fields to the context
    }

    return render(request, 'dashboard.html', context)

def vm(request):
   return render(request, 'vm.html')

def profile(request):
   return render(request, 'profile.html')

def logout1(request):
   logout(request)
   return redirect('login')
  # return HttpResponse('this is profile')