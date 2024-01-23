## Snippets

*dictionary only*

Client:

```python
req = requests.post(url, json=dict_api)
res = req.json()
print(res["message"])
```

Server: 
```python
dict_api = request.get_json()
return {"message": "return from the server"}
```

*file from client (upload)*
*file from server (download)*

Client
```python
req = requests.post(url, json=dict_api)

filename = req.headers._store['content-disposition'][1].split("filename=")[1].replace('"','')

file_path, _ = QFileDialog.getSaveFileName(self, 'Save Help', filename, 'pdf (*.pdf)')

with open(file_path, 'wb') as file:
	file.write(req.content)
```

Server
```python
file_path = "file\path\here"

return send_file(file_path, as_attachment=True, download_name='File Name') 
```

*file + dictionary from client*

Client:
```python
file_path, _ = QFileDialog.getOpenFileName(self, 'Choose Excel File', '', 'Excel Files (*.xlsx *.xls)')
files = {'file': open(file_path, 'rb')}
dict_api = {'dict_login': self.dict_login}
data = {'dict_api': json.dumps(dict_api)}

req = requests.post(url, 
					files = files, 
					data = data,
					)

```

Server:
```python
dict_api = json.loads(request.form['dict_api'])
file = request.files['file']
file_content = file.read()
```


*file + dictionary* from server
- [ ] `???` check reliability

Client
```python
file_path, _ = QFileDialog.getSaveFileName(self, 'Save Excel File', '', 'Excel Files (*.xlsx)')
response = requests.get(url)
local_file_path = 'downloaded_file.txt'
with open(local_file_path, 'wb') as local_file:
	local_file.write(response.content)
		
json_data = response.json() # Load the JSON data from the response
```

Server
```python
sample_file_path = 'sample_file.txt'
with open(sample_file_path, 'w') as file:
	file.write('This is a sample file content.')

sample_data = {'key1': 'value1', 'key2': 'value2'}
response = send_file(sample_file_path, as_attachment=True)
os.remove(sample_file_path)

return jsonify({'data': sample_data}), 200, {'Content-Disposition': 'attachment; filename=sample_file.txt'}
```
