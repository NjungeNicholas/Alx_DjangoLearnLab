# CREATING A BOOK

## Option 1 : Create and save

``` python
book = Book(title="1984", author="George Orwell", year_published=1949)
book.save()
```

## Option 2: Create in one line

``` python
book = Book.objects.create(title="1984", author="George Orwell", year_published = 1949)
```
