
from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
import numpy as np
import PIL
import tensorflow as tf
import sys
import cv2
import os
import glob
import shutil

Form, Window = uic.loadUiType("untitled.ui")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.model = tf.keras.models.load_model('.\\model.h5')
        self.class_names = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.initUI()

    def getpose(self, filepath):
        res = 50
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
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filepath, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)
        if filepath:
            original_fp = filepath
            new_file = '.\\pic.' + filepath.split('.')[-1]
            if os.path.exists(new_file):
                os.remove(new_file)
            shutil.copy(filepath, new_file)
            filepath = new_file
            self.filepath = filepath
            self.l_path.setText(original_fp)
            self.l_path.adjustSize()
            pathw = self.l_path.width()
            pathh = self.l_path.height()
            self.l_path.setGeometry(220, 40, pathw, pathh)
            self.pic.setPixmap(QPixmap(filepath))
            im = np.asarray(PIL.Image.open(filepath))
            resx = min(im.shape[0], self.winw - 50)
            resy = min(im.shape[1], self.winh - 200)
            self.pic.setGeometry(QtCore.QRect((self.winw - resx) // 2, 100, resx, resy))
            self.l_pose.setText(self.getpose(filepath))
            self.l_pose.adjustSize()
            posew = self.l_pose.width()
            self.l_pose.setGeometry((self.winw - posew) // 2, 100 + resy + 30, posew, 50)

        pass

    def initUI(self):
        self.winw = 600
        self.winh = 600
        self.setGeometry(100, 100, self.winw, self.winh)
        self.setWindowTitle("Road signs classifier")

        self.b_load = QtWidgets.QPushButton(self)
        self.b_load.setText("Выбрать файл")
        b_font = self.font()
        b_font.setPointSize(12)
        self.b_load.setFont(b_font)
        self.b_load.setGeometry(40, 40, 150, 30)
        self.b_load.clicked.connect(self.load)

        self.l_path = QtWidgets.QLabel(self)
        l_font = self.font()
        l_font.setPointSize(10)
        self.l_path.setFont(l_font)
        self.l_path.setGeometry(220, 10, 300, 100)
        self.l_path.setWordWrap(True)

        self.pic = QtWidgets.QLabel(self)
        self.pic.setGeometry(QtCore.QRect(40, 100, 200, 200))
        self.pic.setText("")
        self.pic.setScaledContents(True)
        self.pic.setObjectName("photo")

        self.l_pose = QtWidgets.QLabel(self)
        l_font = self.font()
        l_font.setPointSize(14)
        self.l_pose.setFont(l_font)
        self.l_pose.setGeometry(220, self.winh - 50, 300, 100)


def window():
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec()


window()