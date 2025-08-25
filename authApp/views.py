from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from .forms import SignUp, Login

# Example view function
#def home(request):
#    return render(request, 'home.html')
class SignUpView(View):
    def get(self, request):
        form = SignUp()
        return render(request, 'signup.html', {'form': form})
    
    def post(self, request):
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/dashboard')
        return render(request, 'signup.html', {'form': form})
    
class LoginView(View):
    def get(self, request):
        form = Login()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request):
        form = Login(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/dashboard')  # Redirect to a dashboard or home page
        return render(request, 'login.html', {'form': form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login')  # Redirect to login page after logout')  

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')  


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')