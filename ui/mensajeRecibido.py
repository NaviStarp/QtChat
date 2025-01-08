# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mensajeRecibido.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ReceivedMessage(object):
    def setupUi(self, ReceivedMessage):
        if not ReceivedMessage.objectName():
            ReceivedMessage.setObjectName(u"ReceivedMessage")
        ReceivedMessage.resize(300, 80)
        ReceivedMessage.setMinimumSize(QSize(300, 80))
        self.horizontalLayout = QHBoxLayout(ReceivedMessage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.profilePic = QLabel(ReceivedMessage)
        self.profilePic.setObjectName(u"profilePic")
        self.profilePic.setMinimumSize(QSize(40, 40))
        self.profilePic.setMaximumSize(QSize(40, 40))
        self.profilePic.setStyleSheet(u"border-radius: 20px; background-color: lightgray;")

        self.horizontalLayout.addWidget(self.profilePic)

        self.messageLayout = QVBoxLayout()
        self.messageLayout.setObjectName(u"messageLayout")
        self.messageContent = QLabel(ReceivedMessage)
        self.messageContent.setObjectName(u"messageContent")
        self.messageContent.setStyleSheet(u"background-color: #e8e8e8; border-radius: 10px; padding: 8px;")
        self.messageContent.setWordWrap(True)

        self.messageLayout.addWidget(self.messageContent)

        self.timeLabel = QLabel(ReceivedMessage)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setStyleSheet(u"color: gray; font-size: 10px;")

        self.messageLayout.addWidget(self.timeLabel)


        self.horizontalLayout.addLayout(self.messageLayout)

        self.rightSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.rightSpacer)


        self.retranslateUi(ReceivedMessage)

        QMetaObject.connectSlotsByName(ReceivedMessage)
    # setupUi

    def retranslateUi(self, ReceivedMessage):
        self.messageContent.setText(QCoreApplication.translate("ReceivedMessage", u"Mensaje recibido", None))
        self.timeLabel.setText(QCoreApplication.translate("ReceivedMessage", u"12:30", None))
        pass
    # retranslateUi

