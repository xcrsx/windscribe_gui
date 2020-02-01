import os
import subprocess
import pexpect

from PySide2 import QtCore, QtWidgets, QtGui, Qt
from mainwindow import Ui_MainWindow
from .login_window import Login

US_C = "US Central"
US = "US East"
US_W = "US West"
CA = "Canada East"
CA_W = "Canada West"
FR = "France"
DE = "Germany"
NL = "Netherlands"
NO = "Norway"
RO = "Romania"
CH = "Switzerland"
GB = "United Kingdom"
HK = "Hong Kong"
SERVER_LIST = ["choose server", US_C, US, US_W, CA, CA_W, FR, DE,
                NL, NO, RO, CH, GB, HK]
servers = {
    US_C: "US_C",
    US: "US",
    US_W: "US_W",
    CA: "CA",
    CA_W: "CA_W",
    FR: "FR",
    DE: "DE",
    NL: "NL",
    NO: "NO",
    RO: "RO",
    CH: "CH",
    GB: "GB",
    HK: "HK"
    }

class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.informLabel.setText("Welcome to Windscribe GUI") # displays info
        self.mainButton.setVisible(False) # changes name and connects to different slots
        self.logoutButton.setVisible(False)
        self.comboBox.setVisible(False)
        self.comboBox.addItems(SERVER_LIST)
               

        self.status = None # info which displays in statusbar
        self.log_window = Login() # dialog window 

        self.actionAccountStatus.triggered.connect(self.get_account_info)
        # self.actionLogout.triggered.connect(self.log_out)
        self.log_window.accepted.connect(self.log_in)
        self.logoutButton.clicked.connect(self.log_out)
        self.mainButton.clicked.disconnect()
       
    def get_account_info(self) -> None:

        self.mainButton.setVisible(True)
        account = pexpect.spawn("windscribe account")
        status = account.expect(["Please login to use Windscribe",
                                " ------- My Account ------- *"])
        if status == 0:
            self.logoutButton.setVisible(False)
            self.mainButton.setText("Log In")
            # self.actionShowLoginDialog.triggered.connect(self.show_login_dialog)
            self.mainButton.clicked.connect(self.show_login_dialog)
        elif status == 1:
            self.logoutButton.setVisible(True)
            display_info = account.read().split(b"\r\n")
            for i in range(len(display_info)):
                display_info[i] = display_info[i].decode("utf-8").replace("\x1b[0m", "")
            self.informLabel.setText("\n".join(display_info))
            self.status = self.get_status()
            if self.status == "DISCONNECTED":
                self.mainButton.setText("Connect")
                self.comboBox.setVisible(True)
                self.mainButton.clicked.connect(self.connect_to_server)
            else:
                self.mainButton.setText("Disconnect")
                self.mainButton.clicked.connect(self.disconnect_server)
            self.statusbar.showMessage(self.status)

    def show_login_dialog(self) -> None:

        self.log_window.setParent(self)
        self.log_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.log_window.setWindowFlags(QtCore.Qt.Window)
        self.log_window.exec_()    

    def log_in(self) -> None:
        command = pexpect.spawn("windscribe login")
        command.expect("Windscribe Username: ")
        command.sendline(self.log_window.loginLine.text())
        command.expect("Windscribe Password: ")
        command.sendline(self.log_window.passwordLine.text())
        command.expect("Logged In")
        self.mainButton.clicked.disconnect(self.show_login_dialog)
        self.get_account_info()
        self.logoutButton.setVisible(True)

    def get_status(self) -> str:
        message = pexpect.spawn("windscribe status")
        message_to_show = message.read().split(b"\r\n")
        for i in range(len(message_to_show)):
            message_to_show[i] = message_to_show[i].decode("utf-8").replace("\x1b[31m", "").replace("\x1b[0m", "").replace("\x1b[32m", "")
        print(message_to_show)
        return message_to_show[2]

    def connect_to_server(self) -> None:

        if self.comboBox.currentText() == "choose server":
            command = pexpect.spawn("windscribe connect")
        else:
            command = pexpect.spawn(
                f"windscribe connect {servers[self.comboBox.currentText()]}"
            )
        command.expect("Connected to*")
        # 
        self.mainButton.clicked.disconnect()
        self.get_account_info()

    def disconnect_server(self) -> None:

        print("the method has been called")
        command = pexpect.spawn("windscribe disconnect")
        command.expect("Firewall Disabled*")
        self.comboBox.setVisible(False)
        self.mainButton.clicked.disconnect()
        self.get_account_info()

    def log_out(self) -> None:
        self.disconnect_server()
        command = pexpect.spawn("windscribe logout")
        command.expect("Logged Out, Disconnecting*")
        self.comboBox.setVisible(False)
        self.mainButton.clicked.disconnect()
        self.get_account_info()
