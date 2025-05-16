# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_histotsuNpSRJb.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMaximumSize(QSize(500, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout.addWidget(self.saveButton, 3, 1, 1, 1)

        self.applyHistButton = QPushButton(self.centralwidget)
        self.applyHistButton.setObjectName(u"applyHistButton")

        self.gridLayout.addWidget(self.applyHistButton, 2, 0, 1, 1)

        self.imageList = QListWidget(self.centralwidget)
        self.imageList.setObjectName(u"imageList")

        self.gridLayout.addWidget(self.imageList, 1, 0, 1, 1)

        self.applyCLAHEButton = QPushButton(self.centralwidget)
        self.applyCLAHEButton.setObjectName(u"applyCLAHEButton")

        self.gridLayout.addWidget(self.applyCLAHEButton, 3, 0, 1, 1)

        self.imagePreview = QLabel(self.centralwidget)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setMaximumSize(QSize(500, 500))
        self.imagePreview.setPixmap(QPixmap(u"../../../Downloads/d03bf668ed91521de96b6e47dab31ac1.jpg"))

        self.gridLayout.addWidget(self.imagePreview, 1, 1, 1, 1)

        self.selectImagesButton = QPushButton(self.centralwidget)
        self.selectImagesButton.setObjectName(u"selectImagesButton")

        self.gridLayout.addWidget(self.selectImagesButton, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Salvar Imagens", None))
        self.applyHistButton.setText(QCoreApplication.translate("MainWindow", u"Equalizar histograma", None))
        self.applyCLAHEButton.setText(QCoreApplication.translate("MainWindow", u"Aplicar CLAHE", None))
        self.imagePreview.setText("")
        self.selectImagesButton.setText(QCoreApplication.translate("MainWindow", u"Selecionar imagens", None))
    # retranslateUi

