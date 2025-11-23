```markdown
# Update Operation
 
# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)

# Expected Output:
# Nineteen Eighty-Four

Explanation:  
- Updates the `title` and saves it.  
- Verification confirms the update.
