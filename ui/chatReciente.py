# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatReciente.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
class Ui_RecentChat(object):
    def setupUi(self, RecentChat):
        if not RecentChat.objectName():
            RecentChat.setObjectName(u"RecentChat")
        RecentChat.setMinimumSize(QSize(280, 70))
        self.horizontalLayout = QHBoxLayout(RecentChat)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.profilePic = QLabel(RecentChat)
        self.profilePic.setObjectName(u"profilePic")
        self.profilePic.setMinimumSize(QSize(50, 50))
        self.profilePic.setMaximumSize(QSize(50, 50))
        self.profilePic.setStyleSheet("""
            QLabel#profilePic {
                background-color: transparent;
                border: none;
                padding: 0;
            }
        """)
        icon = QPixmap("res/cuenta.svg")
        scaled_icon = icon.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio,
                                  Qt.TransformationMode.SmoothTransformation)
        self.profilePic.setPixmap(scaled_icon)

        self.horizontalLayout.addWidget(self.profilePic)

        self.infoLayout = QVBoxLayout()
        self.infoLayout.setObjectName(u"infoLayout")
        self.ipLabel = QLabel(RecentChat)
        self.ipLabel.setObjectName(u"ipLabel")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.ipLabel.setFont(font)

        self.infoLayout.addWidget(self.ipLabel)

        self.lastConnection = QLabel(RecentChat)
        self.lastConnection.setObjectName(u"lastConnection")
        self.lastConnection.setStyleSheet(u"color: #666;")

        self.infoLayout.addWidget(self.lastConnection)


        self.horizontalLayout.addLayout(self.infoLayout)

        self.connectButton = QPushButton(RecentChat)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setMaximumSize(QSize(60, 25))
        self.connectButton.setStyleSheet(u"background-color: #2196F3; color: white;")

        self.horizontalLayout.addWidget(self.connectButton)


        self.retranslateUi(RecentChat)

        QMetaObject.connectSlotsByName(RecentChat)
    # setupUi

    def retranslateUi(self, RecentChat):
        self.ipLabel.setText(QCoreApplication.translate("RecentChat", u"IP: 192.168.1.1:8080", None))
        self.lastConnection.setText(QCoreApplication.translate("RecentChat", u"\u00daltima conexi\u00f3n: Hace 2 horas", None))
        self.connectButton.setText(QCoreApplication.translate("RecentChat", u"Conectar", None))
        pass
    # retranslateUi

