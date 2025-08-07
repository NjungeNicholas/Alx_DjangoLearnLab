from .views import list_books
from .views import LibraryDetailView
from django.urls import path

# URL patterns for the relationship app
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
