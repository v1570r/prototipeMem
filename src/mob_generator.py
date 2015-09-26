
import random

from mob import Mob


class MobGenerator:

	def __init__(self):
		self.maxMobs = random.randint(15, 22)
		self.mobs = []


	def generate(self):

		for i in range(self.maxMobs):
			posX = random.randint(200, 600)
			posY = random.randint(200, 500)
			self.mobs.append(Mob(posX, posY))



	def render(self):
		for mob in self.mobs:
			mob.render()


	def update(self):
		print(self.maxMobs)