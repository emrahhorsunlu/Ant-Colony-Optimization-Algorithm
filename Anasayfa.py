# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

"""
@author: emrah
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 328)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Girdiler = QtWidgets.QLineEdit(self.centralwidget)
        self.Girdiler.setGeometry(QtCore.QRect(190, 40, 181, 20))
        self.Girdiler.setObjectName("Girdiler")
        self.Agirlik = QtWidgets.QLineEdit(self.centralwidget)
        self.Agirlik.setGeometry(QtCore.QRect(190, 70, 181, 20))
        self.Agirlik.setObjectName("Agirlik")
        self.Populasyon = QtWidgets.QLineEdit(self.centralwidget)
        self.Populasyon.setGeometry(QtCore.QRect(190, 100, 181, 20))
        self.Populasyon.setObjectName("Populasyon")
        self.MinAralik = QtWidgets.QLineEdit(self.centralwidget)
        self.MinAralik.setGeometry(QtCore.QRect(190, 130, 181, 20))
        self.MinAralik.setObjectName("MinAralik")
        self.MaxAralik = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxAralik.setGeometry(QtCore.QRect(190, 160, 181, 20))
        self.MaxAralik.setObjectName("MaxAralik")
        self.Iterasyon = QtWidgets.QLineEdit(self.centralwidget)
        self.Iterasyon.setGeometry(QtCore.QRect(190, 190, 181, 20))
        self.Iterasyon.setObjectName("Iterasyon")
        self.BireSayisi = QtWidgets.QLineEdit(self.centralwidget)
        self.BireSayisi.setGeometry(QtCore.QRect(190, 220, 181, 20))
        self.BireSayisi.setObjectName("BireSayisi")
        self.GirdilerText = QtWidgets.QLabel(self.centralwidget)
        self.GirdilerText.setGeometry(QtCore.QRect(150, 40, 47, 13))
        self.GirdilerText.setObjectName("GirdilerText")
        self.AgirlikText = QtWidgets.QLabel(self.centralwidget)
        self.AgirlikText.setGeometry(QtCore.QRect(150, 70, 47, 13))
        self.AgirlikText.setObjectName("AgirlikText")
        self.PopulasyonText = QtWidgets.QLabel(self.centralwidget)
        self.PopulasyonText.setGeometry(QtCore.QRect(30, 100, 161, 20))
        self.PopulasyonText.setObjectName("PopulasyonText")
        self.MinAralikText = QtWidgets.QLabel(self.centralwidget)
        self.MinAralikText.setGeometry(QtCore.QRect(110, 130, 81, 20))
        self.MinAralikText.setObjectName("MinAralikText")
        self.MaxAralikText = QtWidgets.QLabel(self.centralwidget)
        self.MaxAralikText.setGeometry(QtCore.QRect(106, 160, 81, 20))
        self.MaxAralikText.setObjectName("MaxAralikText")
        self.IterasyonText = QtWidgets.QLabel(self.centralwidget)
        self.IterasyonText.setGeometry(QtCore.QRect(140, 190, 47, 13))
        self.IterasyonText.setObjectName("IterasyonText")
        self.BireySayisiText = QtWidgets.QLabel(self.centralwidget)
        self.BireySayisiText.setGeometry(QtCore.QRect(130, 220, 61, 20))
        self.BireySayisiText.setObjectName("BireySayisiText")
        self.HesaplaButon = QtWidgets.QPushButton(self.centralwidget)
        self.HesaplaButon.setGeometry(QtCore.QRect(190, 250, 181, 31))
        self.HesaplaButon.setObjectName("HesaplaButon")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(430, 30, 511, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GirdilerText.setText(_translate("MainWindow", "Girdiler"))
        self.AgirlikText.setText(_translate("MainWindow", "Ağırlık"))
        self.PopulasyonText.setText(_translate("MainWindow", "Popülasyon Başına Çözüm Sayısı"))
        self.MinAralikText.setText(_translate("MainWindow", "Minimum Aralık"))
        self.MaxAralikText.setText(_translate("MainWindow", "Maximum Aralık"))
        self.IterasyonText.setText(_translate("MainWindow", "İterasyon"))
        self.BireySayisiText.setText(_translate("MainWindow", "Birey sayisi"))
        self.HesaplaButon.setText(_translate("MainWindow", "Hesapla"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))