import random
from pico2d import *
from math import *

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
            self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y= random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame +1) % 8
        self.x += -5+random.randint(-20,40)

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

xx=0
yy=0
x=0
y=0
xxx=0
yyy=0
frame = 0
radius=300
angle=0
i=0
j=0
def handle_events():
    global running
    global key_down_right
    global key_down_left
    global key_down_up
    global key_down_down

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                key_down_right = True

            if event.key == SDLK_LEFT:
                key_down_left = True

            if event.key == SDLK_UP:
                key_down_up = True

            if event.key == SDLK_DOWN:
                key_down_down = True

            if event.key == SDLK_ESCAPE:
                running = False
        if event.type == SDL_KEYUP:
              if event.key == SDLK_RIGHT:
                key_down_right = False

              if event.key == SDLK_LEFT:
                key_down_left = False

              if event.key == SDLK_UP:
                key_down_up = False

              if event.key == SDLK_DOWN:
                key_down_down = False

              if event.key == SDLK_ESCAPE:
                running = False


# initialization code
open_canvas()

character = load_image('run_animation.png')
character1 = load_image('run_animation.png')
character2 = load_image('run_animation.png')
boy1 = Boy()
boy2 = Boy()
boy3 = Boy()
boy4 = Boy()
boy5 = Boy()
boy6 = Boy()
boy7 = Boy()
boy8 = Boy()
boy9 = Boy()
boy10 = Boy()
team=[boy1,boy2,boy3,boy4,boy5,boy6,boy7,boy8,boy9,boy10]
team=[Boy()]*11
team=[Boy()for i in range(11)]
grass = Grass()

key_down_up = False
key_down_down = False
key_down_right = False
key_down_left = False

running = True;
# game main loop code
while running:
    handle_events()


    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()
    character.clip_draw(frame * 100, 0, 100, 100, xx, yy)
    character1.clip_draw(frame * 100, 0, 100, 100, i+400, j+400)
    character2.clip_draw(frame * 100, 0, 100, 100, xxx, yyy+600)
    for boy in team:
        boy.draw()
    update_canvas()

    frame=random.randint(0,7)
    delay(0.05)
    handle_events()
    if key_down_left == True:
        xx -= 5
    if key_down_right == True:
        xx += 5
    if key_down_down == True:
        yy -= 5
    if key_down_up == True:
        yy += 5

    for i in range(1,100):
       for j in range(1,100):
         j=radius*cos(angle)
         i=radius*sin(angle)

    if xxx<700:
        xxx+=10
        if(xxx>680):
            xxx-=10
            yyy-=10


    angle+=0.05;


# finalization code
close_canvas()