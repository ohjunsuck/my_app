import sys
sys.path.append('../LabsAll/Labs')

import random
from pico2d import *

running = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3


    def handle_left_run(self):
        self.x -=5
        self.run_frames +=10
        if self.x <0:
            self.state = self.RIGHT_RUN
            self.x=0
        if self.run_frames ==100:
            self.state = self.LEFT_STAND
            self.stand_frames =0
        pass # fill here

    def handle_left_stand(self):
        self.stand_frames +=25
        if self.stand_frames ==50:
            self.state =self.LEFT_RUN
            self.run_frames =0
        pass # fill here


    def handle_right_run(self):
        self.x +=5
        self.run_frames +=10
        if self.x >800:
            self.state = self.LEFT_RUN
            self.x=800
        if self.run_frames ==100:
            self.state = self.RIGHT_STAND
            self.stand_frames =0
        pass # fill here


    def handle_right_stand(self):
        self.stand_frames +=25
        if self.stand_frames ==50:
            self.state =self.RIGHT_RUN
            self.run_frames =0
        pass # fill here



    #fill here
    handle_state ={
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }


    def update(self):
        self.frame = (self.frame +1) % 8
        self.handle_state[self.state](self)
        pass # fill here



    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def main():

    open_canvas()

    boy = Boy()
    grass = Grass()

    global running
    running = True

    while running:
        handle_events()

        boy.update()

        clear_canvas()
        grass.draw()
        boy.draw()
        update_canvas()

        delay(0.04)

    close_canvas()


if __name__ == '__main__':
    main()