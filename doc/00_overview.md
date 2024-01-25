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

- client 
  - retrieves the filename from the response header;
  - saves the file locally via the dedicated dialog.
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
  - loads a file via the dedicated dialog;
  - reads the file (`'rb'`) and stores it into a dictionary that will be the request `files`;
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

A `POST` request containing the text edited by the user is sent to the server from the client. The server creates a file `txt` including that text, hour, and date. Then transfers the file to the client together with a confirmation message that will be displayed
The client saves the file locally, reads its content, and writes it into the *client log* text edit together with the server confirmation message.

Specs/Implementation:
- client
  - attach the text into the request;
  - r
- server
  - creates a file into a folder;
  - the file content is the client text + hour annd date;
  - the file is loaded by `ByteIO` to be transferred, then deleted;
  - the file is transferred as bytes with a dictionary containing a message.

`@app.route("/upload_dict_file", methods=['POST'])`

*Like the previous, with the following variant: the client uploads a txt file and a message, the server appends the the message to the txt file. Then it's like the `download_dict_file*

Description:



Specs/Implementation:




