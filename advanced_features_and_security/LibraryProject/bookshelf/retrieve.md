# Retrieving and displaying all attributes

``` python
from library.models import Book
```

## Retrieve the first Book

```python
book = Book.objects.get(id=1)

from django.forms.models import model_to_dict
model_to_dict(book)
```

## Output

``` python
{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}
```
