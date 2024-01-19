import sys, os
sys.path.extend([os.path.join(os.path.dirname(os.path.abspath(__file__)), "gui")])

from gui.api_file_transfer_class import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())