"""
URL configuration for authuser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from authuser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_user,name='login_user'),
    path('signup/',views.signup,name='signup'),
    path('show/',views.show),
    path('homepage/',views.homepage,name='homepage'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),    
    path('delete/<int:id>',views.destroy, name='destroy'),
    path('crud_home/',views.addnew),
    path('crud_display/', views.inde),
    path('account/login',views.login_user),
    path('logout',views.logout_view),
    path('edit_user/<int:id>/', views.signup_edit, name='signup_edit'),
    path('signup_update/<int:user_id>',views.signup_update, name='signup_update'),
    path('delete_user/<int:id>/',views.signup_destroy,name='signup_destroy'),
]
