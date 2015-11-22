import random

from pico2d import *
i=0
state=0
class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    eat_sound = None
    sound =None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 200, 190
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.xdir = 0
        self.ydir = 0
        self.state = self.RIGHT_STAND
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')
        if Boy.eat_sound == None:
            Boy.eat_sound = load_wav('pickup.wav')
            Boy.eat_sound.set_volume(32)



    def eat(self, ball):
        self.eat_sound.play()
        # fill here
    def sound(self):
        self.sound.play()




    def update(self, frame_time):
        print(i)
        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

        if(self.x<3400and self.x>100 ):
            self.x += (self.xdir * distance)
        else:
            self.x -= (self.xdir * distance)
        if(self.y<1400and self.y>100 ):
            self.y += (self.ydir * distance)
        else:
            self.y -= (self.ydir * distance)

        if self.xdir == -1: self.state = self.LEFT_RUN
        elif self.xdir == 1: self.state = self.RIGHT_RUN
        elif self.xdir == 0:
            if self.state == self.RIGHT_RUN: self.state = self.RIGHT_STAND
            elif self.state == self.LEFT_RUN: self.state = self.LEFT_STAND




    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_event(self, event):
        global state
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.xdir += -1
            elif event.key == SDLK_RIGHT:
                self.xdir += 1
                self.frame+=1
            elif event.key == SDLK_UP: self.ydir += 1
            elif event.key == SDLK_DOWN: self.ydir -= 1



        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.xdir += 1
            elif event.key == SDLK_RIGHT: self.xdir += -1
            elif event.key == SDLK_UP: self.ydir -= 1
            elif event.key == SDLK_DOWN: self.ydir += 1





