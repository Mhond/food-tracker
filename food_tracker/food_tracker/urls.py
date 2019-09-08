"""food_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(('food.urls','food'), namespace="food")),

    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='auth_login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(next_page='food:login'), name='auth_logout'),
	url(r'^accounts/password/change$', auth_views.PasswordChangeView.as_view (template_name='password_change.html',success_url=reverse_lazy('food:login')),name='auth_password_change'),

]
