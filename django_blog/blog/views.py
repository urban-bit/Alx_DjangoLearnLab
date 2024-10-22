from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views  # Import Django's built-in authentication views
from django.urls import reverse_lazy

# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            messages.success(request, "Registration successful.")
            return redirect('profile')  # Redirect to the profile page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Use Django’s built-in LoginView
class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'  # Specify your custom login template
    redirect_authenticated_user = True  # Redirect users if they are already logged in

# Use Django’s built-in LogoutView
class CustomLogoutView(auth_views.LogoutView):
    template_name = 'registration/logged_out.html'  # Specify a template for logged-out users (optional)

# Profile View
@login_required
def profile(request):
    user = request.user
    return render(request, 'registration/profile.html', {'user': user})

# Edit Profile View
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect('profile')
    return render(request, 'registration/edit_profile.html', {'user': user})
