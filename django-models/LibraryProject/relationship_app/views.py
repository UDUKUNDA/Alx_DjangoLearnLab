from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book, Author
from django.http import HttpResponse


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

# Admin view
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# Librarian view
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

# Member view
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        publication_year = request.POST.get("publication_year")

        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(
            title=title,
            author=author,
            publication_year=publication_year
        )
        return HttpResponse("Book added successfully!")

    authors = Author.objects.all()
    return render(request, "relationship_app/add_book.html", {"authors": authors})

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return HttpResponse("Book updated!")

    return render(request, "relationship_app/edit_book.html", {"book": book})
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return HttpResponse("Book deleted!")

    return render(request, "relationship_app/delete_book.html", {"book": book})
