from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', book_list, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='books'),
    path('librarians/', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarians'),
    path('libraries/', list_libraries, name='libraries'),
    path('library/form', library_form, name='library_form'),
    path('libraries/<int:library_id>/', library_details, name='libraries'),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name="register"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
