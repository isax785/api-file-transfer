# Snippets `Python`

- [ ] write/red file
- [ ] encoding/deciding overview


## Work with files

**Read**

```python
with open(file_path, 'rb') as file:
    file_content = file.read()
```

or

```
file_content = open(file_path, 'rb')
```

**Write**

```python
with open(file_path, 'wb') as file:
    file.write(file_content)
```

## Decoding/Encoding