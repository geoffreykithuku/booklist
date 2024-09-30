from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    # I have modified this to be more flexible
    publication_date = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'number_of_pages', 'price']


# form to update a book

class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'number_of_pages', 'price']
