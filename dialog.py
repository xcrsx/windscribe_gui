# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(385, 203)
        Dialog.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: azure;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(180, 150, 89, 25))
        self.cancelButton.setAutoDefault(False)
        self.logInButton = QPushButton(Dialog)
        self.logInButton.setObjectName(u"logInButton")
        self.logInButton.setGeometry(QRect(280, 150, 89, 25))
        self.loginField = QLabel(Dialog)
        self.loginField.setObjectName(u"loginField")
        self.loginField.setGeometry(QRect(20, 60, 81, 31))
        font = QFont()
        font.setPointSize(13)
        self.loginField.setFont(font)
        self.passwordField = QLabel(Dialog)
        self.passwordField.setObjectName(u"passwordField")
        self.passwordField.setGeometry(QRect(20, 100, 81, 31))
        self.passwordField.setFont(font)
        self.loginLine = QLineEdit(Dialog)
        self.loginLine.setObjectName(u"loginLine")
        self.loginLine.setGeometry(QRect(110, 60, 261, 30))
        self.loginLine.setStyleSheet(u"")
        self.passwordLine = QLineEdit(Dialog)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setGeometry(QRect(110, 100, 261, 30))
        self.dialogText = QLabel(Dialog)
        self.dialogText.setObjectName(u"dialogText")
        self.dialogText.setGeometry(QRect(0, 6, 381, 41))
        font1 = QFont()
        font1.setPointSize(15)
        self.dialogText.setFont(font1)
        self.dialogText.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)
        self.logInButton.clicked.connect(Dialog.accept)
        self.cancelButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.logInButton.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.loginField.setText(QCoreApplication.translate("Dialog", u"Login:", None))
        self.passwordField.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.dialogText.setText(QCoreApplication.translate("Dialog", u"Login in your account", None))
    # retranslateUi

