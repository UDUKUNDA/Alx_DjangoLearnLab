from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Secure form for creating and editing Book objects.
    Using Django ModelForms prevents SQL injection and
    automatically validates and sanitizes user input.
    """
    class Meta:
        model = Book
        fields = ['title', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title
