"""TV_shows URL Configuration

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
from django.urls import path
from website import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.featured_page, name='featured'),
    path('add_to_favorites/<int:show_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/', views.favorites_page, name='favorites'),
    path('details/<int:show_id>/', views.details_page, name='details'),
    path('add_to_favorites/<int:id>/', views.details_page, name='add_to_favorites'),
    path('remove_from_favorites/<int:show_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
