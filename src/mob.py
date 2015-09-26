
import ctypes
from math import cos, sin, pi

from OpenGL import GL, GLU
from sdl2 import *

from maths import Vect2d


class Mob:

	def __init__(self, x, y):
		self.pos = Vect2d(x, y)
		self.vel = Vect2d(0, 0)
		self.accel = Vect2d(0, 0)


	def render(self):
		lineAmount = 100
		radius = 5.0
		twicePi = 2.0 * pi
	
		GL.glBegin(GL.GL_POLYGON)    
		for i in range(lineAmount):    
			GL.glVertex2f(
			    self.pos.x + (radius * cos(i *  twicePi / lineAmount)), 
			    self.pos.y + (radius * sin(i * twicePi / lineAmount))
			)
		GL.glEnd()


	#def response(self, force):
