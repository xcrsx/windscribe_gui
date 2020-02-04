
from dialog import Ui_Dialog
from PySide2 import QtWidgets, QtCore


class Login(Ui_Dialog, QtWidgets.QDialog):

    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("login")
        self.setAutoFillBackground(True)
        self.setWindowFlags(QtCore.Qt.Window)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sourceLabel.setText("<a href=\"https://windscribe.com/signup\">Have not register yet?</a>")
        self.sourceLabel.setTextFormat(QtCore.Qt.RichText)
        self.sourceLabel.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.sourceLabel.setOpenExternalLinks(True)
        