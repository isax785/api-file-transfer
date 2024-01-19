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


*file + dictionary from client*

Client:
```python
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
