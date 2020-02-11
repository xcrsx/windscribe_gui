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
        Dialog.resize(382, 219)
        Dialog.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"	background-color: darkgray;\n"
"}")
        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(180, 150, 89, 25))
        font = QFont()
        font.setFamily(u"Perfect DOS VGA 437")
        font.setBold(True)
        font.setWeight(75);
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet(u"QPushButton{\n"
"background-color: #bbbbbb;\n"
"border: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: #666666;\n"
" }\n"
"QPushButton:pressed {\n"
"border-style:solid;\n"
"border-width:3px;\n"
"}")
        self.cancelButton.setAutoDefault(False)
        self.cancelButton.setFlat(True)
        self.logInButton = QPushButton(Dialog)
        self.logInButton.setObjectName(u"logInButton")
        self.logInButton.setGeometry(QRect(280, 150, 89, 25))
        self.logInButton.setFont(font)
        self.logInButton.setStyleSheet(u"QPushButton{\n"
"background-color: #bbbbbb;\n"
"border: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: #666666;\n"
" }\n"
"QPushButton:pressed {\n"
"border-style:solid;\n"
"border-width:3px;\n"
"}")
        self.logInButton.setFlat(True)
        self.loginField = QLabel(Dialog)
        self.loginField.setObjectName(u"loginField")
        self.loginField.setGeometry(QRect(20, 60, 81, 31))
        font1 = QFont()
        font1.setFamily(u"Perfect DOS VGA 437")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75);
        self.loginField.setFont(font1)
        self.loginField.setStyleSheet(u"color: #defe54;")
        self.passwordField = QLabel(Dialog)
        self.passwordField.setObjectName(u"passwordField")
        self.passwordField.setGeometry(QRect(20, 100, 81, 31))
        self.passwordField.setFont(font1)
        self.passwordField.setStyleSheet(u"color: #defe54;")
        self.loginLine = QLineEdit(Dialog)
        self.loginLine.setObjectName(u"loginLine")
        self.loginLine.setGeometry(QRect(110, 60, 261, 30))
        self.loginLine.setFont(font)
        self.loginLine.setStyleSheet(u"")
        self.passwordLine = QLineEdit(Dialog)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setGeometry(QRect(110, 100, 261, 30))
        self.passwordLine.setFont(font)
        self.dialogText = QLabel(Dialog)
        self.dialogText.setObjectName(u"dialogText")
        self.dialogText.setGeometry(QRect(0, 6, 381, 41))
        font2 = QFont()
        font2.setFamily(u"Perfect DOS VGA 437")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75);
        self.dialogText.setFont(font2)
        self.dialogText.setStyleSheet(u"color: #defe54;")
        self.dialogText.setAlignment(Qt.AlignCenter)
        self.sourceLabel = QLabel(Dialog)
        self.sourceLabel.setObjectName(u"sourceLabel")
        self.sourceLabel.setGeometry(QRect(0, 190, 391, 31))
        self.sourceLabel.setFont(font)
        self.sourceLabel.setStyleSheet(u"color: #defe54;\n"
"background-color: #bbbbbb;\n"
"border: 1px;")
        self.sourceLabel.setAlignment(Qt.AlignCenter)

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
        self.sourceLabel.setText("")
    # retranslateUi

