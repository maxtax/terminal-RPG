import random
import art
import game

class Areas(object):

	def __init__(self, monster, player):
		self.monster = monster
		self.player = player

	def battleArena(self):
		print "The monster is a " + self.monster.getMonsterKind() + " and his HP/Mana is " + str(self.monster.getHp()) + "/" + str(self.monster.getMana()) + "!"
		if self.monster.getMonsterKind() == "Ogre":
			art.ogre()
		elif self.monster.getMonsterKind() == "Imp":
			art.imp()
		else:
			art.skeleton()
		print "***********************"
		print "You have " + str(self.player.getHp()) + " HP and " + str(self.player.getMana()) + " mana!"
		monsterBattleHp = self.monster.getHp()
		playerBattleHp = self.player.getHp()
		while True:
			print "***********************"
			print "1.Kick 2.Punch 3.Spit 4.Run"
			choice = raw_input("Choose your move: ")
			if choice == str(1):
				damage = random.randint(5,20)
				monsterBattleHp = monsterBattleHp - damage
				print "You hit and makes " + str(damage) + " damage! The " + self.monster.getMonsterKind() + " has " + str(monsterBattleHp) + " left!"
			elif choice == str(2):
				damage = random.randint(1,23)
				monsterBattleHp = monsterBattleHp - damage
				print "You hit and makes " + str(damage) + " damage! The " + self.monster.getMonsterKind() + " has " + str(monsterBattleHp) + " left!"
			elif choice == str(3):
				print "Why did you spit on him? It just mad him angry! The " + self.monster.getMonsterKind() + " gets 100 hp extra."
				monsterBattleHp = monsterBattleHp + 100
			elif choice == str(4):
				print "You are a chicken! But will it work?"
				roll = random.randint(1,10)
				if roll == 10:
					print "Oh shit you made it!"
				else:
					game.gameover()
			else:
				print "You fumble and missed your move!"
			if monsterBattleHp <= 0:
				print "***********************"
				print "You killed that fucker!"
				print "***********************"
				newHp = playerBattleHp
				self.player.setHp(newHp)
				break
			else:
				monsterDamage = random.randint(1,10)
				if damage == str(1):
					print "You parry his blow! Good job!"
				else:
					playerBattleHp = playerBattleHp - monsterDamage
					print "You got punch in the face. You took " + str(monsterDamage) + " damage and have " + str(playerBattleHp) + " hp left!"
				if playerBattleHp <= 0:
					self.gameover()