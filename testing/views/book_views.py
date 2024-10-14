from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy 
from django.contrib import messages 
from ..models import Book
from ..forms import BookForm

class BookListView(ListView): 
    model = Book 
    template_name = 'books/book_list.html' 
    context_object_name = 'books' 
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        name = self.request.GET.get('name') 
        if name: 
            queryset = queryset.filter(name__icontains=name)
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'name': 
            queryset = queryset.order_by('name')
        elif sort_by == '-name': 
            queryset = queryset.order_by('-email')
        return queryset
            

class BookCreateView(CreateView): 
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html' 
    success_url = reverse_lazy('books_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Book created successfully!')
        return super().form_valid(form)
    
class BookUpdateView(UpdateView): 
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html' 
    success_url = reverse_lazy('books_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Book updated successfully!')
        return super().form_valid(form)
    
class BookDetailView(DetailView): 
    model = Book 
    template_name = 'books/book_detail.html'
    context_object_name = 'book' 

def book_delete_view(request, pk): 
    book = get_object_or_404(Book, pk) 
    if request.method == "POST": 
        book.delete() 
        messages.success(request, "Book deleted successfully!")
    return redirect('book_list')
    
    