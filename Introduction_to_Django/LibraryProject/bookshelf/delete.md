# Deleting a book

``` python
book = Book.objects.get(id=1)
book.delete()
print(book)
```

## Output

```python
Book object (None)
```
