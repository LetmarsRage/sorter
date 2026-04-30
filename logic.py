from sorter_gui import *
from sorter import *
from PyQt6.QtWidgets import *
from pathlib import Path

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.sorter = Sorter()

        self.select_folder.clicked.connect(self.choose_folder)
        self.sort.clicked.connect(self.run_sort)

    def choose_folder(self):
        directory = QFileDialog.getExistingDirectory(self, "Select a Directory")
        self.label.setText("You Have Chosen: " + Path(directory).name)
        self.select_folder.setEnabled(False)
        self.sorter.create_and_organize(directory)

    def run_sort(self):
        self.sorter.sort()
        self.label.setText("Sorted Successfully")
        self.sort.setEnabled(False)


