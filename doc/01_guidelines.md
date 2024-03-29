# Guidelines

Some guidelines for a reliable implementation of the APIs service.

## Basic GUI Architecture

Basic architecture for the implementation of a `PyQt5` gui.

Folder structure:

```
client
╠ gui
║	╠ py
║	║  ╠ mainWindow.py 
║	║  ╚ res_rc.py	
║	╠ res
║	║  ╠ image.png
║	║  ╚ res.qrc 
║	╠ ui
║	║  ╚ mainWindow.ui
║	╚ mainWindow_class.py
╚ main.py
```

`main.py`

```python
import sys, os
sys.path.extend([os.path.join(os.path.dirname(os.path.abspath(__file__)), "gui")])

from PyQt5.QtWidgets import QApplication
from gui.mainwindow_class import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Untitled()
    sys.exit(app.exec_())
```

`gui/mainWindowClass.py`

A window with a push button and a text cell. When the button is clicked, a text is written into the text cell.

```python
from PyQt5.QtWidgets import QMainWindow
from mainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.set_push_button_name()
        self.ui.pushButton.clicked.connect(self.printout)

    def set_push_button_name(self):
	    "Change push button name"
        self.ui.pushButton.setText("Button Name")

    def printout(self):
	    "Write into text cell"
        print("executed") # console printout
        self.ui.textEdit.setText("Push button text.")
```

## Directory Path

when dealing with files and path it is always useful to have the availability of the current file directory path:

```python
import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
```
## Create, Load, and Delete File

On any side (i.e. client or server) for transferring a file to be deleted:

```python
file_folder = os.path.join(CUR_DIR, "res")
file_name = f"{formatted_datetime()}_server_file.txt"
file_path = os.path.join(file_folder, file_name)

with open(file_path, 'w') as f:
    f.write(text)

print(f"File created: {file_name}")

with open(file_path, 'rb') as f:
    file_content = f.read() # <class 'bytes'>

# Encode the file content <class 'bytes'> as base64 <class 'str'>
encoded_content = base64.b64encode(file_content).decode('utf-8')

print("File ready to be transferred.")

os.remove(file_path)

print(f"{file_name} deleted!")

return_message = "from server!"
```

## APIs Error Handling


A reliable structure for error handling while implementing the APIs:

- both server and client `def` should be enclosed into a `try...except` structure;
- on client side, the second `try...except` allows handling both server and client errors;
- on client side the error can be displayed by a `print` or shown to the user by a `QMessagebox`.

Server:

```python
try:
    ...
    return {"message": "Message from Server"}
except Exception as e:
    return {"message": f"{e}"}   except
```

Client:

```python
try:
    ...
except Exception as e:
    try:
        message = f"Client Error: {e}\nServer Error: {req.json()['message']}\n"
    except:
        message = f"Client Error: {e}\n"
    print(message)

```

---

<a href="./../readme.md"><< To Index</a>
