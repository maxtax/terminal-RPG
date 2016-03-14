from hero import Hero
from potions import Potions
from monsters import Monsters
from battle import Areas
import art
from nature import Nature
import random

class GameController(object):

	def __init__(self):
		self.player = None
		self.monster = None
		self.nature = Nature(0)
		self.steps = 0

	def intro(self):
		self.potions = Potions(None)
		print "Are you ready to start? Press any button!"
		raw_input("Press Enter to continue...")
		self.createHero()
		print "***********************"
		print "Welcome " + self.player.getHeroName() + " the " + self.player.getHeroClass() + "!"
		self.gameplay()

	def gameplay(self):
		print "***********************"
		print "Your HP is " + str(self.player.getHp()) + " and your mana is " + str(self.player.getMana())+"."
		print "***********************"
		while True:
			print "What do you want to do?"
			print "1.Walk 2.Look around 3.Sleep 4.Check stats 5.Exit"
			nextMove = raw_input("Choose a number between 1-5: ")
			if nextMove == str(1):
				self.walk()
			elif nextMove == str(2):
				self.look(self.steps)
			elif nextMove == str(3):
				sleep()
			elif nextMove == str(4):
				print "Your HP is " + str(self.player.getHp()) + " and your mana is " + str(self.player.getMana())+"."
			elif nextMove == str(5):
				print "Bye!"
				return False

	def createHero(self):
		name = raw_input("Whats your heros name? ")
		print "***********************"
		print "What kind of hero do you want to be?"
		print "1. Knight 2.Wizard 3.Paladin"
		while True:
			heroKind = raw_input("Choose the number of the kind of hero you want to be: ")
			if heroKind == "1":
				heroClass = "Knight"
				hp = random.randint(100,120)
				mana = random.randint(20,40)
				break
			elif heroKind == "2":
				heroClass = "Wizard"
				hp = random.randint(60,80)
				mana = random.randint(100,120)
				break
			elif heroKind == "3":
				heroClass = "Paladin"
				hp = random.randint(80,100)
				mana = random.randint(40,60)
				break
			else:
				print "It needs to be a number between 1-3!"
				print "1. Knight 2.Wizard 3.Paladin"
		self.player = Hero(heroClass, name, hp, mana)

	def walk(self):
			self.steps = self.steps + 1
			if self.steps == 10:
				self.steps = 0
			roll = random.randint(1,10)
			if roll == 1:
				print "You find a health potion!"
				newHp = self.potions.healingPotion(10, self.player.getHp())
				self.player.setHp(newHp)
				art.bottleHealth()
				print "***********************"
				print "Your new HP is: " + str(self.player.getHp())
				print "***********************"
			elif roll == 2:
				print "You find a mana potion!"
				newMana = self.potions.manaPotion(10, self.player.getMana())
				self.player.setMana(newMana)
				art.bottleMana()
				print "***********************"
				print "Your new mana is: " + str(self.player.getMana())
				print "***********************"
			elif 3 <= roll <=6:
				print "***********************"
				print "Oh shit a MONSTER!!!!"
				print "***********************"
				self.createMonster()
				fight = Areas(self.monster,self.player)
				fight.battleArena()
			elif 7 <= roll <= 10:
				print "***********************"
				print "Nothing happen!"
				print "***********************"

	def look(self, steps):
		self.nature.generateSurrondings(steps)

	def createMonster(self):
		monsterRoll = random.randint(1,3)
		if monsterRoll == 1:
			monsterKind = "Imp"
			hp = 30
			mana = 20
		if monsterRoll == 2:
			monsterKind = "Ogre"
			hp = 80
			mana = 10
		if monsterRoll == 3:
			monsterKind = "Skeleton"
			hp = 40
			mana = 100
		self.monster = Monsters(monsterKind,hp,mana)

def gameover():
	print "You are dead. You didn't save the world from what ever you tried to save it from!"

def sleep(self):
	print "When you sleep you get back 100 hp. To bad this part of the game only can be accessed with microtransaction and that part isnt implemented yet..."

game = GameController()
game.intro()