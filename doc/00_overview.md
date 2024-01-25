# Overview

Here below a brief description of the implemented APIs, including their usage and the specs.

`@app.route("/download_dict", methods=['GET'])`

Description:

A simple `GET` request is sent by the client, and a message including datetime is returned. The message is then displayed by the *client log* text edit.

Specs/Implementation:

- server response is a dictionary 

`@app.route("/upload_dict", methods=['POST'])`

Description:

A message is sent by the client via a `POST` request, then the read message is returned by the server slightly modified.

Specs/Implementation:

- client request contains a dictionary as `json`
- server response is a dictionary


`@app.route("/download_file", methods=['GET'])`

Description:

A simple `GET` request is sent by the client and a `txt` file is downloaded by the server. The file is saved by the client into a path defined by the user.

Specs/Implementation:

- client retrieves the filename from the response header
- server response with the file via `send_file` method (`flask` library)

`@app.route("/upload_file", methods=['POST'])`

Description:

A file is uploaded by the client via a `POST` request. Also the filepath is sent (into the header). The server:
- reads the filepath, and parses it to retrieve the filename;
- reads the file and decodes it to a human-readable string;
- returns a message including the filename and the file content.
The response is then displayed by the *client log* text edit. 

Specs/Implementation:

- client
  - reads a file (`'rb'`) and stores it into a dictionary that will be the request `files`;
  - stores the filepath into another dictionary that will be the request `headers`;
  - request includes `headers` and `files`;
  - reads the returned message by response `.json()`.
- server
  - reads the filepath from `headers` and parses it to retrieve the filename;
  - reads the file form `files` and decodes it into human-readable format;
  - returns the message to the client into a dictionary.
- exception handling and message returning the same dictionary structure.

`@app.route("/download_dict_file", methods=['GET'])`

Description:



Specs/Implementation:




`@app.route("/upload_dict_file", methods=['POST'])`

Description:



Specs/Implementation:




