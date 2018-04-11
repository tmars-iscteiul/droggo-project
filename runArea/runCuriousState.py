import sys
sys.path.append('../graphicsZone/')
sys.path.append('../nervousCentralCore/nervousSensors/camera/')

import curiousStateGUI
import cameraCore
import threading
import time
from PyQt5.QtCore import QThread

class GuiGenerator(QThread):

	def __init__(self):
		QThread.__init__(self)

	def __del__(self):
		self.wait()

	def run(self):
		gui = curiousStateGUI.App()
		self.sleep(1)

	def sendPackageInfo(package):
		pass


class VisionGenerator():

	vision = cameraCore.Camera()
	image = None
	active = True

	def startVision(self):

		self.vision.startSight(1)
		self.active = True

		while(self.active):
			image, ret = self.vision.getVision(True)

			if ret == False:
				active = False
				break

			time.sleep(0.01)


gui = GuiGenerator()
vision = VisionGenerator()

visionThread = threading.Thread(target=vision.startVision(), name='visionThread').start()
gui.start()
#guiThread = threading.Thread(target=gui.createApp(), name='guiThread').start()