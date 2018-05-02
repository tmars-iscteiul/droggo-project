#from instinct import instinctCore
from nervousSystemLink import nervousSensorsLinkCore, nervousActuatorsLinkCore
from intelligence import intelligenceCore
from shortTermMemory import shortTermMemoryCore

class Brain():

	nervousSensors = None
	nervousActuators = None
	instinct = None
	intelligence = None
	memory = None
	

	def __init__(self, mainNervousSystem):
		self.nervousSensors = nervousSensorsLinkCore.NervousSensorsLink(mainNervousSystem)
		self.nervousActuators = nervousActuatorsLinkCore.NervousActuatorsLink(mainNervousSystem)
		intelligence = intelligenceCore.Intelligence(self)
		#instinct = instinctCore.Instinct()
		#memory = shortTermMemoryCore.ShortTermMemory()


	def getNervousSystem(self):
		return self.nervousSystem

	def getIntelligence(self):
		return self.intelligence

	def getInstinct(self):
		return self.instinct

	def getMemory(self):
		return self.memory


	
