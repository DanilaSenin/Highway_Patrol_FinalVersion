from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("untitled.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()

# #
# # ###############################################################
#
# from PyQt6 import QtWidgets, QtCore, QtGui
# from PyQt6.QtGui import QFont, QPixmap, QImage
# from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
# import numpy as np
# import PIL
# import tensorflow as tf
# import sys
# import cv2
# import os
# import glob
# import shutil
#
#
# class Ui_MainWindow(object):
#     def __init__(self):
#         try:
#             super(Ui_MainWindow, self).__init__()
#             self.model = tf.keras.models.load_model('model.h5')
#             self.class_names = ['Предупреждающие знаки', 'Знаки приоритета', 'Запрещающие знаки', 'Предписывающие знаки',
#                                 'Знаки особых предписаний', 'Информационные знаки', 'Знаки сервиса',
#                                 'Знаки дополнительной информации']
#         except Exception as e:
#             print(f"Произошла ошибка: {e}")
#     def getpose(self, filepath):
#         try:
#             res = 80
#             im = PIL.Image.open(filepath)
#             im = im.convert('RGB')
#             im = im.resize((res, res), PIL.Image.Resampling.LANCZOS)
#             im = np.asarray(im)
#             im = im / 255.
#             im = im.reshape((1, res, res, 3))
#             pred = self.model.predict(im, verbose=0)
#             pred_class = self.class_names[np.argmax(pred)]
#             pred_class = pred_class.replace('_', ' ')
#             os.remove(filepath)
#             return pred_class
#         except Exception as e:
#             print(f"Произошла ошибка: {e}")
#     def load(self):
#         try:
#             file_dialog = QFileDialog()
#             # Установка фильтра для выбора только файлов изображений
#             file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
#             file_dialog.selectNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
#             # Открытие диалогового окна
#             file_dialog.exec()
#             # Получение выбранного пути к файлу
#             filepath = file_dialog.selectedFiles()[0]
#             n = 0
#             if filepath:
#                 original_fp = filepath
#                 n += 1
#                 new_file = '.\\1' + str(n) + '.pic.' + filepath.split('.')[-1]
#                 if os.path.exists(new_file):
#                     n += 1
#                     new_file = '.\\1' + str(n) + '.pic.' + filepath.split('.')[-1]
#                 shutil.copy(filepath, new_file)
#                 filepath = new_file
#                 self.filepath = filepath
#                 self.pic.setPixmap(QtGui.QPixmap(filepath))
#                 self.label.setText(self.getpose(filepath))
#         except Exception as e:
#             print(f"Произошла ошибка: {e}")