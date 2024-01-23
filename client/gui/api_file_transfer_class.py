from PyQt5.QtWidgets import QMainWindow, QFileDialog
from py.api_file_transfer import Ui_MainWindow
import requests

# QPlainTextEdit
# Widgets of interest:
# self.ui.d_btn_dwn - dict
# self.ui.d_btn_up
# self.ui.d_txt
# self.ui.f_btn_dwn - file
# self.ui.f_btn_up
# self.ui.df_btn_dwn - dict + file
# self.ui.df_btn_up
# self.ui.df_txt
# self.ui.log_txt - log
LOCALHOST = 'http://127.0.0.1:5000'
DWN_D_URL = f"{LOCALHOST}/download_dict"
UP_D_URL = f"{LOCALHOST}/upload_dict"
DWN_F_URL = f"{LOCALHOST}/download_file"
UP_F_URL = f"{LOCALHOST}/upload_file"
DWN_DF_URL = f"{LOCALHOST}/download_dict_file"
UP_DF_URL = f"{LOCALHOST}/upload_dict_file"


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_widgets()
        self.show()

    def connect_widgets(self):
        self.ui.d_btn_dwn.clicked.connect(self.download_dict)
        self.ui.d_btn_up.clicked.connect(self.upload_dict)
        self.ui.f_btn_dwn.clicked.connect(self.download_file)
        self.ui.f_btn_up.clicked.connect(self.upload_file)
        self.ui.df_btn_dwn.clicked.connect(self.download_dict_file)
        self.ui.df_btn_up.clicked.connect(self.upload_dict_file)

    def download_dict(self):
        req = requests.get(DWN_D_URL)
        res = req.json()
        self.ui.log_txt.setPlainText(res['message'])

    def upload_dict(self):
        text = self.ui.d_txt.toPlainText()
        req = requests.post(UP_D_URL, json={"text": text})
        res = req.json()
        self.ui.log_txt.setPlainText(res['message'])

    def download_file(self):
        req = requests.get(DWN_F_URL)
        filename = req.headers._store['content-disposition'][1].split("filename=")[1].replace('"','')
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Help', filename, 'txt (*.txt)')
        with open(file_path, 'wb') as file:
            file.write(req.content)

    def upload_file(self):
        # upload any kind of file
        req = requests.post(UP_F_URL)
        pass

    def download_dict_file(self):
        req = requests.post(DWN_DF_URL)
        pass

    def upload_dict_file(self):
        req = requests.post(UP_DF_URL)
        pass
