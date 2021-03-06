"""
	Pointer class uses for iteraction with mouse and
	it execute the actions when click the button
"""

import ctypes
from math import cos, sin, pi

from OpenGL import GL, GLU
from sdl2 import *

from maths import Vect2d


class Pointer:

	def __init__(self):
		self.pos = Vect2d(0, 0)
##This function renew the position of mouse
	def mousePos(self):
		mouseX = (c_int)()
		mouseY = (c_int)()
		SDL_GetMouseState(mouseX, mouseY)
		return Vect2d(mouseX.value, mouseY.value)

##
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
		self.pos.set(self.mousePos())
