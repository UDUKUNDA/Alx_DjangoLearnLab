from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books.
# Allows read-only access to unauthenticated users.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
