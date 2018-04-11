import numpy as np
import testCamera
import testGui
from PyQt5.QtCore import *
import time

class CamWorker(QRunnable):

	def __init__(self):
		super(CamWorker, self).__init__()

	@pyqtSlot()
	def run(self):
		camera = testCamera.Camera()

class GuiWorker(QRunnable):

	def __init__(self):
		super(GuiWorker, self).__init__()

	@pyqtSlot()
	def run(self):
		app = testGui.App()
		self.window = app.getWindow()

class Main():
	
	def __init__(self):
		self.threadpool = QThreadPool()
		camworker = CamWorker()
		self.threadpool.start(camworker)
		guiworker = GuiWorker()
		self.threadpool.start(guiworker)

		while(True):
			a = 1

main = Main()


