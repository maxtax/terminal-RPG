from art import Art

class Nature(object):

	def __init__(self,surronding):
		self.surronding = surronding
		self.art = Art()

	def generateSurrondings(self, surronding):
		if surronding == 0:
			self.art.town()
		elif 1 <= surronding <=3:
			self.art.forest()
		elif 4 <= surronding <=6:
			self.art.mountain()
		else:
			self.art.sea()

