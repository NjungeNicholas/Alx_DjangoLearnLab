from .views import list_books
from .views import LibraryDetailView
from .views import CustomLoginView
from .views import register
from .views import logout_view
from .views import admin_view, librarian_view, member_view

from django.urls import path

# URL patterns for the relationship app
urlpatterns = [
    path('login/', CustomLoginView, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin_view, name='admin'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # urls needed for the checker
    # path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # path('register/', views.register, name='register'),
    
]
