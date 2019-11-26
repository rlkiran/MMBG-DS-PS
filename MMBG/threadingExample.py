from PyQt5 import QtWidgets, uic, QtCore , QtGui
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
import sys
import os
from os import path
import threading
import time
import pyautogui

import datetime
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
		self.levelCountNum = 0
		self.missCountNum = 0
		self.bExit = True
		self.T1Exit = True

		self.session = False
		self.startPin = 4
		self.stopPin = 17
		self.count = 0
		self.Level = 0

		homeIcon = os.getcwd() + "//images//Icons//" +"home.png"
		folderIcon = os.getcwd() + "//images//Icons//" +"folder.png"
		logoutIcon = os.getcwd() + "//images//Icons//" +"logout.png"
		self.levelCount = self.findChild(QtWidgets.QLabel, 'levelCount')
		self.missCount = self.findChild(QtWidgets.QLabel, 'missCount')
		self.studentName = self.findChild(QtWidgets.QLabel, 'studentName')
		self.statusLabel = self.findChild(QtWidgets.QLabel, 'statusLabel')
		self.levelCount.setText(str(self.levelCountNum))
		self.missCount.setText(str(self.missCountNum))
		self.studentName.setText("userName"+" - Class "+"className")
		self.homeBtn = self.findChild(QtWidgets.QPushButton, 'homeBt')
		self.homeBtn.setIcon(QtGui.QIcon(homeIcon))
		self.finishBtn = self.findChild(QtWidgets.QPushButton, 'finishBt')
		self.startBt = self.findChild(QtWidgets.QPushButton, 'startBt')

		self.folderBtn = self.findChild(QtWidgets.QPushButton, 'folderBt')
		self.folderBtn.setIcon(QtGui.QIcon(folderIcon))

		self.logoutBtn = self.findChild(QtWidgets.QPushButton,'logoutBt')
		self.logoutBtn.setIcon(QtGui.QIcon(logoutIcon))

		self.logoutBtn.clicked.connect((self.logout))
		self.homeBtn.clicked.connect(self.opencatSelec)
		self.folderBtn.clicked.connect(self.openFolder)
		self.finishBtn.clicked.connect(self.takess)
		self.startBt.clicked.connect(self.startT1)

		
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
		self.second_time = datetime.now()
		self.second_time = str(self.second_time.hour)+":"+str(self.second_time.minute)+":"+str(self.second_time.second)
		self.fmt = '%H:%M:%S'
		self.tstamp1 = datetime.strptime(self.first_time, self.fmt)
		self.tstamp2 = datetime.strptime(self.second_time, self.fmt)
		self.finalTime = str(int(round(abs((self.tstamp1 - self.tstamp2).total_seconds()) / 60)))+" Minutes : "+str(int(abs((self.tstamp1 - self.tstamp2).total_seconds()))) + " seconds"
		self.statusLabel.setText("FINISHED in "+self.finalTime)
		self.Level = 0
		self.count = 0
		self.bExit = False
		self.T1Exit = True
		self.levelCountNum  = 0
		self.missCountNum   = 0
		self.levelCount.setText("0")
		self.missCount.setText("0")
	def startT1(self):
		self.bExit = True
		self.t1 = threading.Thread(target=self.startUP)
		GPIO.setup(self.startPin, GPIO.IN, GPIO.PUD_UP)
		GPIO.setup(self.stopPin, GPIO.IN, GPIO.PUD_UP)
		if self.T1Exit:
			self.first_time = datetime.now()
			self.first_time = str(self.first_time.hour)+":"+str(self.first_time.minute)+":"+str(self.first_time.second)
			self.t1.start()
			self.T1Exit = False
	def startUP(self):
		self.statusLabel.setText("STARTED")
		while self.bExit:
			self.startState = GPIO.input(self.startPin)
			self.stopState = GPIO.input(self.stopPin)
			if self.count > 9 and self.session:
				self.session = False
				print("Level Down")
				if self.Level > 0:
					self.Level -= 1
					self.levelCount.setText(str(self.Level))
				self.count = -1
			if (self.stopState == GPIO.LOW and self.count < 10):
				self.Level += 1
				self.levelCount.setText(str(self.Level))
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

	def quitApp(self):
		self.takess()
		sys.exit(0)   

def createMainWindow():
		window = physicalSlate()
		sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)
createMainWindow()