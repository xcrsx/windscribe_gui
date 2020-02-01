# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 450)
        self.actionAccountStatus = QAction(MainWindow)
        self.actionAccountStatus.setObjectName(u"actionAccountStatus")
        self.actionShowLoginDialog = QAction(MainWindow)
        self.actionShowLoginDialog.setObjectName(u"actionShowLoginDialog")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionDisconnect = QAction(MainWindow)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.informLabel = QLabel(self.centralwidget)
        self.informLabel.setObjectName(u"informLabel")
        self.informLabel.setGeometry(QRect(10, 5, 380, 87))
        self.informLabel.setStyleSheet(u"")
        self.informLabel.setFrameShape(QFrame.StyledPanel)
        self.informLabel.setFrameShadow(QFrame.Raised)
        self.informLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.accountStatusButton = QPushButton(self.centralwidget)
        self.accountStatusButton.setObjectName(u"accountStatusButton")
        self.accountStatusButton.setGeometry(QRect(10, 100, 380, 31))
        self.mainButton = QPushButton(self.centralwidget)
        self.mainButton.setObjectName(u"mainButton")
        self.mainButton.setGeometry(QRect(10, 140, 381, 50))
        self.mainButton.setAutoFillBackground(True)
        self.mainButton.setStyleSheet(u"")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(270, 200, 120, 41))
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(10, 200, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.accountStatusButton.clicked.connect(self.actionAccountStatus.trigger)
        self.mainButton.clicked.connect(self.actionShowLoginDialog.trigger)
        self.logoutButton.clicked.connect(self.actionLogout.trigger)
        self.mainButton.clicked.connect(self.actionConnect.trigger)
        self.mainButton.clicked.connect(self.actionDisconnect.trigger)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Windscribe VPN", None))
        self.actionAccountStatus.setText(QCoreApplication.translate("MainWindow", u"checkStat", None))
        self.actionShowLoginDialog.setText(QCoreApplication.translate("MainWindow", u"conDiscon", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.actionDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.informLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.accountStatusButton.setText(QCoreApplication.translate("MainWindow", u"Check account status", None))
        self.mainButton.setText("")
        self.comboBox.setCurrentText("")
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
    # retranslateUi

