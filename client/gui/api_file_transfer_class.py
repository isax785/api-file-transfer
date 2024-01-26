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
        try:
            req = requests.get(DWN_F_URL)
            file_name = req.headers._store['content-disposition'][1].split("filename=")[1].replace('"','')
            file_path, _ = QFileDialog.getSaveFileName(self, 'Save Help', file_name, 'txt (*.txt)')
            with open(file_path, 'wb') as file:
                file.write(req.content)
        except Exception as e:
            print(f"Error: {e}")

    def upload_file(self):
        # upload a file belonging to the allowed types
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, 'Text readable file', '', '*.txt *.md *.py')
            file_name = file_path.split('/')[-1]
            files = {'file': open(file_path, 'rb')}
            headers = {'filename': file_name}

            req = requests.post(UP_F_URL, 
                                headers=headers,
                                files=files)

            res = req.json()
            self.ui.log_txt.setPlainText(res['message'])
            
        except Exception as e:
            print(f"Error: {e}")

    def download_dict_file(self):
        try:
            text = self.ui.df_text.toPlainText()
            req = requests.post(DWN_DF_URL, json={"text": text})

            file_name = req.headers._store['content-disposition'][1].split("filename=")[1].replace('"','')
            file_path, _ = QFileDialog.getSaveFileName(self, 'Save Help', file_name, 'txt (*.txt)')
            with open(file_path, 'wb') as file:
                file.write(req.content)

            data = req.json()['data']
            message = data["message"]
            self.ui.log_txt.setPlainText(message)

        except Exception as e:
            print(f"Error: {e}")

        pass

    def upload_dict_file(self):
        req = requests.post(UP_DF_URL)
        # file_path, _ = QFileDialog.getOpenFileName(self, 'Open Custom Table', '', 'Excel Files (*.xlsx *.xls)')
        # files = {'file': open(file_path, 'rb')}
        # dict_api = {'dict_login': self.dict_login}
        # data = {'dict_api': json.dumps(dict_api)}

        # req = requests.post(url, 
        #                     files = files, 
        #                     data = data,
        #                     )

        # print(req) # D
        # res = req.json()
        # self.ch_models_custom = res['ch_models_custom']
        
        pass
