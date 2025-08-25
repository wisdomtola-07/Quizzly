from django.urls import path
from . import views

app_name = 'authApp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("login/", views.LoginView.as_view(), name= "Login"),
    path("signup/", views.SignUpView.as_view(), name= "SignUp"),
    path("logout/", views.LogoutView.as_view(), name="Logout"),
    path("dashboard/", views.DashboardView.as_view(), name="Dashboard"),
]

# these are the patterns for the urls of the application they help us map the urls to the views