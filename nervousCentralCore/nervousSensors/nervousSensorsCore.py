from nervousSensors.cameraSensor import cameraCore

class NervousSensors():

	eyes = None
	battery = None
	motion = None
	upperLaser = None
	downLaser = None
	leftLaser = None
	rightLaser = None
	backLaser = None
	leftEar = None
	rightEar = None

	def __init__ (self):
		self.eyes = cameraCore.Camera()
		self.eyes.startSight(0)
		#battery = Battery()
		#motion = Motion()
		#upperLaser = UpperLaser()
		#downLaser = DownLaser()
		#leftLaser = LeftLaser()
		#rightLaser = RightLaser()
		#backLaser = BackLaser()
		#leftEar = LeftEar()
		#rightEar = RightEar()


	def getEyes(self):
		return self.eyes.getSight(True)

