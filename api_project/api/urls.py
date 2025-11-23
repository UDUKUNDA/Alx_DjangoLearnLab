from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing list view
    path('books/', BookList.as_view(), name='book-list'),

    # Include router URLs (all CRUD operations)
    path('', include(router.urls)),
]
