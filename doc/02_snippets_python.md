# Snippets `Python`

Some useful snippets belonging to the Python base libraries.

## Browse Folders

In the snippet below (same order):

- file path
- file folder
- path of `another_folder`

```python
import os

FILE_PATH = os.path.abspath(__file__)
FILE_DIR = os.path.dirname(FILE_PATH)
FOLDER_PATH = os.path.join(FILE_DIR, "another_folder")
```

## Create a Folder

Function that creates a directory and handles the exception if such a directory already exists:

```python
def make_directory(self):
    try:
        os.mkdir(self.export_folder)
    except Exception as e:
        print(f"Warning creating export folder: {e}")
```

## Work with Files

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

**Delete**

```python
import os 

os.remove(file_path)
```

## Decoding/Encoding

Decoding and encoding of an information.


**Example 1**

1. read the content of a file `<class 'bytes'>`
2. decode the content into a human readable format `<class 'str'>`

```python
with open(file_path, 'rb') as f:
    file_content = f.read() # <class 'bytes'>

human_readable = file_content.decode('utf-8') # <class 'str'>
```

**Example 2**

1. read the content of a file `<class 'bytes'>`
2. encode as base 64 `<class 'bytes'>`
3. decode into a human readable format `<class 'str'>`
4. decode the base 64 readable `str` into `bytes`
5. decode the base 64 `bytes` into human readable format

> between the points `3.` and `4.` there could be the transfer of information between a server and a client: the transferred invormation is the bytes64 string that can be easily be passed via `json`.

```python
import base64

with open(file_path, 'rb') as f:
    file_content = f.read() # <class 'bytes'>

encoded_content_bytes = base64.b64encode(file_content) # <class 'bytes'>

encoded_content = encode_content_bytes.decode('utf-8') # <class 'str'> e.g. 'RmlsZSBjcmVhdGVkIGJ5IH...

# decode the base64 <class 'str'> into <class 'bytes'>
file_buffer = base64.b64decode(encoded_content)

human_readable = file_buffer.decode('utf-8') # 'File created by ... => <class 'str'>

```

---

<a href="./../readme.md"><< To Index</a>
