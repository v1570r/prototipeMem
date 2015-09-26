
import ctypes
from math import cos, sin, pi

from OpenGL import GL, GLU
from sdl2 import *

from maths import Vect2d


class Pointer:

	def __init__(self):
		self.pos = Vect2d(0, 0)


	def render(self):
		lineAmount = 100
		radius = 50.0
		twicePi = 2.0 * pi
	
		GL.glBegin(GL.GL_LINE_LOOP)    
		for i in range(lineAmount):    
			GL.glVertex2f(
			    self.pos.x + (radius * cos(i *  twicePi / lineAmount)), 
			    self.pos.y + (radius* sin(i * twicePi / lineAmount))
			)
		GL.glEnd()


	def update(self):
		mouseX = (c_int)()
		mouseY = (c_int)()
		SDL_GetMouseState(mouseX, mouseY)
		mousePos = Vect2d(mouseX.value, mouseY.value)
		self.pos.set(mousePos)

		print(self.pos.x , "  ", self.pos.y)