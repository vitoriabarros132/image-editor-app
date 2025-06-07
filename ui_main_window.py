################################################################################
## Form generated from reading UI file 'main_windowArJzir.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1150, 600)
        mainWindow.setMinimumSize(QSize(1150, 600))
        mainWindow.setMaximumSize(QSize(1150, 600))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        mainWindow.setFont(font)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.selectButton = QPushButton(self.centralwidget)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setGeometry(QRect(20, 17, 151, 25))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.selectButton.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(375, 400, 311, 23))
        self.label_2.setFont(font1)
        self.equalizationBox = QComboBox(self.centralwidget)
        self.equalizationBox.addItem("")
        self.equalizationBox.addItem("")
        self.equalizationBox.setObjectName(u"equalizationBox")
        self.equalizationBox.setGeometry(QRect(710, 437, 231, 23))
        self.equalizationBox.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(375, 437, 331, 23))
        self.label.setFont(font1)
        self.applyButton = QPushButton(self.centralwidget)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setGeometry(QRect(530, 494, 241, 25))
        self.applyButton.setFont(font1)
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(530, 530, 241, 25))
        self.saveButton.setFont(font1)
        self.filterBox = QComboBox(self.centralwidget)
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.addItem("")
        self.filterBox.setObjectName(u"filterBox")
        self.filterBox.setGeometry(QRect(710, 400, 231, 23))
        self.filterBox.setFont(font1)
        self.imageList = QListView(self.centralwidget)
        self.imageList.setObjectName(u"imageList")
        self.imageList.setGeometry(QRect(20, 56, 150, 400))
        self.imageList.setMinimumSize(QSize(150, 250))
        self.imageList.setMaximumSize(QSize(150, 400))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(830, 66, 300, 300))
        self.groupBox_3.setMinimumSize(QSize(300, 300))
        self.groupBox_3.setMaximumSize(QSize(300, 300))
        self.imgEqualizada = QLabel(self.groupBox_3)
        self.imgEqualizada.setObjectName(u"imgEqualizada")
        self.imgEqualizada.setGeometry(QRect(30, 30, 250, 250))
        self.imgEqualizada.setMinimumSize(QSize(250, 250))
        self.imgEqualizada.setMaximumSize(QSize(250, 250))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(195, 66, 300, 300))
        self.groupBox.setMinimumSize(QSize(300, 300))
        self.groupBox.setMaximumSize(QSize(300, 300))
        self.imgOriginal = QLabel(self.groupBox)
        self.imgOriginal.setObjectName(u"imgOriginal")
        self.imgOriginal.setGeometry(QRect(20, 30, 250, 250))
        self.imgOriginal.setMinimumSize(QSize(250, 250))
        self.imgOriginal.setMaximumSize(QSize(250, 250))
        self.imgOriginal.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(510, 66, 300, 300))
        self.groupBox_2.setMinimumSize(QSize(300, 300))
        self.groupBox_2.setMaximumSize(QSize(300, 300))
        self.imgFiltrada = QLabel(self.groupBox_2)
        self.imgFiltrada.setObjectName(u"imgFiltrada")
        self.imgFiltrada.setGeometry(QRect(20, 30, 250, 250))
        self.imgFiltrada.setMinimumSize(QSize(250, 250))
        self.imgFiltrada.setMaximumSize(QSize(250, 250))
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        self.filterBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Editor de imagens", None))
        self.selectButton.setText(QCoreApplication.translate("mainWindow", u"Selecionar imagens", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Selecione o filtro para remo\u00e7\u00e3o de ru\u00eddo", None))
        self.equalizationBox.setItemText(0, QCoreApplication.translate("mainWindow", u"Equaliza\u00e7\u00e3o de Histograma", None))
        self.equalizationBox.setItemText(1, QCoreApplication.translate("mainWindow", u"Equaliza\u00e7\u00e3o CLAHE", None))

        self.label.setText(QCoreApplication.translate("mainWindow", u"Selecione a t\u00e9cnica para ajuste de contraste", None))
        self.applyButton.setText(QCoreApplication.translate("mainWindow", u"Aplicar configura\u00e7\u00e3o", None))
        self.saveButton.setText(QCoreApplication.translate("mainWindow", u"Salvar Imagens", None))
        self.filterBox.setItemText(0, QCoreApplication.translate("mainWindow", u"Transformada de Wavelet", None))
        self.filterBox.setItemText(1, QCoreApplication.translate("mainWindow", u"Filtro de Wiener", None))
        self.filterBox.setItemText(2, QCoreApplication.translate("mainWindow", u"Filtro de Mediana", None))
        self.filterBox.setItemText(3, QCoreApplication.translate("mainWindow", u"Difus\u00e3o Anisotr\u00f3pica", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("mainWindow", u"Com ajuste de contraste", None))
        self.imgEqualizada.setText(QCoreApplication.translate("mainWindow", u"Equalizada", None))
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"Imagem original", None))
        self.imgOriginal.setText(QCoreApplication.translate("mainWindow", u"Imagem Original", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("mainWindow", u"Com remo\u00e7\u00e3o de ru\u00eddo", None))
        self.imgFiltrada.setText(QCoreApplication.translate("mainWindow", u"Com tratamento", None))
    # retranslateUi


