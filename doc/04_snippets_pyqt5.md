# Snippets `PyQt5`

A useful toolbox for a lightweight `PyQt5` implementation.


## Sender

**Sender**

```python
# Identify the widget that triggered the signal 
sender_widget = self.sender()
```

Common properties and methods that can be used to identify the sender:

1. `text()`: If the sender is a widget with text (e.g., `QPushButton`, `QLabel`), you can use `self.sender().text()` to get the text content of the widget.
2. `objectName()`: If you have set an object name for the widget using `setObjectName`, you can use `self.sender().objectName()` to retrieve it.
3. `property()`: You can use `self.sender().property(propertyName)` to retrieve the value of a custom property set on the widget.

## Widgets

### `ComboBox`

```python
from PyQt5.QtWidgets import QComboBox

self.comboBox = QComboBox(self)

# add single item or list of items
self.comboBox.addItem("item")
self.comboBox.addItems([list of items])
# clear all items
self.comboBox.clear()
# read current (selected) text
self.comboBox.currentText()
# connect a function to be executed when selecting a value
self.comboBox.currentIndexChanged.connect(self.comboBoxSelectionChanged)
# retrieve the selected index
selected_index = self.comboBox.currentIndex()
# set the value by index
self.comboBox.setCurrentIndex(1)
# retrieve the index of a specific value
index = self.comboBox.findText("value")
# block the signal (to be re-enabled once finished)
self.comboBox.blockSignals(True)
```

### `Table`

```python
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QMainWindow

...

self.tableWidget = QTableWidget(self) 

# Initialize size
self.tableWidget.setRowCount(5)
self.tableWidget.setColumnCount(3)

# set stylesheet
self.ui.tableWidget.setStyleSheet("QTableView::item:selected { background-color: #36827F; text-color: white}")

# set selection behavior
self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
self.ui.tableWidget.setSelectionMode(QTableWidget.MultiSelection) # Multiple row selection

# fill table (single column) with list components (multiple rows)
self.ui.tableWidget.setRowCount(len(listName))
self.ui.tableWidget.setColumnCount(1)
self.ui.tableWidget.setHorizontalHeaderLabels(['Chiller Name'])
for i, value in enumerate(self.ch_models):
	self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(value))

# count rows/columns
self.ui.tableWidget.rowCount()
self.ui.tableWidget.columnCount()

# select all
self.ui.tableWidget.selectAll()

# deselect all selected
self.ui.tableWidget.clearSelection()

# automatic column resizing
self.ui.tableWidget.resizeColumnsToContents()

# Extract the row numbers from the selected items
selected_items = self.ui.tableWidget.selectedItems()
for item in selected_items:
    row = item.row()
    if row not in selected_rows:
        selected_rows.append(row)

# Select full row 
item = self.ui.tableWidget.item(row, 0)  # row:int
if item:
	row = item.row()
	for col in range(self.table_cols_nr):
		self.ui.tableWidget.item(row, col).setSelected(True)

# automatically select all rows
for row in range(self.ui.tableWidget.rowCount()):
	item = ... # se "Select full row"

# table sorting from header
self.ui.tableWidget.setSortingEnabled(True) 

# delete all records (rows)
self.tableWidget.setRowCount(0)

```

### `CheckBox`

```python
from PyQt5.QtWidgets import QCheckBox

self.checkBox = QCheckbox(self)

# Set initial text for the checkbox
checkbox.setText('Check me!')
# connect to a function when checking/unchecking
self.checkBox.stateChanged.connect(self.any_function)
# True/False if checked/unchecked
self.checkbox.isChecked()
# set checkbox state
self.checkbox.setChecked(True)
# Disable the checkbox
self.checkbox.setEnabled(False)
```

### `MessageBox`

With application to an error:

```python
from PyQt5.QtWidgets import QMessageBox 

try:
	...
except Exception as e: 
	self.showErrorMessageBox(str(e))

def showErrorMessageBox(self, error_message):
	msg_box = QMessageBox()
	msg_box.setIcon(QMessageBox.Critical)
	msg_box.setWindowTitle("Error")
	msg_box.setText(f"An error occurred:\n{error_message}")
	msg_box.exec_()
```

### `PlainTextEdit`

```python
from PyQt5.QtWidgets QPlainTextEdit

self.text_edit = QPlainTextEdit(self)

# clear text
self.text_edit.clear()
# read text
text = self.text_edit.toPlainText()
# write text
text = self.text_edit.setPlainText(text_to_write)
```

### `LineEdit`

```python
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLineEdit

self.line_edit = QLineEdit(self)

...

# Write text into the QLineEdit
self.line_edit.setText('Hello, PyQt!')

# Read text from the QLineEdit
text = self.line_edit.text()
print(f'Read Text: {text}')

# Set a specific text into the QLineEdit
self.line_edit.setText('New Text Set')

# set color
self.line_edit.setStyleSheet(f'color: {color.name()}')

# Open a QColorDialog to set text color
color = QColorDialog.getColor()
if color.isValid():
	# Set the text color of the QLineEdit
	self.line_edit.setStyleSheet(f'color: {color.name()}')
```

### `PushButton`

```python
from PyQt5.QtWidgets import QPushButton

btn = QPushButton('Button Text', self)

# close the window where the push button is by connecting to the `close` method
btn.clicked.connect(self.close)
```

## Cursor

```python
QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
QApplication.restoreOverrideCursor()
```

## `FileDialog`

```python
from PyQt5.QtWidgets import QFileDialog

...

# Save file
file_path, _ = QFileDialog.getSaveFileName(self, 'Save Help', file_name, 'txt (*.txt)')

# Open file
file_path, _ = QFileDialog.getOpenFileName(self, 'Text readable file', '', '*.txt *.md *.py')
```

---

<a href="./../readme.md.md"><< To Index</a>