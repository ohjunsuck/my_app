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
        self.plantx=[130,190,250,310,370,430,620,730]
        self.planty=[565,565,565,565,565,565,565,580]
        self.plantsize=[0,0,0,0,0,0,0,0]
        self.savex=[0,0,0,0,0,0,0,0,0,0]
        self.savey=[0,0,0,0,0,0,0,0,0,0]
        self.cnt=0
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
        self.plant.clip_draw(0, 250, 50,50,self.plantx[0], self.planty[0]+self.plantsize[0])
        self.plant.clip_draw(50, 250, 50,50,self.plantx[1], self.planty[1]+self.plantsize[1])
        self.plant.clip_draw(250,250, 50,50,self.plantx[2], self.planty[2]+self.plantsize[2])
        self.plant.clip_draw(300, 250, 50,50,self.plantx[3], self.planty[3]+self.plantsize[3])
        self.plant.clip_draw(0, 0, 50,50,self.plantx[4], self.planty[4]+self.plantsize[4])
        self.plant.clip_draw(0, 200, 50,50,self.plantx[5], self.planty[5]+self.plantsize[5])
        self.erase.clip_draw(0, 0, 95,58 ,self.plantx[6], self.planty[6]+self.plantsize[6])
        self.menu.clip_draw(0, 0, 110, 26,self.plantx[7], self.planty[7]+self.plantsize[7])

        if(self.state!=0 and self.state!=6 and self.state!=7 and self.state!=8):
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



        if(self.click==1):
         for i in range(0,9):
             for j in range(0,5):
                 if(self.savex[i]!=0 and self.savey[j]!=0):
                    self.myplant.clip_draw(100, 180, 100, 100, self.savex[i]-30, self.savey[j])
        if(self.click==2):
            self.myplant.clip_draw(0, 180, 100, 100, 400, 400)

    def handle_events(self):
        pass

    def update(self):
        global x, y
        events = get_events()
        for event in events:
         if event.type == SDL_MOUSEMOTION:
              x, y =event.x, 600 - event.y


            # for i in range(0,9):
              #  for j in range(0,5):
              #   self.plantspace.draw(60+80*(i),80+100*(j))
        for i in range(1,8):
             if( event.type == SDL_MOUSEBUTTONDOWN and self.state==i):
                self.click=i
                for i in range(-1,9):
                    for j in range(0,5):
                         if((40+80*i<x and x<100+80*(i) ) and (100*j-40<y and 40+100*(j+1)>y)):
                             self.savex[i]=80*(i+1)
                             self.savey[j]=(j+1)*100
        print(x)


        for i in range(0,8):
            if(x>self.plantx[i]-25 and x<self.plantx[i]+25 and y>self.planty[i]-25 and y<self.planty[i]+25):
              self.state=i+1



        for i in range(0,8):
            if(self.plantsize[i]<10and self.state==i+1):
               self.plantsize[i]+=10
            elif(self.plantsize[i]>0 and self.state!=i+1):
                self.plantsize[i]-=10













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





