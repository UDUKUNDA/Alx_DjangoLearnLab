# Advanced API Project

## Overview
This project implements a comprehensive API for managing books and authors using Django REST Framework (DRF). It demonstrates the use of generic views, custom serialization validation, permissions, and URL routing.

## Features

### Models
- **Author**: Represents a writer.
- **Book**: Represents a book written by an author, linked via a ForeignKey.

### API Endpoints
The API uses DRF's generic views to provide CRUD operations for the `Book` model.

| Endpoint | Method | View Class | Description | Permissions |
|----------|--------|------------|-------------|-------------|
| `/api/books/` | GET | `BookListView` | Retrieve a list of all books. | Read-only for unauthenticated users. |
| `/api/books/<id>/` | GET | `BookDetailView` | Retrieve details of a specific book. | Read-only for unauthenticated users. |
| `/api/books/create/` | POST | `BookCreateView` | Create a new book. | Authenticated users only. |
| `/api/books/update/<id>/` | PUT/PATCH | `BookUpdateView` | Update an existing book. | Authenticated users only. |
| `/api/books/delete/<id>/` | DELETE | `BookDeleteView` | Delete a book. | Authenticated users only. |

### Permissions
- **ListView & DetailView**: Accessible to everyone (Read-Only). `IsAuthenticatedOrReadOnly` ensures that unauthenticated users can only view data.
- **CreateView, UpdateView, DeleteView**: Restricted to authenticated users (`IsAuthenticated`).

### Advanced Features (Filtering, Searching, Ordering)
The `BookListView` endpoint (`/api/books/`) supports powerful query parameters to refine results:

**1. Filtering**
Filter books by exact matches on specific fields.
- **By Author Name**: `/api/books/?author__name=J.K. Rowling`
- **By Publication Year**: `/api/books/?publication_year=1997`
- **By Title**: `/api/books/?title=Harry Potter`

**2. Searching**
Perform text searches across `title` and `author` fields.
- **Search**: `/api/books/?search=Potter` (Matches "Potter" in title or author name)

**3. Ordering**
Sort the results by specific fields. Use a hyphen `-` for descending order.
- **Order by Title (A-Z)**: `/api/books/?ordering=title`
- **Order by Publication Year (Newest first)**: `/api/books/?ordering=-publication_year`

**Combinations**
You can combine these parameters:
- *Example*: Find books by "J.K. Rowling" published in "1997", ordered by title:
  `/api/books/?author__name=J.K. Rowling&publication_year=1997&ordering=title`

### Validation
- **BookSerializer**: Custom validation ensures that `publication_year` cannot be in the future.

## Testing
This project includes a comprehensive test suite to verify the functionality of the API. The tests cover:
- **CRUD Operations**: Ensuring books can be created, read, updated, and deleted.
- **Permissions**: Verifying that unauthenticated users have read-only access and cannot modify data.
- **Advanced Features**: Testing filtering, searching, and ordering capabilities.

### Running Tests
To run the tests, use the following command:
```bash
python manage.py test api
```

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install django djangorestframework
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Run Server**:
   ```bash
   python manage.py runserver
   ```

4. **Access API**:
   Navigate to `http://127.0.0.1:8000/api/books/` in your browser or use a tool like Postman.
