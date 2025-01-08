# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PeticionEntrante.ui'
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
class Ui_IncomingRequest(object):
    def setupUi(self, IncomingRequest):
        if not IncomingRequest.objectName():
            IncomingRequest.setObjectName(u"IncomingRequest")
        IncomingRequest.setMinimumSize(QSize(280, 70))
        self.horizontalLayout = QHBoxLayout(IncomingRequest)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.profilePic = QLabel(IncomingRequest)
        self.profilePic.setObjectName(u"profilePic")
        self.profilePic.setMinimumSize(QSize(40, 40))
        self.profilePic.setStyleSheet(u"border-radius: 20px; background-color: #e0e0e0;")

        self.horizontalLayout.addWidget(self.profilePic)

        self.infoLayout = QVBoxLayout()
        self.infoLayout.setObjectName(u"infoLayout")
        self.ipLabel = QLabel(IncomingRequest)
        self.ipLabel.setObjectName(u"ipLabel")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.ipLabel.setFont(font)

        self.infoLayout.addWidget(self.ipLabel)

        self.requestStatus = QLabel(IncomingRequest)
        self.requestStatus.setObjectName(u"requestStatus")
        self.requestStatus.setStyleSheet(u"color: #666;")

        self.infoLayout.addWidget(self.requestStatus)


        self.horizontalLayout.addLayout(self.infoLayout)

        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.acceptButton = QPushButton(IncomingRequest)
        self.acceptButton.setObjectName(u"acceptButton")
        self.acceptButton.setMaximumSize(QSize(60, 25))
        self.acceptButton.setStyleSheet(u"background-color: #4CAF50; color: white;")

        self.buttonLayout.addWidget(self.acceptButton)

        self.rejectButton = QPushButton(IncomingRequest)
        self.rejectButton.setObjectName(u"rejectButton")
        self.rejectButton.setMaximumSize(QSize(60, 25))
        self.rejectButton.setStyleSheet(u"background-color: #f44336; color: white;")

        self.buttonLayout.addWidget(self.rejectButton)


        self.horizontalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(IncomingRequest)

        QMetaObject.connectSlotsByName(IncomingRequest)
    # setupUi

    def retranslateUi(self, IncomingRequest):
        self.ipLabel.setText(QCoreApplication.translate("IncomingRequest", u"IP: 192.168.1.1:8080", None))
        self.requestStatus.setText(QCoreApplication.translate("IncomingRequest", u"Solicitud de chat pendiente...", None))
        self.acceptButton.setText(QCoreApplication.translate("IncomingRequest", u"\u2713", None))
        self.rejectButton.setText(QCoreApplication.translate("IncomingRequest", u"\u2715", None))
        pass
    # retranslateUi

