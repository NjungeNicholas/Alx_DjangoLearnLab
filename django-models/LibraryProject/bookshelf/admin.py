from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    list_filter = ('author', 'publication_year')           # Filters on sidebar
    search_fields = ('title', 'author')                   # Search box fields

admin.site.register(Book, BookAdmin)