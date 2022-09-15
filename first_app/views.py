
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
import Books
from first_app.models import Book, Publisher


def index(request):
    name = "damilola"
    return render(request, 'index.html', context={"name": name})


def redirect(request):
    return HttpResponseRedirect(reverse('first_app:hello'))


def hello(request, name: str, num: int):
    return HttpResponse(f"<h1>Hello {num}. {name.title()}, Welcome to Django</h1>")


# Create your views here.


def book_list(request):
    with transaction.atomic():
        p1 = Publisher.objects.create(name="thug")
        b1 = Book.objects.create(title="")
        books = Book.objects.raw()
    return render(request, 'first_app/book-list.html', {'books': list(books)})


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        return render(request, '/book-details.html', {'book': book})
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    # OR
    # book = get_object_or_404(Book, pk=pk)
    # return render(request, 'my_app/book-detail.html', {'book': book})


def book_list_for_fiction(request):
    books = Book.objects.filter(genre='FICTION')
    return render(request, 'first_app/book-list-fiction.html', {'books': list(books)})


def book_list_for_price(request):
    books = Book.objects.filter(price__lt=80)
    return render(request, 'first_app/book-list-price.html', {'books': list(books)})

