#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os,codecs
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
from pygame import mixer
from pydub import AudioSegment
import mutagen.mp3

AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\ffmpeg\\bin\\ffprobe.exe"
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        

        self.searchlist = QtWidgets.QListWidget(self.centralwidget)
        self.searchlist.setGeometry(QtCore.QRect(10, 40, 300, 531))
        self.searchlist.setObjectName("searchlist")
        
        
        self.playlist = QtWidgets.QListWidget(self.centralwidget)
        self.playlist.setGeometry(QtCore.QRect(350, 40, 300, 531))
        self.playlist.setObjectName("playlist")
        
        
        self.mixlist = QtWidgets.QListWidget(self.centralwidget)
        self.mixlist.setGeometry(QtCore.QRect(700, 40, 300, 531))
        self.mixlist.setObjectName("mixlist")
        
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(10, 600, 200, 23))
        self.searchBtn.setObjectName("searchBtn")
        
        
        self.playBtn = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn.setGeometry(QtCore.QRect(350, 600, 100, 23))
        self.playBtn.setObjectName("playBtn")
        
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(460, 600, 100, 23))
        self.stopBtn.setObjectName("stopBtn")
        
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(570, 600, 100, 23))
        self.addBtn.setObjectName("addBtn")
        
        self.mixBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mixBtn.setGeometry(QtCore.QRect(680, 600, 100, 23))
        self.mixBtn.setObjectName("mixBtn")
        
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(790, 600, 100, 23))
        self.delBtn.setObjectName("delBtn")
        
        self.pauseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pauseBtn.setGeometry(QtCore.QRect(900, 600, 100, 23))
        self.pauseBtn.setObjectName("pauseBtn")

        self.fastBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fastBtn.setGeometry(QtCore.QRect(350, 650, 200, 23))
        self.fastBtn.setObjectName("fastBtn")

        self.slowBtn = QtWidgets.QPushButton(self.centralwidget)
        self.slowBtn.setGeometry(QtCore.QRect(560, 650, 200, 23))
        self.slowBtn.setObjectName("slowBtn")
        
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(10, 650, 100, 23))
        self.exitBtn.setObjectName("exitBtn")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Музыкальный плеер"))
        self.searchBtn.setText(_translate("MainWindow", "Искать на диске"))
        self.playBtn.setText(_translate("MainWindow", "Плей"))
        self.stopBtn.setText(_translate("MainWindow", "Стоп"))
        self.addBtn.setText(_translate("MainWindow", "Добавить"))
        self.mixBtn.setText(_translate("MainWindow", "Объединить"))
        self.delBtn.setText(_translate("MainWindow", "Удалить"))
        self.pauseBtn.setText(_translate("MainWindow", "Пауза"))
        self.fastBtn.setText(_translate("MainWindow", "В 2 раза быстрее"))
        self.slowBtn.setText(_translate("MainWindow", "В 2 раза медленнее"))
        self.exitBtn.setText(_translate("MainWindow", "Выход"))


#mp3=mutagen.mp3.MP3(r'D:\Музыка\Agualung - Brighter Than Sunshine1.mp3')
#mixer.init(frequency=int(mp3.info.sample_rate*4))
#mixer.init()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        path = os.getcwd()+'\\sound1.mp3'
        p=os.getcwd()+'\\dir.txt'
        if(os.path.exists(p)):
            file=open(u''+p)
            self.ui.lineEdit.setText(file.read().strip())
            file.close()
            self.mode='mp3'

                             
        self.ui.searchBtn.clicked.connect(self.scandisk)
        self.ui.searchlist.currentTextChanged.connect(self.getfiles)
        #self.ui.listWidget_2.currentTextChanged.connect(self.playmusic)
        self.ui.playBtn.clicked.connect(self.playmusic)
        self.ui.addBtn.clicked.connect(self.addmusic)
        self.ui.stopBtn.clicked.connect(self.stopmusic)
        self.ui.mixBtn.clicked.connect(self.mix)
        self.ui.delBtn.clicked.connect(self.delete)
        self.ui.pauseBtn.clicked.connect(self.pause)
        self.ui.fastBtn.clicked.connect(self.faster)
        self.ui.slowBtn.clicked.connect(self.slowly)
        self.ui.exitBtn.clicked.connect(self.close)
        self.songs=[]
        self.mixer=[]
        self.flag=0
        self.paused = True
        self.scandisk()
        
   
        
    def scandisk(self):
        self.mode='mp3'
        mas=[]
        mas2=[]
        p=str(self.ui.lineEdit.text()).strip()
        file = codecs.open(u''+os.getcwd()+'\\dir.txt', "w", "utf-8")
        file.write(p)
        file.close()
            
        for rootdir, dirs, files in os.walk(str(p)):
            for file in files:       
                if((file.split('.')[-1])=='mp3'):
                    mas.append(os.path.join(rootdir, file))
                    mas2.append(os.path.join(rootdir, file).split('\\')[-2])
        mas2 = dict(zip(mas2, mas2)).values()
        self.mp3=mas
        self.ui.searchlist.clear()
        for x in mas2:
            self.ui.searchlist.addItem(x.strip())
        
    
    def getfiles(self):
        self.flag=1
        self.mode='song'
        self.songs=[]
        self.ui.playlist.clear()
        catname=self.ui.searchlist.currentItem().text()
        for x in self.mp3:
            mp3=x.split('\\')[-2]
            if(catname==mp3.strip()):
                self.songs.append(x)
                self.ui.playlist.addItem(x.split('\\')[-1])
        self.ui.playlist.setFocus()
        self.flag=0
        
    def playmusic(self):
        if(self.flag==0):
            selitem=self.ui.playlist.currentRow()
            put=self.songs[selitem]
            mixer.quit()
            mixer.init()
            mixer.music.stop()
            mixer.music.load(u''+put)
            mixer.music.play()

    def faster(self):
        try:
            if(self.flag==0):
                selitem=self.ui.playlist.currentRow()
                put=self.songs[selitem]
                mixer.music.stop()
                mixer.quit()
                print(u''+put)
                mp3=mutagen.mp3.MP3(u''+put)
                mixer.init(frequency=mp3.info.sample_rate*3)

                mixer.music.load(u''+put)
                mixer.music.play()
        except Exception as e:
            print(e)
    def slowly(self):
        try:
            if(self.flag==0):
                selitem=self.ui.playlist.currentRow()
                put=self.songs[selitem]
                mixer.music.stop()
                mixer.quit()
                print(u''+put)
                mp3=mutagen.mp3.MP3(u''+put)
                mixer.init(frequency=int(mp3.info.sample_rate/3))

                mixer.music.load(u''+put)
                mixer.music.play()
        except Exception as e:
            print(e)
    def addmusic(self):
        if(self.flag==0):
            selitem=self.ui.playlist.currentRow()
            put=self.songs[selitem]
            self.mixer.append(put)
            self.ui.mixlist.addItem(put.split('\\')[-1])
    
    def mix(self):
        
        if(self.flag==0):
            try:
                output = AudioSegment.from_mp3(self.mixer[0])
                for i in range(1,len(self.mixer)):
                    print(self.mixer[0])
                    print(self.mixer[1])
                    sound1 = AudioSegment.from_mp3(self.mixer[1])
                    print(sound1)
                    output= output.append(sound1)
                output.export(format = "mp3")
            except Exception as e:
                print(e)
    def delete(self):
        self.flag=1
        self.mode='song'
        self.mixer=[]
        self.ui.mixlist.clear()
        self.ui.mixlist.setFocus()
        self.flag=0
        
    def stopmusic(self):
        mixer.music.stop()
        
    def pause(self):
        if self.paused == True:
            mixer.music.unpause()
            self.paused = False
        elif self.paused == False:
            mixer.music.pause()
            self.paused = True        
    
    def close(self):

        reply = QMessageBox.question(self, 'Message', "Вы точно хотите выйти?",
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            uic.loadUi('пока.ui',self)
        else:
            pass

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
