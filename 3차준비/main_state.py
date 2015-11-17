import random
import json
import os
import Project

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None
jombie = None

class Grass:
    def __init__(self):
      pass

    def draw(self):
        global i,j
        pass


        i
    def handle_events(self):
        pass

    def update(self):
       pass


class Boy:
    def __init__(self):
     pass


    def update(self):
       pass


    def draw(self):
       pass

class Jombie:
    image =None
    def __init__(self):
        pass

    def update(self):
       pass


    def draw(self):
      pass


def enter():
    global boy,grass

    boy= Boy()
    grass = Grass()

    pass


def exit():
    global boy, grass
    del(boy)
    del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    pass

def update():
    boy.update()
    jombie.update()
    grass.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    jombie.draw()
    update_canvas()
    pass





