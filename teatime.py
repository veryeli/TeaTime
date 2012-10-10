import random
import datetime

class Donut:
  def __init__(self, flavor):
		self.flavor = flavor
		self.bites_left = 6

class Samosa:
	def __init__(self):
		self.bites_left = 10

flavors = ["creamy", "chocolatey", "chocolatey", "chocolatey", "cakey", "yeasty","yeasty","yeasty","yeasty","yeasty","yeasty", "sprinkles"]

donuts = []
samosas = []

def replenish():
	global donuts
	global samosas
	donuts = [Donut(random.choice(flavors)) for i in range(60)]
	samosas = [Samosa for i in range(30)]

def nom_nom_nom():
	print 'OMGZ! Look at all these snacks!'
	while donuts or samosas:
		desire = random.choice([donuts, samosas])
		if (desire == donuts and donuts) or (desire == samosas and not samosas):
			eat_next = random.choice(donuts)
			print 'nom nom nom {0} donut'.format(eat_next.flavor)
			if desire == samosas:
				desire = donuts
		else:
			eat_next = random.choice(samosas)
			print 'nom nom nom samosa'
			if desire == donuts:
				desire = samosas
		desire.remove(eat_next)

def teatime():
	print '3pm! Yay!'
	replenish()
	nom_nom_nom()
	print 'All gone! :('
	print '...'
	print '3:30!' #replenish
	replenish()
	nom_nom_nom()

teatime()
