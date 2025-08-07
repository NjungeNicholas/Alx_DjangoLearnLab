from . import views
from django.urls import path

# URL patterns for the relationship app
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
