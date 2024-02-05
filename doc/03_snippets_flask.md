# Snippets `flask`

> All the APIs are viewed (i.e. download/upload) from the *Client*'s side.

Basic snippets for the implementation of APIs functionalities: the examples below deal with a single dictionary and / or a single file. The approach can be easily extended to multiple dictionaries/files in order to increase the number of transferred information.

## Packages

Client:

```python
import os
import requests
import base64
import json
```

Server:

```python
import os
from flask import Flask, request, send_file 
import base64
import json
```

## Download

### Dictionary

Client:

```python
req = requests.get(DWN_D_URL)
res = req.json()  # {'message': message}
```

Server:

```python
return {'message': message}
```

### File

Client:

```python
req = requests.get(DWN_F_URL)

file_name = req.headers._store['content-disposition'][1].split("filename=")[1].replace('"','') # retrieve the filename

file_path = f"{file_name}.txt"

with open(file_path, 'wb') as file:
	file.write(req.content)
```

Server:

```python
return send_file(file_path, as_attachment=True, download_name=file_name) 
```

### Dictionary + File

> The file transferred from the server can also be deleted.

Client:

```python
req = requests.post(DWN_DF_URL, json={"text": text})

data = req.json()
```

Server:

```python
text = request.get_json()['text']

with open(file_path, 'rb') as f:
            file_content = f.read() # <class 'bytes'>

# human_readable = file_content.decode('utf-8') # <class 'str'>

# Encode the file content <class 'bytes'> as base64 <class 'str'>
encoded_content = base64.b64encode(file_content).decode('utf-8')

print("File ready to be transferred.")

os.remove(file_path) # 

print(f"{file_name} deleted!")

response_data = {'file_buffer': encoded_content,
				 'message': "from server!",
				 'filename': file_name
				 }

return response_data
```

## Upload

### Dictionary

Client:

```python
req = requests.post(UP_D_URL, json={"text": text})
res = req.json() # {'message': message}
```

Server:

```python
req = request.get_json() # {"text": text}
...
return {'message': message}
```

### File

Client:

```python
files = {'file': open(file_path, 'rb')}
headers = {'filename': file_name}

req = requests.post(UP_F_URL, 
					headers=headers,
					files=files)

res = req.json()
```

Server:

```python
filename = request.headers.get('filename')
file = request.files['file'].read() # <class 'bytes'>
        file_human = file.decode('utf-8') # <class 'str'>

return {"message": "Message from the server"}
```

### Dictionary + File

Client:

```python
files = {'file': open(file_path, 'rb')}
headers = {'filename': file_name}
data = {'text': text}
data = {'data': json.dumps(data)}

req = requests.post(UP_DF_URL, 
					files = files,
					headers=headers, 
					data = data,
					)

data = req.json()
```

Server:

```python
data = json.loads(request.form['data']) # <class 'dict'> {'text': text}
text = data['text']

file_content = request.files['file'].read() # <class 'bytes'>
filename = request.headers.get('filename')

file_human = file_content.decode('utf-8') # <class 'str'> human readable

return {"message": message} 
```

---

<a href="./../readme.md"><< To Index</a>
