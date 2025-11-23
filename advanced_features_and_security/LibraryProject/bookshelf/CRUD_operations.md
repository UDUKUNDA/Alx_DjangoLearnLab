## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: 1984>

## Retrieve

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949

## Update

book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)
# Output: Nineteen Eighty-Four

## Delete 

book.delete()
books = Book.objects.all()
print(books)
# Output: <QuerySet []>
