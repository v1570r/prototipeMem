
import sys
import ctypes

from OpenGL import GL, GLU
from sdl2 import *

from pointer import Pointer
from mob_generator import MobGenerator

class Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = True
        self.event = SDL_Event()
        self.pointer = Pointer()
        self.mobs = MobGenerator()

    def init(self):
        SDL_Init(SDL_INIT_EVERYTHING)

        self.window = SDL_CreateWindow(b"prototipe mem",
                                    SDL_WINDOWPOS_CENTERED,
                                    SDL_WINDOWPOS_CENTERED,
                                    self.width, self.height,
                                    SDL_WINDOW_OPENGL)    

        self.context = SDL_GL_CreateContext(self.window)

        if not self.window:
            print(SDL_GetError())
            return -1

        GL.glMatrixMode(GL.GL_PROJECTION | GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        GL.glOrtho(0, self.width, self.height, 0, 0, 1)

        GL.glClearColor(0.5, 0.47, 0.78, 1)

        self.mobs.generate()



    def render(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        self.pointer.render()
        self.mobs.render()

        SDL_GL_SwapWindow(self.window)
        SDL_Delay(10)

    def update(self):
        self.pointer.update()
        self.mobs.update()


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
