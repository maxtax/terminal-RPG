import art

def generateSurrondings(surronding):
	if surronding == 0:
		art.town()
	elif 1 <= surronding <=3:
		art.forest()
	elif 4 <= surronding <=6:
		art.mountain()
	else:
		art.sea()