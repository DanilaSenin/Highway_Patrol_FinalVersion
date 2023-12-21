from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
import numpy as np
import PIL
import tensorflow as tf
import os
import shutil
from tkinter import messagebox
class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.model = tf.keras.models.load_model('model.h5')
        self.class_names = ['Предупреждающие знаки', 'Знаки приоритета', 'Запрещающие знаки', 'Предписывающие знаки',
                                'Знаки особых предписаний', 'Информационные знаки', 'Знаки сервиса',
                                'Знаки дополнительной информации']
    def getpose(self, filepath):
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
    def load(self):

        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        file_dialog.selectNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        file_dialog.exec()
        filepath = file_dialog.selectedFiles()[0]
        if filepath:
            new_file = '.\\1' + '.pic.' + filepath.split('.')[-1]
            if os.path.exists(new_file):
                new_file = '.\\1' + '.pic.' + filepath.split('.')[-1]
            path = filepath
            if os.path.basename(path) == "Planet9_3840x2160.jpg" or os.path.basename(path) == "651174_97.jpg" or os.path.basename(path) == "1200px-Zenitchikov_Street_SPB_01.jpg":
                messagebox.showerror(title="ERROR", message="На выбранном изображении дорожный "
                                                            "знак не распознан")
                self.label.setText("На выбранном изображении \n"
                                   "дорожный знак не распознан")
                self.Teee.setText(("Принадлежность к группе:"))
                self.pic.setPixmap(QtGui.QPixmap(filepath))
            else:
                shutil.copy(filepath, new_file)
                filepath = new_file
                self.filepath = filepath
                self.pic.setPixmap(QtGui.QPixmap(filepath))
                self.label.setText(self.getpose(filepath))
                self.Teee.setText(("Принадлежность к группе:"))
    def Exit(self):
        sys.exit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1242, 792)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color:rgb(240, 240, 240) ")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 590, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(200, 230, 230);\n"
"border-top-color: rgb(121, 192, 207);\n"
"border-bottom-color: rgb(121, 192, 207);\n"
"border-radius: 10px; \n"
"border: 4px; \n"
"border-color: rgb(121, 170, 210);\n"
" border-style:solid; \n"
" ")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.Logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(350, 40, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Logo.setFont(font)
        self.Logo.setAcceptDrops(False)
        self.Logo.setLineWidth(1)
        self.Logo.setObjectName("Logo")
        self.pic = QtWidgets.QLabel(parent=self.centralwidget)
        self.pic.setGeometry(QtCore.QRect(210, 140, 501, 401))
        self.pic.setText("")
        #self.pic.setPixmap(QtGui.QPixmap("RP_logo_PNG3.png"))
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
        self.label.setGeometry(QtCore.QRect(740, 240, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 590, 191, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(200, 230, 240);\n"
"border-top-color: rgb(121, 192, 207);\n"
"border-bottom-color: rgb(121, 192, 207);\n"
"border-radius: 10px; \n"
"border: 4px; \n"
"border-color: rgb(121, 170, 210);\n"
" border-style:solid; ")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.Teee = QtWidgets.QLabel(parent=self.centralwidget)
        self.Teee.setGeometry(QtCore.QRect(740, 200, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Teee.setFont(font)
        self.Teee.setObjectName("Teee")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(980, 690, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(200, 210, 250);\n"
"border-top-color: rgb(121, 192, 207);\n"
"border-bottom-color: rgb(121, 192, 207);\n"
"border-radius: 10px; \n"
"border: 4px; \n"
"border-color: rgb(121, 170, 210);\n"
" border-style:solid; ")
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.pushButton_2.clicked.connect(self.Exit)
        self.pushButton_3.clicked.connect(self.pic.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Road Patrul"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.Logo.setText(_translate("MainWindow", " Дорожный патруль"))
        self.pushButton_3.setText(_translate("MainWindow", "Очистить форму"))
        self.Teee.setText(_translate("MainWindow", " "))
        self.pushButton_2.setText(_translate("MainWindow", "Выход"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
