from hp import Hp
from mana import Mana

class Monsters(Hp,Mana):

	def __init__(self, monsterKind,hp,mana):
		Hp.__init__(self,hp)
		Mana.__init__(self,mana)
		self.monsterKind = monsterKind

	def setMonsterKind(self,monsterKind):
		self.monsterKind = monsterKind
		return self.monsterKind

	#GET
	def getMonsterKind(self):
		return self.monsterKind
