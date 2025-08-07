from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author'
        }
        help_texts = {
            'title': 'Enter the full title of the book',
            'author': 'Select the author from the dropdown'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make sure all authors are available in the dropdown
        self.fields['author'].queryset = Author.objects.all().order_by('name')
        
        # Make fields required
        self.fields['title'].required = True
        self.fields['author'].required = True

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title:
            title = title.strip()
            if len(title) < 2:
                raise forms.ValidationError("Title must be at least 2 characters long.")
        return title
