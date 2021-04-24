from django.shortcuts import render
from .models import Book

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import BookForm


def main_page(request):
    books = Book.objects.all()
    return render(request, 'base.html', {'books': books})


def novelty(request):
    books = Book.objects.filter(published=True).order_by('-published_date')[0:5]
    return render(request, 'novelty.html', {'books': books})


class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('main_page')
    template_name = 'upload_book.html'
