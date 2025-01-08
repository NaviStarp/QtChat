# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mensajeEnviado.ui'
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

class Ui_SentMessage(object):
    def setupUi(self, SentMessage):
        if not SentMessage.objectName():
            SentMessage.setObjectName(u"SentMessage")
        SentMessage.resize(300, 80)
        SentMessage.setMinimumSize(QSize(300, 80))
        self.horizontalLayout = QHBoxLayout(SentMessage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.leftSpacer)

        self.messageLayout = QVBoxLayout()
        self.messageLayout.setObjectName(u"messageLayout")
        self.messageContent = QLabel(SentMessage)
        self.messageContent.setObjectName(u"messageContent")
        self.messageContent.setStyleSheet(u"background-color: #DCF8C6; border-radius: 10px; padding: 8px;")
        self.messageContent.setWordWrap(True)
        self.messageContent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.messageLayout.addWidget(self.messageContent)

        self.timeLabel = QLabel(SentMessage)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setStyleSheet(u"color: gray; font-size: 10px;")
        self.timeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.messageLayout.addWidget(self.timeLabel)


        self.horizontalLayout.addLayout(self.messageLayout)


        self.retranslateUi(SentMessage)

        QMetaObject.connectSlotsByName(SentMessage)
    # setupUi

    def retranslateUi(self, SentMessage):
        self.messageContent.setText(QCoreApplication.translate("SentMessage", u"Mensaje enviado", None))
        self.timeLabel.setText(QCoreApplication.translate("SentMessage", u"12:30", None))
        pass
    # retranslateUi

