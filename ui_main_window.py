# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowWbFFUA.ui'
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
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 100, 531, 382))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.imageList = QListWidget(self.layoutWidget)
        self.imageList.setObjectName(u"imageList")

        self.gridLayout.addWidget(self.imageList, 1, 0, 1, 2)

        self.imagePreview = QLabel(self.layoutWidget)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setPixmap(QPixmap(u"../../../Downloads/d03bf668ed91521de96b6e47dab31ac1.jpg"))

        self.gridLayout.addWidget(self.imagePreview, 1, 2, 1, 1)

        self.selectImagesButton = QPushButton(self.layoutWidget)
        self.selectImagesButton.setObjectName(u"selectImagesButton")

        self.gridLayout.addWidget(self.selectImagesButton, 0, 0, 1, 2)

        self.saveButton = QPushButton(self.layoutWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout.addWidget(self.saveButton, 2, 2, 1, 1)

        self.applyFilterButton = QPushButton(self.layoutWidget)
        self.applyFilterButton.setObjectName(u"applyFilterButton")

        self.gridLayout.addWidget(self.applyFilterButton, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imagePreview.setText("")
        self.selectImagesButton.setText(QCoreApplication.translate("MainWindow", u"Selecionar imagens", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Salvar Imagens", None))
        self.applyFilterButton.setText(QCoreApplication.translate("MainWindow", u"Aplicar filtro", None))
    # retranslateUi

