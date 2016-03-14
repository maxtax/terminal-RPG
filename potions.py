from hero import Hero

class Potions(object):
	def __init__(self, newHp):
		self.newHp = newHp

	def healingPotion(self, potionStrength, playerHp):
		self.newHp = potionStrength + playerHp
		return self.newHp

	def manaPotion(self, potionStrength, playerMana):
		self.newMana = potionStrength + playerMana
		return self.newMana