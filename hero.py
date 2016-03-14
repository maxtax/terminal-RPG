from hp import Hp
from mana import Mana

class Hero(Hp,Mana):

	def __init__(self, heroClass, name,hp,mana):
		Hp.__init__(self,hp)
		Mana.__init__(self,mana)
		self.name = name
		self.heroClass = heroClass

	#SET
	def setHeroName(self,name):
		self.name = name
		return self.name

	def setHeroClass(self,heroClass):
		self.heroClass = heroClass
		return self.heroClass

	#GET
	def getHeroName(self):
		return self.name

	def getHeroClass(self):
		return self.heroClass