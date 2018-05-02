from nervousSensors import nervousSensorsCore
from nervousActuators import nervousActuatorsCore

class NervousSystem():

	sensors = None
	actuators = None

	def __init__ (self):
		self.sensors = nervousSensorsCore.NervousSensors()
		#actuators = nervousActuatorsCore.NervousActuators(self)

	def getEyes(self):
		return self.sensors.getEyes()