from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow , QShortcut
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import QKeySequence

import sys
import os
from os import path
import time
import pyautogui
import subprocess
from datetime import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

physicalSlateUI, _ = uic.loadUiType("mainwindow.ui") #the path to UI

class ActivityThread(QThread):
    #signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, currentLevel ,currentMiss, totalLevel , totalMiss):
        QThread.__init__(self)
        self.currentLevel = currentLevel
        self.currentMiss = currentMiss
        self.totalLevel = totalLevel
        self.totalMiss = totalMiss
        self.currentLevelCount = 0
        self.currentMissCount = 0
        self.totalLevelCount = 0
        self.totalMissCount = 0

        self.session = False
        self.startPin = 4
        self.stopPin = 17

        self.startTime = 0
        self.stopTime = 0
        self.curretTime = 0

        GPIO.setup(self.startPin, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.stopPin, GPIO.IN, GPIO.PUD_UP)

    def run(self):
       while True:
       	    # self.currentLevel.setText(str(self.currentLevelCount))
            # self.currentMiss.setText(str(self.currentMissCount))
            # self.totalLevel.setText(str(self.totalLevelCount))
            # self.totalMiss.setText(str(self.totalMissCount))
       	    self.startState = GPIO.input(self.startPin)
            self.stopState = GPIO.input(self.stopPin)

            if self.startState == GPIO.LOW:
                self.session = True
            if self.session == True:
            	if self.startState == GPIO.HIGH:
                    self.currentMissCount += 1
                    self.currentMiss.setText(str(self.currentMissCount))
                    time.sleep(2)
                if self.stopState == GPIO.LOW:
                    self.currentLevelCount += 1
                    self.currentMissCount = 0
                    self.currentMiss.setText(str(self.currentMissCount))
                    self.currentLevel.setText(str(self.currentLevelCount))
                    time.sleep(2)
                    self.session = False


    def finishSession(self):
        pass # take ss , wait for 2 seconds 
        # time.sleep(1)
        # self.count += 1
        # self.signal.emit(self.count)

class PhysicalSlate(QMainWindow, physicalSlateUI):

    def __init__(self):

        QMainWindow.__init__(self)
        physicalSlateUI.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.quitApp)

        #self.pushButton.setText("Start Thread 1")
        #self.pushButton.clicked.connect(self.startThread)
        self.test_thread = ActivityThread(self.currentLevel, self.currentMiss , self.totalLevel , self.totalMiss) 
        #self.test_thread.signal.connect(self.finished)
        self.startThread()



    def startThread(self):
        #self.pushButton.setEnabled(False)  # Disables the pushButton
        self.test_thread.start()
    def quitApp(self):
        sys.exit(0)   

    # def finished(self, result):
    #     self.pushButton.setEnabled(True)
    #     self.pushButton.setText("Thread Stopped at "+str(result))
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = PhysicalSlate()
    window.show()
    sys.exit(app.exec_())
