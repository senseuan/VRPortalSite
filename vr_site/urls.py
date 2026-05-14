from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('experiences/', views.experiences, name='experiences'),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name='vr_site/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='index'), name="logout"),
]