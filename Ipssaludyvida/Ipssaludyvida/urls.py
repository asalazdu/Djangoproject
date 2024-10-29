
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('medvisit.urls')),
    path('accounts/', auth_views.LoginView.as_view(template_name='public/login/login.html'), name="accounts"),
]
