from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    # Make sure to reference the template as "relationship_app/list_books.html"
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view: show library details including all books
class LibraryDetailView(DetailView):
    model = Library
    # Use full path for template
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user immediately after registration
            return redirect('list_books')  # Redirect to some page after login
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect after successful login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# User Logout View
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
