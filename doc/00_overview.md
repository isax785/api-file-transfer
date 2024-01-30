# Overview

Here below a brief description of the implemented APIs, including their usage and the specs.

## Download Dictionary

`@app.route("/download_dict", methods=['GET'])`

Description:

A simple `GET` request is sent by the client, and a message including datetime is returned. The message is then displayed by the *client log* text edit.

Specs/Implementation:

- server response is a dictionary 

## Upload Dictionary

`@app.route("/upload_dict", methods=['POST'])`

Description:

A message is sent by the client via a `POST` request, then the read message is returned by the server slightly modified.

Specs/Implementation:

- client request contains a dictionary as `json`
- server response is a dictionary

## Download File

`@app.route("/download_file", methods=['GET'])`

Description:

A simple `GET` request is sent by the client and a `txt` file is downloaded by the server. The file is saved by the client into a path defined by the user.

Specs/Implementation:

- client 
  - retrieves the filename from the response header;
  - saves the file locally via the dedicated dialog.
- server response with the file via `send_file` method (`flask` library)

## Upload File

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

# Download Dictionary and File

`@app.route("/download_dict_file", methods=['POST'])`

Description:

A `POST` request containing the text edited by the user is sent to the server from the client. The server creates a file `txt` including that text, hour, and date. Then transfers the file to the client together with a confirmation message that will be displayed
The client saves the file locally, reads its content, and writes it into the *client log* text edit together with the server confirmation message.

Specs/Implementation:
- client
  - attaches the text into the request as `json`;
  - retrieves the returned message from the response and displays it into the *client log* text edit;
  - reads the file from the response and saves it.
- server
  - creates a file into a folder with datetime into the name;
  - the file is written: it contains a message with the client text + hour and date;
  - the file is loaded and encoded (`base64`), allowing to delete the file
  - both the file and the message are transferred by a `json`


# Upload Dictionary and File

`@app.route("/upload_dict_file", methods=['POST'])`

Description:

A `POST` request containing the text edited by the user is sent to the server from the client together with a file. The server reads both the text and the file and returns a message that is the composition of the client message and the file content. The client reads the server message and writes it into the *client log* text edit.

Specs/Implementation:

- client
  - attaches the text into the request as `json`;
  - reads the file and attaches its content (bytes) into a json;
  - send the filename writing it into the header;
  - writes the server message into the *client log*;
- server
  - reads the client message from the `json`;
  - reads the filename from the header;
  - reads the file content by decoding it into a human readable format;
  - composes and returns the message.




