# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PaginaPrincipal.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1099, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FramePrincipal = QStackedWidget(self.centralwidget)
        self.FramePrincipal.setObjectName(u"FramePrincipal")
        self.FramePrincipal.setEnabled(True)
        self.PaginaPrincipal = QWidget()
        self.PaginaPrincipal.setObjectName(u"PaginaPrincipal")
        self.verticalLayout_4 = QVBoxLayout(self.PaginaPrincipal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.PaginaPrincipal)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.pushButton = QPushButton(self.PaginaPrincipal)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout.setStretch(2, 15)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.PaginaPrincipal)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.IPEdit = QTextEdit(self.PaginaPrincipal)
        self.IPEdit.setObjectName(u"IPEdit")
        self.IPEdit.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_6.addWidget(self.IPEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.PaginaPrincipal)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.PuertoEdit = QTextEdit(self.PaginaPrincipal)
        self.PuertoEdit.setObjectName(u"PuertoEdit")
        self.PuertoEdit.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_5.addWidget(self.PuertoEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.PaginaPrincipal)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.PaginaPrincipal)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.listWidget = QListWidget(self.PaginaPrincipal)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_8.addWidget(self.listWidget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.PaginaPrincipal)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.listWidget_2 = QListWidget(self.PaginaPrincipal)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_7.addWidget(self.listWidget_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_4.setStretch(3, 5)
        self.FramePrincipal.addWidget(self.PaginaPrincipal)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_10 = QVBoxLayout(self.page_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.VolverDeAjustes = QPushButton(self.page_2)
        self.VolverDeAjustes.setObjectName(u"VolverDeAjustes")

        self.horizontalLayout_7.addWidget(self.VolverDeAjustes)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.PuertoPersonalizado = QLineEdit(self.page_2)
        self.PuertoPersonalizado.setObjectName(u"PuertoPersonalizado")

        self.verticalLayout_9.addWidget(self.PuertoPersonalizado)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_9.addWidget(self.pushButton_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 8)
        self.FramePrincipal.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.FramePrincipal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.FramePrincipal.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"QTChat", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n ip", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Puerto", None))
        self.PuertoEdit.setMarkdown("")
        self.PuertoEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"12345", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Entrantes", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Recientes", None))
        self.VolverDeAjustes.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Puerto personalizado", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Borrar todos los datos", None))
    # retranslateUi

