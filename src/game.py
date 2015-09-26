
import sys
import ctypes

from OpenGL import GL, GLU
from sdl2 import *



class Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = True
        self.event = SDL_Event()

    def init(self):
        SDL_Init(SDL_INIT_EVERYTHING)

        self.window = SDL_CreateWindow(b"p",
                                    SDL_WINDOWPOS_CENTERED,
                                    SDL_WINDOWPOS_CENTERED,
                                    self.width, self.height,
                                    SDL_WINDOW_OPENGL)    

        self.selfcontext = SDL_GL_CreateContext(self.window)

        if not self.window:
            print(SDL_GetError())
            return -1

        GL.glMatrixMode(GL.GL_PROJECTION | GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        GL.glOrtho(0, self.width, 0, self.height, 0, 1)

        GL.glClearColor(0.5, 0.47, 0.78, 1)

        self.rota = 0



    def render(self):
        #prueba inicial, dibuja el triangulo
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        x = self.width/2
        y = self.height/2
        

        GL.glPushMatrix()
        GL.glTranslatef(x, y, 0.0)
        GL.glRotatef(self.rota, 0.0, 0.0, 1.0)
        GL.glBegin(GL.GL_TRIANGLES)
        GL.glColor3f(1.0, 0.0, 0.0)
        GL.glVertex2f(0.0, 90.0)
        GL.glColor3f(0.0, 1.0, 0.0)
        GL.glVertex2f(90.0, -90.0)
        GL.glColor3f(0.0, 0.0, 1.0)
        GL.glVertex2f(-90.0, -90.0)
        GL.glEnd()
        GL.glPopMatrix()

        self.rota += 0.05
        SDL_GL_SwapWindow(self.window)


    def eventHandle(self):
        while SDL_PollEvent(ctypes.byref(self.event)) != 0:
            if self.event.type == SDL_QUIT:
                self.running = False
                break

            if self.event.type == SDL_KEYDOWN:
                if self.event.key.keysym.scancode == SDL_SCANCODE_ESCAPE:
                    self.running = False
                    break


    def quit(self):
        SDL_GL_DeleteContext(self.context)
        SDL_DestroyWindow(self.window)
        SDL_Quit()
