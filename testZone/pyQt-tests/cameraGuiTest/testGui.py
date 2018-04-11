import sys
from PyQt5.QtWidgets import (QApplication, QPushButton, QDesktopWidget, QFrame, 
	QTextEdit, QLabel, QLineEdit, QListWidget, QMainWindow)
from PyQt5.QtGui import QIcon, QColor, QPixmap, QFont, QImage
from PyQt5.QtCore import *
import time
import testCamera
import numpy as np
import random
import threading
import cv2

class Worker(QRunnable):

	main = 0

	def __init__(self, main):
		super(Worker, self).__init__()
		self.main = main

	@pyqtSlot()
	def run(self):
		while 1:
			self.main.updateImage()
			time.sleep(0.2)


class CameraDisplay(QLabel):
	def __init__(self, main):
		super(CameraDisplay, self).__init__(main)

	def updateFrame(self, image):
		self.setPixmap(QPixmap.fromImage(image))


class MainWindow(QMainWindow):

	camera = None
	lbl = None
	cameraDisplay = None
	cameraDisplaySignal = pyqtSignal(QImage)
    
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.threadpool = QThreadPool()

		self.resize(1000, 650)
		self.move(100,20)
		self.setWindowTitle('Droggo')
		self.setWindowIcon(QIcon('icon.png'))

		actionLbl = QLabel("Action status:",self)
		actionLbl.setFont(QFont('Arial', 12))
		actionLbl.resize(200,30)
		actionLbl.move(660,10)

		searchingActionBtn = QPushButton('Searching for objects',self)
		searchingActionBtn.setFont(QFont('Arial', 12))
		searchingActionBtn.resize(165,40)
		searchingActionBtn.move(660,50)
		searchingActionBtn.setEnabled(True)

		checkingActionBtn = QPushButton('Checking the object',self)
		checkingActionBtn.setFont(QFont('Arial', 12))
		checkingActionBtn.resize(165,40)
		checkingActionBtn.move(660,100)
		checkingActionBtn.setEnabled(False)

		learningActionBtn = QPushButton('Learning the object',self)
		learningActionBtn.setFont(QFont('Arial', 12))
		learningActionBtn.resize(165,40)
		learningActionBtn.move(830,50)
		learningActionBtn.setEnabled(False)

		confirmingActionBtn = QPushButton('Confirming the object',self)
		confirmingActionBtn.setFont(QFont('Arial', 12))
		confirmingActionBtn.resize(165,40)
		confirmingActionBtn.move(830,100)
		confirmingActionBtn.setEnabled(False)

		interactionLbl = QLabel("Interaction console:",self)
		interactionLbl.setFont(QFont('Arial', 12))
		interactionLbl.resize(200,30)
		interactionLbl.move(660,160)

		interaction = QListWidget(self)
		interaction.resize(330,150)
		interaction.move(660,190)

		inputDialog = QLineEdit(self)
		inputDialog.setFont(QFont('Arial', 11))
		inputDialog.resize(230,30)
		inputDialog.move(660,350)

		sendBtn = QPushButton('Send',self)
		sendBtn.setFont(QFont('Arial', 12))
		sendBtn.resize(90,30)
		sendBtn.move(900,350)

		objectListLbl = QLabel("Learn objects tree:",self)
		objectListLbl.setFont(QFont('Arial', 12))
		objectListLbl.resize(200,30)
		objectListLbl.move(660,390)

		objectList = QListWidget(self)
		objectList.resize(330,220)
		objectList.move(660,420)

		thoughtsLbl = QLabel("Droggo thoughts console:",self)
		thoughtsLbl.setFont(QFont('Arial', 12))
		thoughtsLbl.resize(200,30)
		thoughtsLbl.move(10,490)

		thoughts = QListWidget(self)
		thoughts.resize(640,120)
		thoughts.move(10,520)

		self.camera = testCamera.Camera()
		self.camera.startCapture(0)

		self.cameraDisplay = CameraDisplay(self)
		self.cameraDisplaySignal.connect(self.cameraDisplay.updateFrame)
		self.cameraDisplay.setPixmap(QPixmap('teste1.jpg'))
		self.cameraDisplay.resize(640,480)
		self.cameraDisplay.move(10,10)

		self.show()

		worker = Worker(self)
		self.threadpool.start(worker)



	def updateImage(self):
		image, ret = self.camera.takeSnapshot()

		if ret:

			height, width,_ = image.shape
			imageRGB = np.ones((width, height, 3), np.uint8)
			
			for i in range(width):
				for j in range(height):
					for k in range(3):
						imageRGB[i,j,k] = (int)(image[j,i,k]*255)

			height, width, bytesPerComponent = imageRGB.shape
			bytesPerLine = bytesPerComponent * width

			cv2.cvtColor(imageRGB, cv2.COLOR_BGR2RGB, imageRGB)

			qImage = QImage(imageRGB.data, 320, 240, bytesPerLine, QImage.Format_RGB888)

			try:
				self.cameraDisplaySignal.emit(qImage)
			
			except Exception:
				print("ups")
		

class App():

	def __init__(self):

		app = QApplication([])
		self.window = MainWindow()
		app.exec_()

	def getWindow(self):
		return self.window

if __name__ == "__main__":
	app = QApplication([])
	window = MainWindow()
	sys.exit(app.exec_())