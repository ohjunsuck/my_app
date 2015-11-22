import random

from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('KPU_GROUND.png')
        self.bgm = load_music('football.mp3')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        #self.bgm.set_volume(64)
        #self.bgm.repeat_play()
    def set_center_object(self, boy):
        self.center_object = boy
        # fill here
        pass
        # fill here

    def draw(self):
        self.image.draw(400, 30)

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass
    def update(self, frame_time):
        self.window_left = clamp(0,
                                 int(self.center_object.x) - self.canvas_width//2,
                                 self.w- self.canvas_width)
        self.window_bottom = clamp(0,
                                   int(self.center_object.y) - self.canvas_height//2,
                                   self.h- self.canvas_height)
    def get_bb(self):
        return 0,0,799,50

    def __del__(self):
        del self.image
        del self.bgm

