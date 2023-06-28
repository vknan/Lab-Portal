from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    # Other URL patterns
    
    path('admin_panel/students/create/', TemplateView.as_view(template_name='index.html')),
    # path('api/', include('myapp.urls')),
]
