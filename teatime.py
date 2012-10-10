import random
import datetime

class Doughnut:
  def __init__(self, flavor):
    self.flavor = flavor
    self.bites_left = 6

class Samosa
  def __init__(self):
    self.bites_left = 10

flavors = ["creamy", "chocolatey", "cakey", "yeasty", "sprinkles"]

doughnuts = [Doughnut(random.choice(flavors)) for i in range(60)]
samosas = [Samosa for i in range(30)]

def teatime():
  desire = doughnuts
  while doughnuts or samosas:
    if desire = dougnuts:
      if dougnuts:
        eat_next = random.choice(doughnuts)
        doughnuts.remove(eat_next)
        desire = samosas
      else if desire = samosas:
        if samosas:
          eat_next = random.choice(samosas)
          samosas.remove(eat_next)
          desire = doughnuts
  if datetime.now() == 3:30: #replenish
    doughnuts = [Doughnut(random.choice(flavors)) for i in range(60)]
    samosas = [Samosa for i in range(30)]

teatime()
