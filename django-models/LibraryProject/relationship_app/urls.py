from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,  
)
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    # Function-based view URL
    path('books/', list_books, name='list_books'),

    # Class-based view URL (library detail)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

     # Authentication views
    path('register/', views.register_view, name='register'),  # ALX expects 'views.register' here
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
