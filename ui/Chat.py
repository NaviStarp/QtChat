# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Chat.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
                               QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
                               QSpacerItem, QTextEdit, QVBoxLayout, QWidget, QLineEdit)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Chat_ip = QLabel(self.centralwidget)
        self.Chat_ip.setObjectName(u"Chat_ip")

        self.horizontalLayout_2.addWidget(self.Chat_ip)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.ListaMensajes = QListWidget(self.centralwidget)
        self.ListaMensajes.setObjectName(u"ListaMensajes")
        self.ListaMensajes.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.ListaMensajes)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.EnviarTexto = QLineEdit(self.centralwidget)
        self.EnviarTexto.setObjectName(u"EnviarTexto")
        self.EnviarTexto.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout.addWidget(self.EnviarTexto)

        self.EnviarBoton = QPushButton(self.centralwidget)
        self.EnviarBoton.setObjectName(u"EnviarBoton")
        self.EnviarBoton.setMinimumSize(QSize(0, 35))

        self.horizontalLayout.addWidget(self.EnviarBoton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 11)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Chat_ip.setText(QCoreApplication.translate("MainWindow", u"Chat con ip", None))
        self.EnviarBoton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

