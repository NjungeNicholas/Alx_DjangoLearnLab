from .views import list_books
from .views import LibraryDetailView
from .views import CustomLoginView
from .views import register
from .views import logout_view

from django.urls import path

# URL patterns for the relationship app
urlpatterns = [
    path('login/', CustomLoginView, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
