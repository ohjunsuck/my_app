# adjust_run_and_action.py : regulate run speed and action speed as well

import random
import json
from pico2d import *

running = None

class Field:
    def __init__(self):
        self.image = load_image('background30M.bmp')

    def draw(self):
        self.image.draw(480, 136)


class Boy:

    # fill here

    PIXEL_PER_METER = (10.0 / 0.3)    # 10 PIXEL 30 CM
    RUN_SPEED_KMPH = 20.0             # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/ 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)




    image = None

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 7)
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')


    def update(self, frame_time):
        # fill here
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += 1.0
        self.frame = (self.frame +1 ) % 8
        self.x += (self.dir * distance)

        if self.x >960:
            self.dir = -1
            self.x = 960
            self.state = self.LEFT_RUN
            print("Change Time: %f, Total Frames : %d" %
                  (get_time(), self.total_frames))
        elif self.x< 0:
            self.dir =1
            self.x =0
            self.state = self.RIGHT_RUN
            print("Change Time : %f, Total Frames : %d" %
                  (get_time(), self.total_frames))

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def handle_events(frame_time):
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



current_time = 0.0


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def main():

    open_canvas(960, 272)

    global running
    global current_time


    hero = Boy()
    field = Field()

    running = True
    current_time = get_time()

    while running:

        # Game Logic
        # fill here
        frame_time = get_frame_time()
        handle_events(frame_time)
        hero.update(frame_time)


        # Game Rendering
        clear_canvas()
        field.draw()
        hero.draw()
        update_canvas()

        delay(0.07)


    close_canvas()


if __name__ == '__main__':
    main()