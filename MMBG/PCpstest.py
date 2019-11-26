from PyQt5 import QtWidgets, uic, QtCore , QtGui
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence


import sys
import os
from os import path
import threading 


import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class physicalSlate(QtWidgets.QMainWindow):
    def __init__(self):
        super(physicalSlate, self).__init__()
        uic.loadUi('physicalSlate.ui',self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.quitApp)
        self.session = False
        self.startPin = 4
        self.stopPin = 17
        self.count = 0
        self.Level = 0
        self.levelCountNum = 1
        self.missCountNum = 1
        homeIcon = os.getcwd() + "//images//Icons//" +"home.png"
        folderIcon = os.getcwd() + "//images//Icons//" +"folder.png"
        logoutIcon = os.getcwd() + "//images//Icons//" +"logout.png"
        self.levelCount = self.findChild(QtWidgets.QLabel, 'levelCount')
        self.missCount = self.findChild(QtWidgets.QLabel, 'missCount')
        self.studentName = self.findChild(QtWidgets.QLabel, 'studentName')
        self.levelCount.setText(str(self.levelCountNum))
        self.missCount.setText(str(self.missCountNum))
        self.studentName.setText("userName"+" - Class "+"className")
        self.homeBtn = self.findChild(QtWidgets.QPushButton, 'homeBt')
        self.homeBtn.setIcon(QtGui.QIcon(homeIcon))
        self.finishBtn = self.findChild(QtWidgets.QPushButton, 'finishBt')

        self.folderBtn = self.findChild(QtWidgets.QPushButton, 'folderBt')
        self.folderBtn.setIcon(QtGui.QIcon(folderIcon))

        self.logoutBtn = self.findChild(QtWidgets.QPushButton,'logoutBt')
        self.logoutBtn.setIcon(QtGui.QIcon(logoutIcon))

        self.logoutBtn.clicked.connect((self.logout))
        self.homeBtn.clicked.connect(self.opencatSelec)
        self.folderBtn.clicked.connect(self.openFolder)
        self.finishBtn.clicked.connect(self.takess)
        GPIO.setup(startPin, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(stopPin, GPIO.IN, GPIO.PUD_UP)
        self.t1 = threading.Thread(target=self.self.startUP, args=(self,))
        self.t1.start()
        
        self.show()
    def opencatSelec(self):
        self.close()
        self.open = selectCategory()
    def openFolder(self):
        global userDir
        subprocess.Popen(["xdg-open", userDir])
    def logout(self):
        self.close()
        self.open = LoginClass()
    def takess(self):
        self.levelCount.setText("0")
        self.missCount.setText("0")
    def startUP(self):
        while True:
            self.startState = GPIO.input(self.startPin)
            self.stopState = GPIO.input(self.stopPin)
            if self.count >= 10 and self.session:
                self.session = False
                print("Level Down")
                if self.Level > 0:
                    self.Level -= 1
                    self.levelCount.setText(str(self.Level))
                self.count = 0
            if (self.stopState == GPIO.LOW and self.count < 10):
                self.Level += 1
                print("Level Up ",self.Level)
                self.count = 0
                time.sleep(1)
            if(self.startState == GPIO.LOW):
                self.session = True
            if(self.session):
                if(self.startState == GPIO.HIGH):
                    self.session = False
                    self.count += 1
                    self.missCount.setText(str(self.count))
                    time.sleep(0.5)
                    print("Level ",self.Level," Miss count ",self.count)
        print("LEVEL DOWN")

    def quitApp(self):
        sys.exit(0)   


def createMainWindow():
    window = physicalSlate()
    sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)
createMainWindow()