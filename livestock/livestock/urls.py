"""livestock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from stock import views
from django.contrib.auth import views as auth_views
from seller import views as seller_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',views.StockCreateView.as_view(),name='stock_create'),
    path('',views.StockListView.as_view(),name='home'),
    path('stock/',include('stock.urls',namespace='stock')),
    path('register/', seller_views.register, name='register'),
    path('profile/', seller_views.profile, name='profile'),
    path('dashboard/', seller_views.DashboardView.as_view(), name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='seller/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='seller/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='seller/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='seller/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='seller/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='seller/password_reset_complete.html'
         ),
         name='password_reset_complete'),




 ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
