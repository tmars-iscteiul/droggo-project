import sys
sys.path.append('../graphicsZone/')
sys.path.append('../nervousCentralCore/nervousSensors/camera/')

import curiousStateGUI
import cameraCore
import threading
import time
from PyQt5.QtCore import QThread

class GuiGenerator():

	def createApp(self):
		gui = curiousStateGUI.App()

	def sendPackageInfo(package):
		pass


class VisionGenerator():

	vision = cameraCore.Camera()
	image = None
	active = True

	def startVision(self):

		self.vision.startSight(0)
		self.active = True

		while(self.active):
			image, ret = self.vision.getVision(True)

			if ret == False:
				active = False
				break

			time.sleep(0.01)



vision = VisionGenerator()
gui = GuiGenerator()

visionThread = threading.Thread(target=vision.startVision(), name='visionThread').start()
guiThread = threading.Thread(target=gui.createApp(), name='guiThread').start()