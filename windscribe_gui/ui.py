from PySide2 import QtCore, QtWidgets
from mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.accountStatus