
from django.shortcuts import render
from .models import Book
from .models import Author

# View to list all available books
def home(request):
    return render(request, 'home.html')


def available_books(request):
    books = Book.objects.filter(available_copies__gt=0) 
    return render(request, 'available_books.html', {'books': books})

def contact_us(request):
    return render(request,'contact_us.html')


def authors(request):
    authors_list = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors_list})

def about_us(request):
    return render(request, 'about_us.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms(request):
    return render(request, 'terms.html')




