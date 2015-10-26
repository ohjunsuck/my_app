import random
import json
import os

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
        self.gumex, self.gumey, self.gumesize = 310,565,0
        self.changstate=0
        self.plantx, self.planty, self.plantsize= 130,565,0
        self.plantx1, self.planty1, self.plantsize1= 190,565,0
        self.plantx2, self.planty2, self.plantsize2= 250,565,0
        self.plantx3, self.planty3, self.plantsize3= 310,565,0
        self.plantx4, self.planty4, self.plantsize4= 370,565,0
        self.plantx5, self.planty5, self.plantsize5= 430,565,0
        self.plantx6, self.planty6, self.plantsize6= 620,565,0
        self.plantx7, self.planty7, self.plantsize7= 730,580,0
        self.click=0
        self.state=0
        self.image = load_image('맵.png')
        self.gume = load_image('구매창.png')
        self.plant = load_image('구매식물.png')
        self.myplant = load_image('타워.png')
        self.plantspace = load_image('식물자리.png')
        self.erase = load_image('파괴아이콘.png')
        self.menu = load_image('메뉴창.png')
        self.jumsu = load_image('숫자.png')



    def draw(self):
        global i,j
        self.image.draw(400, 300)
        self.gume.clip_draw(0,0,570,69,self.gumex-30,self.gumey)
        self.plant.clip_draw(0, 250, 50,50,self.plantx, self.planty+self.plantsize)
        self.plant.clip_draw(50, 250, 50,50,self.plantx1, self.planty1+self.plantsize1)
        self.plant.clip_draw(250,250, 50,50,self.plantx2, self.planty2+self.plantsize2)
        self.plant.clip_draw(300, 250, 50,50,self.plantx3, self.planty3+self.plantsize3)
        self.plant.clip_draw(0, 0, 50,50,self.plantx4, self.planty4+self.plantsize4)
        self.plant.clip_draw(0, 200, 50,50,self.plantx5, self.planty5+self.plantsize5)
        self.erase.clip_draw(0, 0, 95,58 ,self.plantx6, self.planty6+self.plantsize6)
        self.menu.clip_draw(0, 0, 110, 26,self.plantx7, self.planty7+self.plantsize7)

        if(self.state!=0 and self.state!=6 and self.state!=7):
            for i in range(0,9):
                for j in range(0,5):
                 self.plantspace.draw(60+80*(i),80+100*(j))


        if(self.state==1):
            self.myplant.clip_draw(100, 180, 100, 100, x, y)
        elif(self.state==2):
            self.myplant.clip_draw(0, 180, 100, 100, x, y)
        elif(self.state==3):
            self.myplant.clip_draw(300, 180, 100, 100, x, y)
        elif(self.state==4):
            self.myplant.clip_draw(350, 0, 100, 100, x, y)
        elif(self.state==5):
            self.myplant.clip_draw(400, 180, 100, 100, x, y)




    def handle_events(self):
        global running
        global x, y
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            if event.type == SDL_MOUSEMOTION:
                x, y =event.x, 600 - event.y

    def update(self):
        global x, y
        events = get_events()
        for event in events:
          if event.type == SDL_MOUSEMOTION:
             x, y =event.x, 600 - event.y
          if(x>self.plantx-25 and x<self.plantx+25 and y>self.planty-25 and y<self.planty+25):
               self.state=1
          elif(x>self.plantx1-25 and x<self.plantx1+25 and y>self.planty1-25 and y<self.planty1+25):
               self.state=2
          elif(x>self.plantx2-25 and x<self.plantx2+25 and y>self.planty2-25 and y<self.planty2+25):
               self.state=3
          elif(x>self.plantx3-25 and x<self.plantx3+25 and y>self.planty3-25 and y<self.planty3+25):
               self.state=4
          elif(x>self.plantx4-25 and x<self.plantx4+25 and y>self.planty4-25 and y<self.planty4+25):
               self.state=5
          elif(x>self.plantx5-25 and x<self.plantx5+25 and y>self.planty5-25 and y<self.planty5+25):
               self.state=0
          elif(x>self.plantx6-25 and x<self.plantx6+25 and y>self.planty6-25 and y<self.planty6+25):
               self.state=6
          elif(x>self.plantx7-25 and x<self.plantx7+25 and y>self.planty7-25 and y<self.planty7+25):
               self.state=7
          else:
             self.plantsize=0
             self.plantsize1=0
             self.plantsize2=0
             self.plantsize3=0
             self.plantsize4=0
             self.plantsize5=0
             self.plantsize6=0
             self.plantsize7=0


        if(self.plantsize<10and self.state==1):
               self.plantsize+=10
        elif(self.plantsize1<10and self.state==2):
               self.plantsize1+=10
        elif(self.plantsize2<10and self.state==3):
               self.plantsize2+=10
        elif(self.plantsize3<10and self.state==4):
               self.plantsize3+=10
        elif(self.plantsize4<10and self.state==5):
               self.plantsize4+=10
        elif(self.plantsize6<10and self.state==6):
               self.plantsize6+=10
        elif(self.plantsize7<10and self.state==7):
               self.plantsize7+=10















class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Jombie:
    image =None
    def __init__(self):
        self.x, self.y = 790, random.randint(50,550)
        self.frame = 0
        self.jombie1 = load_image('좀비1.png')
        self.dir = 1
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= self.dir*0.3

    def draw(self):
        self.jombie1.clip_draw(self.frame * 95, 370, 100, 110, self.x, self.y)


def enter():
    global boy,grass,jombie

    boy= Boy()
    grass = Grass()
    jombie = Jombie()
    pass


def exit():
    global boy, grass, jombie
    del(boy)
    del(grass)
    del(jombie)
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





