# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_newDOLzoa.ui'
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
        self.imageList = QListWidget(self.centralwidget)
        self.imageList.setObjectName(u"imageList")

        self.gridLayout.addWidget(self.imageList, 1, 0, 1, 1)

        self.imagePreview = QLabel(self.centralwidget)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setMaximumSize(QSize(500, 500))
        self.imagePreview.setPixmap(QPixmap(u"../../../Downloads/d03bf668ed91521de96b6e47dab31ac1.jpg"))

        self.gridLayout.addWidget(self.imagePreview, 1, 1, 1, 1)

        self.selectImagesButton = QPushButton(self.centralwidget)
        self.selectImagesButton.setObjectName(u"selectImagesButton")

        self.gridLayout.addWidget(self.selectImagesButton, 0, 0, 1, 1)

        self.applyWaveletButton = QPushButton(self.centralwidget)
        self.applyWaveletButton.setObjectName(u"applyWaveletButton")

        self.gridLayout.addWidget(self.applyWaveletButton, 2, 0, 1, 1)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout.addWidget(self.saveButton, 3, 1, 1, 1)

        self.applyWienerButton = QPushButton(self.centralwidget)
        self.applyWienerButton.setObjectName(u"applyWienerButton")

        self.gridLayout.addWidget(self.applyWienerButton, 3, 0, 1, 1)

        self.applyMedianButton = QPushButton(self.centralwidget)
        self.applyMedianButton.setObjectName(u"applyMedianButton")

        self.gridLayout.addWidget(self.applyMedianButton, 4, 0, 1, 1)

        self.labelPSNR = QLabel(self.centralwidget)
        self.labelPSNR.setObjectName(u"labelPSNR")
        font = QFont()
        font.setPointSize(12)
        self.labelPSNR.setFont(font)

        self.gridLayout.addWidget(self.labelPSNR, 5, 0, 1, 1)


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
        self.imagePreview.setText("")
        self.selectImagesButton.setText(QCoreApplication.translate("MainWindow", u"Selecionar imagens", None))
        self.applyWaveletButton.setText(QCoreApplication.translate("MainWindow", u"Aplicar filtro - WAVELET", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Salvar Imagens", None))
        self.applyWienerButton.setText(QCoreApplication.translate("MainWindow", u"Aplicar filtro - WIENER", None))
        self.applyMedianButton.setText(QCoreApplication.translate("MainWindow", u"Aplicar filtro - MEDIAN", None))
        self.labelPSNR.setText(QCoreApplication.translate("MainWindow", u"PSNR = XX.XX", None))
    # retranslateUi

