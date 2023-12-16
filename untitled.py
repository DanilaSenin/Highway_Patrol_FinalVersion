# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QFont, QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
import numpy as np
import PIL
import tensorflow as tf
import sys
import cv2
import os
import glob
import shutil


class Ui_MainWindow(object):
    def __init__(self):
        try:
            super(Ui_MainWindow, self).__init__()
            self.model = tf.keras.models.load_model('model.h5')
            self.class_names = ['Предупреждающие знаки', 'Знаки приоритета', 'Запрещающие знаки', 'Предписывающие знаки',
                                'Знаки особых предписаний', 'Информационные знаки', 'Знаки сервиса',
                                'Знаки дополнительной информации']
            # self.setupUi(MainWindow)
        except Exception as e:
            print(f"Произошла ошибка: {e}")


    def getpose(self, filepath):
        try:
            res = 80
            im = PIL.Image.open(filepath)
            im = im.convert('RGB')
            im = im.resize((res, res), PIL.Image.Resampling.LANCZOS)
            im = np.asarray(im)
            im = im / 255.
            im = im.reshape((1, res, res, 3))
            pred = self.model.predict(im, verbose=0)
            pred_class = self.class_names[np.argmax(pred)]
            pred_class = pred_class.replace('_', ' ')
            os.remove(filepath)
            return pred_class

        except Exception as e:
            print(f"Произошла ошибка: {e}")


    def load(self):
        try:
            file_dialog = QFileDialog()
            # Установка фильтра для выбора только файлов изображений
            file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
            file_dialog.selectNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
            # Открытие диалогового окна
            file_dialog.exec()
            # Получение выбранного пути к файлу
            filepath = file_dialog.selectedFiles()[0]
            n = 0
            if filepath:
                original_fp = filepath
                n += 1
                new_file = '.\\1' + str(n) + '.pic.' + filepath.split('.')[-1]
                if os.path.exists(new_file):
                    n += 1
                    new_file = '.\\1' + str(n) + '.pic.' + filepath.split('.')[-1]
                shutil.copy(filepath, new_file)
                filepath = new_file
                self.filepath = filepath
                #self.navs.setText((filepath))
                self.pic.setPixmap(QtGui.QPixmap(filepath))
                #self.pic.setPixmap(QtGui.QPixmap(filepath))
                self.label.setText(self.getpose(filepath))
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1242, 792)
        MainWindow.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 590, 181, 81))
        self.pushButton.setObjectName("pushButton")
        self.Logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(370, 40, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Logo.setFont(font)
        self.Logo.setAcceptDrops(False)
        self.Logo.setLineWidth(1)
        self.Logo.setObjectName("Logo")
        self.pic = QtWidgets.QLabel(parent=self.centralwidget)
        self.pic.setGeometry(QtCore.QRect(210, 140, 501, 401))
        self.pic.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"color: rgb(240, 240, 240);")
        self.pic.setText("")
        #self.pic.setPixmap(QtGui.QPixmap("1_7000.png"))
        self.pic.setScaledContents(True)
        self.pic.setObjectName("pic")
        self.eticetka = QtWidgets.QLabel(parent=self.centralwidget)
        self.eticetka.setGeometry(QtCore.QRect(210, 40, 91, 81))
        self.eticetka.setStyleSheet("")
        self.eticetka.setText("")
        self.eticetka.setPixmap(QtGui.QPixmap("RP_logo_PNG3.png"))
        self.eticetka.setScaledContents(True)
        self.eticetka.setObjectName("eticetka")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(790, 250, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 590, 181, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.Teee = QtWidgets.QLabel(parent=self.centralwidget)
        self.Teee.setGeometry(QtCore.QRect(790, 200, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Teee.setFont(font)
        self.Teee.setObjectName("Teee")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1242, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.load) # type: ignore
        self.pushButton_3.clicked.connect(self.pic.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тест приложения на Python"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.Logo.setText(_translate("MainWindow", "Дорожный патруль"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", "Очистить форму"))
        self.Teee.setText(_translate("MainWindow", "Принадлоежность к группе: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
