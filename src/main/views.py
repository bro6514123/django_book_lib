from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import Book, Ganre, Author


def product_list_page(request, slug=None):
    ganres = Ganre.objects.all()
    books = Book.objects.all()
    search = request.GET.get('search')

    ganre = None
    if slug:
        ganre = get_object_or_404(Ganre, slug=slug)
        books = books.filter(ganres=ganre)

    if search:
        books = Book.objects.filter(
            Q(title__icontains=search) |
            Q(author__fullname__icontains=search) |
            Q(ganres__name__icontains=search)
        ).distinct()
    
    context = {
        'ganre': ganre,
        'books': books,
        'ganres': ganres
    }

    return render(request, 'main/list.html', context)

def details_page(request, id):
    book = get_object_or_404(Book, id=id)
    author = book.author
    ganres = Ganre.objects.all()

    context = {
        'book': book,
        'ganres': ganres,
        'author': author
    }

    return render(request, 'main/details.html', context)

def author_page(request, slug):
    author = get_object_or_404(Author, slug=slug)
    ganres = Ganre.objects.all()
    books = author.books.all()

    context = {
        'books': books,
        'ganres': ganres,
        'author': author
    }

    return render(request, 'main/author.html', context)
    

