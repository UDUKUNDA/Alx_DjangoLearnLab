from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books.
# Allows read-only access to unauthenticated users.
# Supports filtering, searching, and ordering.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Configure filtering, searching, and ordering backends
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtering: Allow filtering by title, author's name, and publication year.
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Searching: Allow searching by title and author's name.
    search_fields = ['title', 'author__name']
    
    # Ordering: Allow ordering by title and publication year.
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # Default ordering

# DetailView: Retrieve a single book by ID.
# Allows read-only access to unauthenticated users.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Add a new book.
# Restricted to authenticated users only.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom behavior: Ensure valid data is saved (default behavior, but can be customized here)
    def perform_create(self, serializer):
        # Example of custom behavior: Validation logic or data modification before saving
        # Here we just save the serializer, but we could add logic like:
        # serializer.save(owner=self.request.user)
        serializer.save()

# UpdateView: Modify an existing book.
# Restricted to authenticated users only.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom behavior: Handle update
    def perform_update(self, serializer):
        serializer.save()

# DeleteView: Remove a book.
# Restricted to authenticated users only.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
