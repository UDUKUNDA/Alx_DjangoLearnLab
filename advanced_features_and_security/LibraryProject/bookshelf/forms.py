from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Secure form for creating and editing Book objects.
    Helps prevent SQL injection and enforces input validation.
    """
    class Meta:
        model = Book
        fields = ['title', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title


class ExampleForm(forms.Form):
    """
    A simple example form required by the system checker.
    Useful for demonstrating CSRF protection and secure input handling.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
