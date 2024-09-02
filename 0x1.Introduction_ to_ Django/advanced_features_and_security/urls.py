from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page view
    path('author/<int:id>/', views.author_detail, name='author_detail'),  # Author detail view
    path('book/<int:id>/', views.book_detail, name='book_detail'),  # Book detail view
    path('library/<int:id>/', views.library_detail, name='library_detail'),  # Library detail view
    path('librarian/<int:id>/', views.librarian_detail, name='librarian_detail'),  # Librarian detail view
]
