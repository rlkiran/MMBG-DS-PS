from PyQt5 import QtWidgets, uic, QtCore , QtGui
from PyQt5.QtCore import Qt, QEvent, QEventLoop, QTimer, pyqtSlot, pyqtSignal, QPoint
from PyQt5.QtWidgets import QShortcut, QLineEdit, QMessageBox, QColorDialog, QPushButton, QApplication, QMainWindow, QAction, QSlider
from PyQt5.QtGui import QKeySequence, QImage, QPainter, QPen, QPixmap, QColor
from PyQt5.QtGui import QKeySequence

import sys
import subprocess
import threading
import time 
import os
import os.path
from os import path
import pyautogui

from datetime import datetime, date
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


global userDir
global LangDir
global cwd
global charctr
global crrED
global inputText
global loginValid 
global Today
global Lang
global Cat
global color
global fileList
global imgCount
global count
global userName
global className

count = 0
EC  =  ['A.png','E.png','I.png','O.png','S.png','W.png']
ES  =  ['a.png','f.png','l.png','q.png','v.png']
ECC =  ['A.png','E.png','J.png','N.png','R.png','W.png']
ECS =  ['a.png','f.png','k.png','o.png','t.png','x.png']
TV  =  ['1.png','5.png','9.png','12.png']
TC  =  ['4.png','8.png','12.png','16.png','20.png','24.png','28.png','32.png','36.png']
HV  =  ['1.png','5.png','8.png','11.png']
HC  =  ['1.png','5.png','8.png','11.png','16.png','21.png','26.png','30.png','34.png']


color = Qt.black
charctr = ''
loginValid = False
Today = str(date.today())

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('startupScreen.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.quitApp)
        self.show()

        loop = QEventLoop()
        QTimer.singleShot(6000, loop.quit)
        loop.exec_()
        self.close()
        self.open = LoginClass()
        
    def quitApp(self):
        sys.exit(0)

class LoginClass(QtWidgets.QMainWindow):
    def __init__(self):
        global cwd
        global charctr
        cwd = os.getcwd() 
        super(LoginClass, self).__init__()
        uic.loadUi('LoginScreen.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.quitApp)
        self.show()
        self.userNameED = self.findChild(QtWidgets.QLineEdit, 'userName')
        self.userNameED.installEventFilter(self)
        self.classNameED = self.findChild(QtWidgets.QLineEdit, 'className')
        self.classNameED.installEventFilter(self)
        self.LoginButton = self.findChild(QtWidgets.QPushButton, 'LoginButton')
        self.LoginButton.clicked.connect(self.openLs)
        self.AButton = self.findChild(QtWidgets.QPushButton, 'a')
        self.AButton.clicked.connect(lambda:self.printChr(self.AButton.text()))
        self.BButton = self.findChild(QtWidgets.QPushButton, 'b')
        self.BButton.clicked.connect(lambda:self.printChr(self.BButton.text()))
        self.CButton = self.findChild(QtWidgets.QPushButton, 'c')
        self.CButton.clicked.connect(lambda:self.printChr(self.CButton.text()))
        self.DButton = self.findChild(QtWidgets.QPushButton, 'd')
        self.DButton.clicked.connect(lambda:self.printChr(self.DButton.text()))
        self.EButton = self.findChild(QtWidgets.QPushButton, 'e')
        self.EButton.clicked.connect(lambda:self.printChr(self.EButton.text()))
        self.FButton = self.findChild(QtWidgets.QPushButton, 'f')
        self.FButton.clicked.connect(lambda:self.printChr(self.FButton.text()))
        self.GButton = self.findChild(QtWidgets.QPushButton, 'g')
        self.GButton.clicked.connect(lambda:self.printChr(self.GButton.text()))
        self.HButton = self.findChild(QtWidgets.QPushButton, 'h')
        self.HButton.clicked.connect(lambda:self.printChr(self.HButton.text()))
        self.IButton = self.findChild(QtWidgets.QPushButton, 'i')
        self.IButton.clicked.connect(lambda:self.printChr(self.IButton.text()))
        self.JButton = self.findChild(QtWidgets.QPushButton, 'j')
        self.JButton.clicked.connect(lambda:self.printChr(self.JButton.text()))
        self.KButton = self.findChild(QtWidgets.QPushButton, 'k')
        self.KButton.clicked.connect(lambda:self.printChr(self.KButton.text()))
        self.LButton = self.findChild(QtWidgets.QPushButton, 'l')
        self.LButton.clicked.connect(lambda:self.printChr(self.LButton.text()))
        self.MButton = self.findChild(QtWidgets.QPushButton, 'm')
        self.MButton.clicked.connect(lambda:self.printChr(self.MButton.text()))
        self.NButton = self.findChild(QtWidgets.QPushButton, 'n')
        self.NButton.clicked.connect(lambda:self.printChr(self.NButton.text()))
        self.OButton = self.findChild(QtWidgets.QPushButton, 'o')
        self.OButton.clicked.connect(lambda:self.printChr(self.OButton.text()))
        self.PButton = self.findChild(QtWidgets.QPushButton, 'p')
        self.PButton.clicked.connect(lambda:self.printChr(self.PButton.text()))
        self.QButton = self.findChild(QtWidgets.QPushButton, 'q')
        self.QButton.clicked.connect(lambda:self.printChr(self.QButton.text()))
        self.RButton = self.findChild(QtWidgets.QPushButton, 'r')
        self.RButton.clicked.connect(lambda:self.printChr(self.RButton.text()))
        self.SButton = self.findChild(QtWidgets.QPushButton, 's')
        self.SButton.clicked.connect(lambda:self.printChr(self.SButton.text()))
        self.TButton = self.findChild(QtWidgets.QPushButton, 't')
        self.TButton.clicked.connect(lambda:self.printChr(self.TButton.text()))
        self.UButton = self.findChild(QtWidgets.QPushButton, 'u')
        self.UButton.clicked.connect(lambda:self.printChr(self.UButton.text()))
        self.VButton = self.findChild(QtWidgets.QPushButton, 'v')
        self.VButton.clicked.connect(lambda:self.printChr(self.VButton.text()))
        self.WButton = self.findChild(QtWidgets.QPushButton, 'w')
        self.WButton.clicked.connect(lambda:self.printChr(self.WButton.text()))
        self.XButton = self.findChild(QtWidgets.QPushButton, 'x')
        self.XButton.clicked.connect(lambda:self.printChr(self.XButton.text()))
        self.YButton = self.findChild(QtWidgets.QPushButton, 'y')
        self.YButton.clicked.connect(lambda:self.printChr(self.YButton.text()))
        self.ZButton = self.findChild(QtWidgets.QPushButton, 'z')
        self.ZButton.clicked.connect(lambda:self.printChr(self.ZButton.text()))

        self.Button0 = self.findChild(QtWidgets.QPushButton, 'b0')
        self.Button0.clicked.connect(lambda:self.printChr(self.Button0.text()))
        self.Button1 = self.findChild(QtWidgets.QPushButton, 'b1')
        self.Button1.clicked.connect(lambda:self.printChr(self.Button1.text()))
        self.Button2 = self.findChild(QtWidgets.QPushButton, 'b2')
        self.Button2.clicked.connect(lambda:self.printChr(self.Button2.text()))
        self.Button3 = self.findChild(QtWidgets.QPushButton, 'b3')
        self.Button3.clicked.connect(lambda:self.printChr(self.Button3.text()))
        self.Button4 = self.findChild(QtWidgets.QPushButton, 'b4')
        self.Button4.clicked.connect(lambda:self.printChr(self.Button4.text()))
        self.Button5 = self.findChild(QtWidgets.QPushButton, 'b5')
        self.Button5.clicked.connect(lambda:self.printChr(self.Button5.text()))
        self.Button6 = self.findChild(QtWidgets.QPushButton, 'b6')
        self.Button6.clicked.connect(lambda:self.printChr(self.Button6.text()))
        self.Button7 = self.findChild(QtWidgets.QPushButton, 'b7')
        self.Button7.clicked.connect(lambda:self.printChr(self.Button7.text()))
        self.Button8 = self.findChild(QtWidgets.QPushButton, 'b8')
        self.Button8.clicked.connect(lambda:self.printChr(self.Button8.text()))
        self.Button9 = self.findChild(QtWidgets.QPushButton, 'b9')
        self.Button9.clicked.connect(lambda:self.printChr(self.Button9.text()))
        self.ButtonPoint = self.findChild(QtWidgets.QPushButton, 'bpoint')
        self.ButtonPoint.clicked.connect(lambda:self.printChr(self.ButtonPoint.text()))
        self.ButtonDelete = self.findChild(QtWidgets.QPushButton, 'deleteb')
        self.ButtonDelete.clicked.connect(lambda:self.printChr(self.ButtonDelete.text()))
        self.SpaceButton = self.findChild(QtWidgets.QPushButton, 'space')
        self.SpaceButton.clicked.connect(lambda:self.printChr(self.SpaceButton.text()))    
    def quitApp(self):
        sys.exit(0)

    def eventFilter(self,obj,event):
        global crrED
        global inputText
        if event.type() == QEvent.FocusIn:
            if obj == self.userNameED:
                crrED = "userNameED"
                inputText = ''
            if obj == self.classNameED:
                crrED = "classNameED"
                inputText = ''
        return super(LoginClass, self).eventFilter(obj, event)

    def getData(self):
        global cwd
        global userDir
        global loginValid
        global Today
        global userName
        global className
        userName = self.userNameED.text().strip()
        className = self.classNameED.text().strip()
        if (not userName) or (not className):
            loginValid = True
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please Fill All The Required Fields')
            msg.setWindowTitle("Error")
            msg.exec_()

        if path.exists(cwd+"//Users//"+className+"//"+userName+"//"+Today):
            userDir = cwd+"//Users//"+className+"//"+userName+"//"+Today
            # print("User created at ",userDir)
            os.chdir(cwd)   
        
        elif path.exists(cwd+"//Users//"+className+"//"+userName):
            os.chdir(cwd+"//Users//"+className+"//"+userName)
            os.mkdir(Today)
            userDir = cwd+"//Users//"+className+"//"+userName+"//"+Today
            # print("User created at ",userDir)
            os.chdir(cwd)

        elif path.exists(cwd+"//Users//"+className):
            os.chdir(cwd+"//Users//"+className)
            os.mkdir(userName)
            os.chdir(cwd+"//Users//"+className+"//"+userName)
            os.mkdir(Today)
            os.chdir(cwd+"//Users//"+className+"//"+userName+"//"+Today)
            userDir = cwd+"//Users//"+className+"//"+userName+"//"+Today
            # print("User created at ",userDir)
            os.chdir(cwd)
        elif path.exists(cwd+"//Users"):
            os.chdir(cwd+"//Users")
            os.mkdir(className)
            os.chdir(cwd+"//Users//"+className)
            os.mkdir(userName)
            os.chdir(cwd+"//Users//"+className+"//"+userName)
            os.mkdir(Today)
            os.chdir(cwd+"//Users//"+className+"//"+userName+"//"+Today)
            userDir = cwd+"//Users//"+className+"//"+userName+"//"+Today
            # print("User created at ",userDir)
            os.chdir(cwd)


    def openLs(self):
        global loginValid
        self.getData()
        if(not loginValid):
            loop = QEventLoop()
            QTimer.singleShot(100, loop.quit)
            loop.exec_()
            self.close()
            self.open = selectCategory()
            #self.open = LanguageSelection()
        else:
            loginValid = False
        # self.open = CanvasClass()
    def printChr(self,charctr):
        # self.userNameED
        # self.classNameED
        global crrED
        if(crrED == "userNameED"):
            old_text =self.userNameED.text()
            if(charctr=="Delete"):
                curr_text = old_text[:-1]
            elif(charctr=="space"):
                curr_text = old_text + " "
            else:
                curr_text = old_text + charctr
            self.userNameED.setText(curr_text)
        if(crrED == "classNameED"):
            old_text =self.classNameED.text()
            if(charctr=="Delete"):
                curr_text = old_text[:-1]
            elif(charctr=="space"):
                curr_text = old_text + " "
            else:
                curr_text = old_text + charctr
            self.classNameED.setText(curr_text)

class selectCategory(QtWidgets.QMainWindow):
    def __init__(self):
        super(selectCategory, self).__init__()
        uic.loadUi('selectCategory.ui',self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.quitApp)
        self.CatList = self.findChild(QtWidgets.QComboBox, 'catCB')
        catSelection = ["Physical Slate","Digital Slate"]
        self.CatList.addItems(catSelection)
        self.catProceedButton = self.findChild(QtWidgets.QPushButton,'catProceed')
        self.catProceedButton.clicked.connect(self.openChoice)
        self.show()
    def openChoice(self):
        selectedCategory = "Physical Slate"
        selectedCategory = self.CatList.currentText()
        if selectedCategory == "Physical Slate":
            self.close()
            try:
                self.open = physicalSlate()
            except Exception as e:
                print(str(e))
            
        elif selectedCategory == "Digital Slate":
            self.close()
            self.open = LanguageSelection()
    def quitApp(self):
        sys.exit(0)

class physicalSlate(QtWidgets.QMainWindow):
    def __init__(self):
        super(physicalSlate, self).__init__()
        uic.loadUi('physicalSlate.ui',self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.quitApp)
        global userName
        global className
        global userDir
        global cwd
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
        self.studentName.setText(userName+" - Class "+className)
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
        subprocess.Popen(["xdg-open", userDir+"//screenshots//"])
    def logout(self):
        self.close()
        self.open = LoginClass()
    def takess(self):
        self.second_time = datetime.now()
        self.second_time = str(self.second_time.hour)+":"+str(self.second_time.minute)+":"+str(self.second_time.second)
        self.fmt = '%H:%M:%S'
        self.tstamp1 = datetime.strptime(self.first_time,self.fmt)
        self.tstamp2 = datetime.strptime(self.second_time,self.fmt)
        self.finalTime = str(int(round(abs((self.tstamp1 - self.tstamp2).total_seconds()) / 60)))+" Minutes : "+str(int(abs((self.tstamp1 - self.tstamp2).total_seconds()))) + " seconds"
        self.statusLabel.setText("FINISHED in "+self.finalTime)
        if path.exists(userDir+"//screenshots//"):
            os.chdir(userDir+"//screenshots//")
            self.thisScreenshot = pyautogui.screenshot()
            self.thisScreenshot.save(userName+" - "+self.second_time+'.png')
            os.chdir(cwd)
        else:
            os.chdir(userDir)
            os.mkdir("screenshots")
            self.thisScreenshot = pyautogui.screenshot()
            self.thisScreenshot.save(userName+" - "+self.second_time+'.png')
            os.chdir(cwd)
        self.bExit = False
        self.T1Exit = True
        self.levelCountNum  = 0
        self.missCountNum   = 0

    def startT1(self):
        self.levelCount.setText("0")
        self.missCount.setText("0")
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

class LanguageSelection(QtWidgets.QMainWindow):
    def __init__(self):
        global cwd
        cwd = os.getcwd() 
        super(LanguageSelection, self).__init__()
        uic.loadUi('languageSelection.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.quitApp)
        self.proceedButton = self.findChild(QtWidgets.QPushButton,'proceedButton')
        self.proceedButton.clicked.connect(self.openCanvas)
        self.LangList = self.findChild(QtWidgets.QComboBox, 'LangCB')
        Langs = ['English','English Cursive','Telugu','Hindi']
        self.LangList.addItems(Langs)
        self.CatList = self.findChild(QtWidgets.QComboBox, 'CatCB')
        self.LangList.currentTextChanged.connect(self.setLang)
        self.CatList.currentTextChanged.connect(self.setCat)
        self.setLang()
        self.setCat()
        self.show()

    def setLang(self):
        global Lang
        Lang = self.LangList.currentText()
        cats = []
        if Lang == "English":
            cats = ["CAPITAL","SMALL"]
            self.CatList.clear()
            self.CatList.addItems(cats)
        if Lang == "English Cursive":
            cats = ["CAPITAL","SMALL"]
            self.CatList.clear()
            self.CatList.addItems(cats)
        if Lang == "Telugu":
            cats = ["Consonants","Vowels"]
            self.CatList.clear()
            self.CatList.addItems(cats)
        if Lang == "Hindi":
            cats = ["Consonants","Vowels"]
            self.CatList.clear()
            self.CatList.addItems(cats)

    def setCat(self):
        global Cat
        Cat = self.CatList.currentText()

    def getData(self):
        global cwd
        global LangDir
        global Lang
        global Cat
        global fileList
        global imgCount
        global count
        LangDir = cwd + "//images//alphabets//"+Lang+"//"+Cat
        # print(LangDir)
        if(Lang=="English" and Cat=="CAPITAL"):
            fileList = EC.copy()
            imgCount = len(fileList)
        elif(Lang=="English" and Cat=="SMALL"):
            fileList = ES.copy()
            imgCount = len(fileList)
        elif(Lang=="English Cursive" and Cat=="CAPITAL"):
            fileList = ECC.copy()
            imgCount = len(fileList)
        elif(Lang=="English Cursive" and Cat=="SMALL"):
            fileList = ECS.copy()
            imgCount = len(fileList)
        elif(Lang=="Hindi" and Cat=="Consonants"):
            fileList = HC.copy()
            imgCount = len(fileList)
        elif(Lang=="Hindi" and Cat=="Vowels"):
            fileList = HV.copy()
            imgCount = len(fileList)
        elif(Lang=="Telugu" and Cat=="Consonants"):
            fileList = TC.copy()
            imgCount = len(fileList)
        elif(Lang=="Telugu" and Cat=="Vowels"):
            fileList = TV.copy()
            imgCount = len(fileList)
        count = 0
    def openCanvas(self):
        self.getData()
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec_()
        self.close()
        self.open = CanvasClass()


    def quitApp(self):
        sys.exit(0)

class CanvasClass(QtWidgets.QMainWindow):
    def __init__(self):
        global color
        super(CanvasClass, self).__init__()
        top = 0
        left = 0
        width = 800
        height = 480

        self.setGeometry(top, left, width, height)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        uic.loadUi('Canvas.ui', self)
        homeIcon = os.getcwd() + "//images//Icons//" +"home.png"
        logoutIcon = os.getcwd() + "//images//Icons//" +"logout.png"
        pencilIcon = os.getcwd() + "//images//Icons//" +"pencil_size.png"
        BrushIcon = os.getcwd() + "//images//Icons//" +"paint_brush.png"
        paletteIcon = os.getcwd() + "//images//Icons//" +"color_palette.png"
        eraserIcon = os.getcwd() + "//images//Icons//" +"eraser.png"
        folderIcon = os.getcwd() + "//images//Icons//" +"folder.png"
        self.folderBtn = self.findChild(QtWidgets.QPushButton, 'folderBt')
        self.folderBtn.setIcon(QtGui.QIcon(folderIcon))
        self.folderBtn.clicked.connect(self.openFolder)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.quitApp)
        self.homeImg = self.findChild(QtWidgets.QLabel, 'homeIcon')
        self.homeImg.setPixmap(QPixmap(homeIcon))
        self.BrushImg = self.findChild(QtWidgets.QLabel, 'BrushImg')
        self.BrushImg.setPixmap(QPixmap(BrushIcon))
        self.paleteButton = self.findChild(QtWidgets.QPushButton,'paleteButton')
        self.paleteButton.setIcon(QtGui.QIcon(paletteIcon))
        self.logoutButton = self.findChild(QtWidgets.QPushButton,'logoutButton')
        self.logoutButton.setIcon(QtGui.QIcon(logoutIcon))
        self.paleteButton.setIconSize(QtCore.QSize(24,24))
        self.paleteButton.clicked.connect(self.openColorDialog)
        self.logoutButton.clicked.connect((self.logout))
        self.HomeButton = self.findChild(QtWidgets.QPushButton,'HomeButton')
        self.HomeButton.clicked.connect(self.openLs)
        self.NextButton = self.findChild(QtWidgets.QPushButton,'NextButton')
        self.NextButton.clicked.connect(self.setCanvasImage)
        self.imgLabel = self.findChild(QtWidgets.QLabel, 'label')
        self.horizontalSlider = self.findChild(QtWidgets.QSlider,'horizontalSlider')
        self.horizontalSlider.valueChanged[int].connect(self.getsliderValue)

        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setValue(20)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(2)

        self.drawing = False
        self.brushSize = 20
        self.brushColor = color
        self.lastpoint = QPoint()

        self.show()      

    def openFolder(self):
        global userDir
        subprocess.Popen(["xdg-open", userDir])
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastpoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastpoint, event.pos())
            self.lastpoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def setCanvasImage(self):
        global LangDir
        global fileList
        global imgCount
        global count
        global Lang
        global Cat

        # print(imgCount)
        if(self.NextButton.text() == 'NEXT'):
            iname = str(Lang)+"-"+str(Cat)+"-"+str(count)
            self.saveImage(iname)
            self.clearCanvas()
            if count==imgCount-1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Success")
                msg.setInformativeText('You Have Successfully Completed the Task')
                msg.setWindowTitle("Success")
                msg.exec_()                
                self.openLs()
            elif count<imgCount-1:
                count = count + 1
                # print(count)
            else:
                count = 0
            self.imgLabel.setPixmap(QPixmap(LangDir + "//"+ fileList[count]))
        if(self.NextButton.text() == 'START'):
            self.NextButton.setText('NEXT')
            self.imgLabel.setPixmap(QPixmap(LangDir + "//"+ fileList[count]))
            self.clearCanvas()
    def clearCanvas(self):
        self.image.fill(Qt.white)
    def saveImage(self,imgname):
        global userDir
        global cwd
        os.chdir(userDir)
        filename = str(imgname)+".png"
        self.image.save(filename,"PNG")
        os.chdir(cwd)



    def quitApp(self):
        sys.exit(0)
    
    def openLs(self):
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec_()
        self.close()
        self.open = LanguageSelection()     
    @pyqtSlot()
    def on_click(self):
        openColorDialog(self)

    def openColorDialog(self):
        global color
        tmpcolor = QColorDialog.getColor()

        if tmpcolor.isValid():
            tmpcolor = (tmpcolor.name()).strip('#')
            tuple1 = tuple(int(tmpcolor[i:i+2], 16) for i in (0, 2, 4))
            color = QColor.fromRgb(tuple1[0],tuple1[1],tuple1[2])
            self.brushColor = color

    def logout(self):
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec_()
        self.close()
        self.open = LoginClass()

    def getsliderValue(self,value):
        self.brushSize= value

def createMainWindow():
    window = LoginClass()
    sys.exit(app.exec_())

app = QtWidgets.QApplication(sys.argv)
createMainWindow()