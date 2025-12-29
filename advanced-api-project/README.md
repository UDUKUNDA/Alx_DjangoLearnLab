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

### Validation
- **BookSerializer**: Custom validation ensures that `publication_year` cannot be in the future.

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
