from PyQt6.QtWidgets import *
from sorter_gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.choose_folder)
    def choose_folder(self):
        dialog = QFileDialog()
        dialog.setDirectory(QFileDialog.getExistingDirectory())
        dialog.setViewMode(QFileDialog.ViewMode.List)
        dialog.selectFile()
