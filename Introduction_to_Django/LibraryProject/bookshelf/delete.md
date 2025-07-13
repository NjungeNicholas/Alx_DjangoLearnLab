# Deleting a book

``` python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
print(book)
```

## Output

```python
Book object (None)
```
