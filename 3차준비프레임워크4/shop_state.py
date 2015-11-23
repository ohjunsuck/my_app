import game_framework
from pico2d import *

name = "ShopState"
running = False


def enter():
    print("샵진입")
    pass


def exit():
    print("나가기")
    pass


def update():
    pass

def draw():
    pass


def handle_events():
    events = get_events()
    for event in events:
      if (event.type, event.key) == (SDL_KEYDOWN, SDLK_o):
          game_framework.pop_state()
    pass

def pause(): pass



def resume(): pass




