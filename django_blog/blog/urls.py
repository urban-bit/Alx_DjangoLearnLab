from django.urls import path
from .views import register, profile, edit_profile, CustomLoginView, CustomLogoutView

urlpatterns = [
    # Registration URL
    path('register/', register, name='register'),

    # Login using Django's built-in LoginView
    path('login/', CustomLoginView.as_view(), name='login'),

    # Logout using Django's built-in LogoutView
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Profile and Edit Profile URLs
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]