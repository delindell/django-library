import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import Library
from ..connection import Connection
from ..books.details import get_book


def get_libraries():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.title,
            l.address
        from libraryapp_library l
        """)

        return db_cursor.fetchall()

@login_required
def book_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'books/form.html'
        context = {
            'all_libraries': libraries
        }

        return render(request, template, context)

@login_required
def book_edit_form(request, book_id):

    if request.method == 'GET':
        book = get_book(book_id)
        libraries = get_libraries()

        template = 'books/form.html'
        context = {
            'book': book,
            'all_libraries': libraries
        }

        return render(request, template, context)
