import random

from pico2d import *

class Grass:
    def __init__(self):
        self.x,self.y =0,0
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def get_bb(self):
        return self.x-20, self.y-20, self.x+20, self.y +20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



    # fill here

