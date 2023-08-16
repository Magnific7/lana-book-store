from django.shortcuts import render
from .models import Book

# Create your views here.
def Index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

