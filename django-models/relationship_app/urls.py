from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # User Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Other Views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),
]

]
