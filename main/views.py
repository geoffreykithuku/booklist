from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, UpdateBookForm
from django.contrib import messages

# Create your views here.

# view to create a new book
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully')
            return redirect('list_books') 
        else:
            messages.error(request, 'Error adding book')
            return render(request, 'create_book.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})

# view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# view to update a book
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = UpdateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully')
            return redirect('list_books') 
        else:
            return render(request, 'update_book.html', {'form': form, 'book': book})
    else:
        form = UpdateBookForm(instance=book)
        return render(request, 'update_book.html', {'form': form, 'book': book})  

# view to delete a book
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully')
    return redirect('list_books') 
