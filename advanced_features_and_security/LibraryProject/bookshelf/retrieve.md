## **retrieve.md**

```markdown
# Retrieve Operation

```python
# Retrieve the book 
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Expected Output:
# 1984 George Orwell 1949


Explanation:  
- Retrieves the book by its title.  
- Prints all attributes.