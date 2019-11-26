from PyQt5 import QtWidgets, uic, QtCore , QtGui
from PyQt5.QtCore import QEventLoop, QTimer, pyqtSlot
from PyQt5.QtWidgets import QShortcut, QLineEdit, QMessageBox, QColorDialog, QPushButton
from PyQt5.QtGui import QKeySequence, QImage, QPainter, QPen, QPixmap
import os
import sys


class CanvasClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(CanvasClass, self).__init__()
        uic.loadUi('Canvas.ui', self)
        self.show()
        homeIcon = os.getcwd() + "\\images\\Icons\\" +"home.png"
        logoutIcon = os.getcwd() + "\\images\\Icons\\" +"logout.png"
        pencilIcon = os.getcwd() + "\\images\\Icons\\" +"pencil_size.png"
        paletteIcon = os.getcwd() + "\\images\\Icons\\" +"color_palette.png"
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.quitApp)
        self.homeImg = self.findChild(QtWidgets.QLabel, 'homeIcon')
        self.homeImg.setPixmap(QPixmap(homeIcon))
        self.logoutImg = self.findChild(QtWidgets.QLabel, 'logoutIcon')
        self.logoutImg.setPixmap(QPixmap(logoutIcon))
        self.pencilImg = self.findChild(QtWidgets.QLabel, 'pencilSize')
        self.pencilImg.setPixmap(QPixmap(pencilIcon))
        #self.paletImg = self.findChild(QtWidgets.QLabel, 'paletteIcon')
        #self.paletImg.setPixmap(QPixmap(paletteIcon))
        self.paleteButton = self.findChild(QtWidgets.QPushButton,'paleteButton')
        self.paleteButton.setIcon(QtGui.QIcon(paletteIcon))
        self.paleteButton.setIconSize(QtCore.QSize(24,24))
        self.paleteButton.clicked.connect(self.openColorDialog)        
    def quitApp(self):
        sys.exit(0)

    @pyqtSlot()
    def on_click(self):
        openColorDialog(self)

    def openColorDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            print(color.name())

# app = QtWidgets.QApplication(sys.argv)
# window = CanvasClass()
# window.show()
# app.exec()