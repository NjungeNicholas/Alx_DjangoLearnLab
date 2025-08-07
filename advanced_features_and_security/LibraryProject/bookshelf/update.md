# Updating a field

``` python
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
```

## Output

``` python
{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year'author': 'George Orwell',: 1949}
```
