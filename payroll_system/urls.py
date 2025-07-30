# payroll_system/urls.py

from django.contrib import admin
from django.urls import path, include
# Import Django's built-in LoginView and LogoutView
from django.contrib.auth import views as auth_views 
from payroll import views as payroll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', payroll_views.home_view, name='home'), 
    
    # Add the login and logout URLs
    path('login/', auth_views.LoginView.as_view(template_name='payroll/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('payroll/', include('payroll.urls')), 
]