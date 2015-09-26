from math import sqrt

class Vect2d:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	#add
	def add(self, x, y):
		self.x += x
		self.y += y

	def add(self, vect):
		self.x += vect.x
		self.y += vect.y

	#sub
	def sub(self, x, y):
		self.x -= x
		self.y -= y

	def sub(self, vect):
		self.x -= vect.x
		self.y -= vect.y

	#set
	def set(self, x, y):
		self.x = x
		self.y = y

	def set(self, vect):
		self.x = vect.x
		self.y = vect.y

	def length(self):
		return sqrt((self.x*self.x)+(self.y*self.y))

	def normalize(self):
		mag = self.length()
		self.x = (self.x/mag)
		self.y = (self.y/mag)