from pico2d import *
import random
import json
import os
import game_framework
import title_state
import shop_state



running = True
startmenu= True
score = 0
sscore =0
time =10
stage=0
Object_List = []
WEAPON_TYPE=1
DDABAL_STATE=0
SHOT_STATE=0
SNIPER_STATE=0
BAJUCA_STATE=0
WEAPON_STATE=0


itemgumeselect=0
buyselect=0
buyselectstate=0
buybig1=0
buybig2=0
buybig3=0
buybig4=0
buybig5=0

# Object Type
BALANCE,BALANCE1, ATTACK, DEFENSE, ITEM =0, 0, 1, 2, 3

class BackGround:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)
    move=0

    def __init__(self, w, h):
        self.image = load_image('./resource/BackGround.png')
        self.image1 = load_image('./resource/구매창.png')
        global char_image1, char_image2, char_image3, char_image4, bg_image, M_Pointer, mx, my, c_i1, c_i2, c_i3, c_i4, System_Sound1
        char_image1 = load_image('./resource/Resume.png')
        char_image2 = load_image('./resource/Shop.png')
        char_image3 = load_image('./resource/To_Title.png')
        char_image4 = load_image('./resource/Exit.png')
        bg_image = load_image('./resource/Menu_BG.png')
        M_Pointer = load_image('./resource/UI_Shot.png')
        System_Sound1 = load_wav('./resource/System01.wav')
        c_i1, c_i2, c_i3, c_i4 = False, False, False, False

        self.speed = 0
        self.left = 0
        self.screen_width = w
        self.screen_height = h


    def draw(self):

        x= int(self.left)
        w= min(self.image.w - x, self.screen_width)


        #self.image.clip_draw_to_origin(x,0,w,self.screen_height,0,0)
        #self.image.clip_draw_to_origin(0,0,self.screen_width-w, self.screen_height,w,0)
        self.image.draw(640-self.left, 320)
        self.image.draw(-660-self.left, 320)
        self.image1.draw(550,605)





    def update(self):
        global turn
        pass



    def First(self):
        self.image = load_image('./resource/BackGround.png')

class User_Interface:
    Time_Slot_image = None
    Play_Time_font = None
    def __init__(self):
        if User_Interface.Play_Time_font == None:
            User_Interface.Play_Time_font = load_font('./resource/H2SA1M.TTF', 80)
        if User_Interface.Time_Slot_image == None:
            User_Interface.Time_Slot_image = load_image('./resource/Time_Slot.png')
        self.gume = load_image('./resource/구매식물.png')
        self.Num_image = load_image('./resource/Number.png')
        self.Num_image1 = load_image('./resource/Number1.png')
        self.Num_image2 = load_image('./resource/Time_Slot.png')
        self.OverTime = load_image('./resource/Number2.png')
        self.Slot = load_image('./resource/Slot.png')
        self.Out_Slot = load_image('./resource/무기인벤토리.png')
        self.Ammo = load_image('./resource/Shop_Ammo.png')
        self.Point = load_image('./resource/포인트.png')
        self.Score = load_image('./resource/스코어.png')
        self.Gume = load_image('./resource/무기구매창.png')
        self.presentgunstate = load_image('./resource/현재총상태.png')
        self.shopplus= load_image('./resource/Shop_Plus.png')
        self.end= load_image('./resource/패배.png')
        self.endsound = load_music('./resource/패배소리.wav')
        self.endsound.set_volume(50)
        self.num_place = 0
        self.num_place1 = 0
        self.num_place2 = 0
        self.num_place3 = 0
        self.num_place4 = 0
        self.num_place5 = 0
        self.itemselect=[0,0,0,0,0]
        self.itemgumeselect=[0,0,0,0,0]
        self.plantx=[210,270,330,390,620,470]
        self.planty=[600,600,600,600,600,600,600,600,600]
        self.plantsize=[0,0,0,0,0,0,0,0]
        self.Play_Time_S = 0
        self.Play_Time_M = 10
        self.Play_Time_H = 0

    def draw_Play_Time(self):
        #self.Time_Slot_image.draw(600, 602)
        self.Play_Time_font.draw(1108, 587, '%2.d:%2.d' % (self.Play_Time_M, self.Play_Time_S), (255,255,255))

    def update(self, frame_time):

        global running
        if self.Play_Time_H <= 0 and self.Play_Time_M <= 0 and self.Play_Time_S <= 1:
            self.end.draw(630,330)
            self.endsound.play()
        if self.Play_Time_H <= 0 and self.Play_Time_M <= 0 and self.Play_Time_S <= 0:
            running =False
        if self.Play_Time_S < 0:
            self.Play_Time_S = 60
            if self.Play_Time_H >= 1:
                self.Play_Time_M = 59
                self.Play_Time_H = 0
            else:
                if self.Play_Time_M > 0:
                    self.Play_Time_M-=1
                else:
                    self.Play_Time_S = 0
        self.Play_Time_S -= frame_time
    def draw_Ammo(self, aim):
        current_time = get_time()
        self.presentgunstate.draw(30,400)
# 1280, 640
        #self.gume.clip_draw(0, 250, 50,50,self.plantx[0], self.planty[0]+self.plantsize[0])
        #self.gume.clip_draw(50, 250, 50,50,self.plantx[1], self.planty[1]+self.plantsize[1])
        #self.gume.clip_draw(250,250, 50,50,self.plantx[2], self.planty[2]+self.plantsize[2])
        #self.gume.clip_draw(300, 250, 50,50,self.plantx[3], self.planty[3]+self.plantsize[3])
        #self.gume.clip_draw(0, 0, 50,50,self.plantx[4], self.planty[4]+self.plantsize[4])
        #self.gume.clip_draw(0, 200, 50,50,self.plantx[5], self.planty[5]+self.plantsize[5])
        self.Slot.clip_draw( 0, 0, 70, 70, 750, 605+(self.itemselect[0]*20))
        self.Slot.clip_draw( 70, 0, 70, 70, 820, 605+(self.itemselect[1]*20))
        self.Slot.clip_draw( 140, 0, 70, 70, 890, 605+(self.itemselect[2]*20))
        self.Slot.clip_draw( 210, 0, 70, 70, 960, 605+(self.itemselect[3]*20))
        self.Slot.clip_draw( 280, 0, 70, 70, 1030, 605+(self.itemselect[4]*20))
        if(WEAPON_TYPE==1):
            for i in 0,1,2,3,4 :
                self.itemselect[i]=0
            self.itemselect[0]=1
        elif(WEAPON_TYPE==2):
            for i in 0,1,2,3,4 :
                self.itemselect[i]=0
            self.itemselect[1]=1
        elif(WEAPON_TYPE==3):
            for i in 0,1,2,3,4 :
                self.itemselect[i]=0
            self.itemselect[2]=1
        elif(WEAPON_TYPE==4):
            for i in 0,1,2,3,4 :
                self.itemselect[i]=0
            self.itemselect[3]=1
        elif(WEAPON_TYPE==5):
            for i in 0,1,2,3,4 :
                self.itemselect[i]=0
            self.itemselect[4]=1

        self.Out_Slot.clip_draw( 0, 0, 90, 70, 300, 605+(self.itemgumeselect[0]*20))
        self.Out_Slot.clip_draw( 87, 0, 90, 70, 390, 605+(self.itemgumeselect[1]*20))
        self.Out_Slot.clip_draw( 175, 0, 95, 70, 475, 605+(self.itemgumeselect[2]*20))
        self.Out_Slot.clip_draw( 280, 0, 90, 70, 567, 605+(self.itemgumeselect[3]*20))
        self.Out_Slot.clip_draw( 380, 0, 100, 70, 657, 605+(self.itemgumeselect[4]*20))



        #self.Out_Slot.draw(460,605)

        if(itemgumeselect==1):
            for i in 0,1,2,3,4 :
                self.itemgumeselect[i]=0
            self.itemgumeselect[0]=1
        elif(itemgumeselect==2):
            for i in 0,1,2,3,4 :
                self.itemgumeselect[i]=0
            self.itemgumeselect[1]=1
        elif(itemgumeselect==3):
            for i in 0,1,2,3,4 :
                self.itemgumeselect[i]=0
            self.itemgumeselect[2]=1
        elif(itemgumeselect==4):
            for i in 0,1,2,3,4 :
                self.itemgumeselect[i]=0
            self.itemgumeselect[3]=1
        elif(itemgumeselect==5):
            for i in 0,1,2,3,4 :
                self.itemgumeselect[i]=0
            self.itemgumeselect[4]=1
        else:
            for i in 0,1,2,3,4 :
                self.itemgumeselect[i]=0


        if(buyselect==1):
           self.Gume.draw(295,470)
        elif(buyselect==2):
           self.Gume.draw(385,470)
        elif(buyselect==3):
           self.Gume.draw(475,470)
        elif(buyselect==4):
           self.Gume.draw(565,470)
        elif(buyselect==5):
           self.Gume.draw(660,470)

        if(buybig1==1):
            self.shopplus.draw(300,545)
        elif(buybig1==2):
            self.shopplus.draw(300,513)
        elif(buybig1==3):
            self.shopplus.draw(300,478)
        elif(buybig1==4):
            self.shopplus.draw(300,441)
        elif(buybig1==5):
            self.shopplus.draw(300,402)

        if(buybig2==1):
            self.shopplus.draw(390,545)
        elif(buybig2==2):
            self.shopplus.draw(390,513)
        elif(buybig2==3):
            self.shopplus.draw(390,478)
        elif(buybig2==4):
            self.shopplus.draw(390,441)
        elif(buybig2==5):
            self.shopplus.draw(390,402)

        if(buybig3==1):
            self.shopplus.draw(480,545)
        elif(buybig3==2):
            self.shopplus.draw(480,513)
        elif(buybig3==3):
            self.shopplus.draw(480,478)
        elif(buybig3==4):
            self.shopplus.draw(480,441)
        elif(buybig3==5):
            self.shopplus.draw(480,402)

        if(buybig4==1):
            self.shopplus.draw(570,545)
        elif(buybig4==2):
            self.shopplus.draw(570,513)
        elif(buybig4==3):
            self.shopplus.draw(570,478)
        elif(buybig4==4):
            self.shopplus.draw(570,441)
        elif(buybig4==5):
            self.shopplus.draw(570,402)

        if(buybig5==1):
            self.shopplus.draw(660,545)
        elif(buybig5==2):
            self.shopplus.draw(660,513)
        elif(buybig5==3):
            self.shopplus.draw(660,478)
        elif(buybig5==4):
            self.shopplus.draw(660,441)
        elif(buybig5==5):
            self.shopplus.draw(660,402)

        self.Score.draw(80,530)
        self.Point.draw(60,575)
        self.Ammo.draw(980,500)
        self.Num_image2.draw(1190,600)



        if aim.ATK%10 == 0:
            self.num_place1 = 0
        elif aim.ATK%10 == 1:
            self.num_place1 = 1
        elif aim.ATK%10 == 2:
            self.num_place1 = 2
        elif aim.ATK%10 == 3:
            self.num_place1 = 3
        elif aim.ATK%10 == 4:
            self.num_place1 = 4
        elif aim.ATK%10 == 5:
            self.num_place1 = 5
        elif aim.ATK%10 == 6:
            self.num_place1 = 6
        elif aim.ATK%10 == 7:
            self.num_place1 = 7
        elif aim.ATK%10 == 8:
            self.num_place1 = 8
        elif aim.ATK%10 == 9:
            self.num_place1 = 9
        self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 110, 480)


        if aim.ATK>=10:
            if aim.ATK%100 >= 0 and aim.ATK%100 <= 9:
                self.num_place1 = 0
            elif aim.ATK%100 >= 10 and aim.ATK%100 <= 19:
                self.num_place1 = 1
            elif aim.ATK%100 >= 20 and aim.ATK%100 <= 29:
                self.num_place1 = 2
            elif aim.ATK%100 >= 30 and aim.ATK%100 <= 39:
                self.num_place1 = 3
            elif aim.ATK%100 >= 40 and aim.ATK%100 <= 49:
                self.num_place1 = 4
            elif aim.ATK%100 >= 50 and aim.ATK%100 <= 59:
                self.num_place1 = 5
            elif aim.ATK%100 >= 60 and aim.ATK%100 <= 69:
                self.num_place1 = 6
            elif aim.ATK%100 >= 70 and aim.ATK%100 <= 79:
                self.num_place1 = 7
            elif aim.ATK%100 >= 80 and aim.ATK%100 <= 89:
                self.num_place1 = 8
            elif aim.ATK%100 >= 90 and aim.ATK%100 <= 99:
                self.num_place1 = 9
            self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 80, 480)

        if aim.Ammo%10 == 0:
            self.num_place1 = 0
        elif aim.Ammo%10 == 1:
            self.num_place1 = 1
        elif aim.Ammo%10 == 2:
            self.num_place1 = 2
        elif aim.Ammo%10 == 3:
            self.num_place1 = 3
        elif aim.Ammo%10 == 4:
            self.num_place1 = 4
        elif aim.Ammo%10 == 5:
            self.num_place1 = 5
        elif aim.Ammo%10 == 6:
            self.num_place1 = 6
        elif aim.Ammo%10 == 7:
            self.num_place1 = 7
        elif aim.Ammo%10 == 8:
            self.num_place1 = 8
        elif aim.Ammo%10 == 9:
            self.num_place1 = 9
        self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 110, 440)


        if aim.Ammo>=10:
            if aim.Ammo%100 >= 0 and aim.Ammo%100 <= 9:
                self.num_place1 = 0
            elif aim.Ammo%100 >= 10 and aim.Ammo%100 <= 19:
                self.num_place1 = 1
            elif aim.Ammo%100 >= 20 and aim.Ammo%100 <= 29:
                self.num_place1 = 2
            elif aim.Ammo%100 >= 30 and aim.Ammo%100 <= 39:
                self.num_place1 = 3
            elif aim.Ammo%100 >= 40 and aim.Ammo%100 <= 49:
                self.num_place1 = 4
            elif aim.Ammo%100 >= 50 and aim.Ammo%100 <= 59:
                self.num_place1 = 5
            elif aim.Ammo%100 >= 60 and aim.Ammo%100 <= 69:
                self.num_place1 = 6
            elif aim.Ammo%100 >= 70 and aim.Ammo%100 <= 79:
                self.num_place1 = 7
            elif aim.Ammo%100 >= 80 and aim.Ammo%100 <= 89:
                self.num_place1 = 8
            elif aim.Ammo%100 >= 90 and aim.Ammo%100 <= 99:
                self.num_place1 = 9
            self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 80, 440)


        if aim.reload_timer%10 == 0:
            self.num_place1 = 0
        elif aim.reload_timer%10 == 1:
            self.num_place1 = 1
        elif aim.reload_timer%10 == 2:
            self.num_place1 = 2
        elif aim.reload_timer%10 == 3:
            self.num_place1 = 3
        elif aim.reload_timer%10 == 4:
            self.num_place1 = 4
        elif aim.reload_timer%10 == 5:
            self.num_place1 = 5
        elif aim.reload_timer%10 == 6:
            self.num_place1 = 6
        elif aim.reload_timer%10 == 7:
            self.num_place1 = 7
        elif aim.reload_timer%10 == 8:
            self.num_place1 = 8
        elif aim.reload_timer%10 == 9:
            self.num_place1 = 9
        self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 110, 400)


        if aim.reload_timer>=10:
            if aim.reload_timer%100 >= 0 and aim.reload_timer%100 <= 9:
                self.num_place1 = 0
            elif aim.reload_timer%100 >= 10 and aim.reload_timer%100 <= 19:
                self.num_place1 = 1
            elif aim.reload_timer%100 >= 20 and aim.reload_timer%100 <= 29:
                self.num_place1 = 2
            elif aim.reload_timer%100 >= 30 and aim.reload_timer%100 <= 39:
                self.num_place1 = 3
            elif aim.reload_timer%100 >= 40 and aim.reload_timer%100 <= 49:
                self.num_place1 = 4
            elif aim.reload_timer%100 >= 50 and aim.reload_timer%100 <= 59:
                self.num_place1 = 5
            elif aim.reload_timer%100 >= 60 and aim.reload_timer%100 <= 69:
                self.num_place1 = 6
            elif aim.reload_timer%100 >= 70 and aim.reload_timer%100 <= 79:
                self.num_place1 = 7
            elif aim.reload_timer%100 >= 80 and aim.reload_timer%100 <= 89:
                self.num_place1 = 8
            elif aim.reload_timer%100 >= 90 and aim.reload_timer%100 <= 99:
                self.num_place1 = 9
            self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 80, 400)


        if aim.speed%10 == 0:
            self.num_place1 = 0
        elif aim.speed%10 == 1:
            self.num_place1 = 1
        elif aim.speed%10 == 2:
            self.num_place1 = 2
        elif aim.speed%10 == 3:
            self.num_place1 = 3
        elif aim.speed%10 == 4:
            self.num_place1 = 4
        elif aim.speed%10 == 5:
            self.num_place1 = 5
        elif aim.speed%10 == 6:
            self.num_place1 = 6
        elif aim.speed%10 == 7:
            self.num_place1 = 7
        elif aim.speed%10 == 8:
            self.num_place1 = 8
        elif aim.speed%10 == 9:
            self.num_place1 = 9
        self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 110, 360)


        if aim.speed>=10:
            if aim.speed%100 >= 0 and aim.speed%100 <= 9:
                self.num_place1 = 0
            elif aim.speed%100 >= 10 and aim.speed%100 <= 19:
                self.num_place1 = 1
            elif aim.speed%100 >= 20 and aim.speed%100 <= 29:
                self.num_place1 = 2
            elif aim.speed%100 >= 30 and aim.speed%100 <= 39:
                self.num_place1 = 3
            elif aim.speed%100 >= 40 and aim.speed%100 <= 49:
                self.num_place1 = 4
            elif aim.speed%100 >= 50 and aim.speed%100 <= 59:
                self.num_place1 = 5
            elif aim.speed%100 >= 60 and aim.speed%100 <= 69:
                self.num_place1 = 6
            elif aim.speed%100 >= 70 and aim.speed%100 <= 79:
                self.num_place1 = 7
            elif aim.speed%100 >= 80 and aim.speed%100 <= 89:
                self.num_place1 = 8
            elif aim.speed%100 >= 90 and aim.speed%100 <= 99:
                self.num_place1 = 9
            self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 80, 360)


        if aim.range%10 == 0:
            self.num_place1 = 0
        elif aim.range%10 == 1:
            self.num_place1 = 1
        elif aim.range%10 == 2:
            self.num_place1 = 2
        elif aim.range%10 == 3:
            self.num_place1 = 3
        elif aim.range%10 == 4:
            self.num_place1 = 4
        elif aim.range%10 == 5:
            self.num_place1 = 5
        elif aim.range%10 == 6:
            self.num_place1 = 6
        elif aim.range%10 == 7:
            self.num_place1 = 7
        elif aim.range%10 == 8:
            self.num_place1 = 8
        elif aim.range%10 == 9:
            self.num_place1 = 9
        self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 110, 320)


        if aim.range>=10:
            if aim.range%100 >= 0 and aim.range%100 <= 9:
                self.num_place1 = 0
            elif aim.range%100 >= 10 and aim.range%100 <= 19:
                self.num_place1 = 1
            elif aim.range%100 >= 20 and aim.range%100 <= 29:
                self.num_place1 = 2
            elif aim.range%100 >= 30 and aim.range%100 <= 39:
                self.num_place1 = 3
            elif aim.range%100 >= 40 and aim.range%100 <= 49:
                self.num_place1 = 4
            elif aim.range%100 >= 50 and aim.range%100 <= 59:
                self.num_place1 = 5
            elif aim.range%100 >= 60 and aim.range%100 <= 69:
                self.num_place1 = 6
            elif aim.range%100 >= 70 and aim.range%100 <= 79:
                self.num_place1 = 7
            elif aim.range%100 >= 80 and aim.range%100 <= 89:
                self.num_place1 = 8
            elif aim.range%100 >= 90 and aim.range%100 <= 99:
                self.num_place1 = 9
            self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 80, 320)


        if sscore%10 == 0:
            self.num_place1 = 0
        elif sscore%10 == 1:
            self.num_place1 = 1
        elif sscore%10 == 2:
            self.num_place1 = 2
        elif sscore%10 == 3:
            self.num_place1 = 3
        elif sscore%10 == 4:
            self.num_place1 = 4
        elif sscore%10 == 5:
            self.num_place1 = 5
        elif sscore%10 == 6:
            self.num_place1 = 6
        elif sscore%10 == 7:
            self.num_place1 = 7
        elif sscore%10 == 8:
            self.num_place1 = 8
        elif sscore%10 == 9:
            self.num_place1 = 9
        self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 250, 520)

        #ten's place
        if sscore>=10:
            if sscore%100 >= 0 and sscore%100 <= 9:
                self.num_place1 = 0
            elif sscore%100 >= 10 and sscore%100 <= 19:
                self.num_place1 = 1
            elif sscore%100 >= 20 and sscore%100 <= 29:
                self.num_place1 = 2
            elif sscore%100 >= 30 and sscore%100 <= 39:
                self.num_place1 = 3
            elif sscore%100 >= 40 and sscore%100 <= 49:
                self.num_place1 = 4
            elif sscore%100 >= 50 and sscore%100 <= 59:
                self.num_place1 = 5
            elif sscore%100 >= 60 and sscore%100 <= 69:
                self.num_place1 = 6
            elif sscore%100 >= 70 and sscore%100 <= 79:
                self.num_place1 = 7
            elif sscore%100 >= 80 and sscore%100 <= 89:
                self.num_place1 = 8
            elif sscore%100 >= 90 and sscore%100 <= 99:
                self.num_place1 = 9
            self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 212, 520)

        if sscore>=100:
            if sscore%1000 >= 0 and sscore%1000 <= 9:
                self.num_place1 = 0
            elif sscore%1000 >= 100 and sscore%1000 <= 199:
                self.num_place1 = 1
            elif sscore%1000 >= 200 and sscore%1000 <= 299:
                self.num_place1 = 2
            elif sscore%1000 >= 300 and sscore%1000 <= 399:
                self.num_place1 = 3
            elif sscore%1000 >= 400 and sscore%1000 <= 499:
                self.num_place1 = 4
            elif sscore%1000 >= 500 and sscore%1000 <= 599:
                self.num_place1 = 5
            elif sscore%1000 >= 600 and sscore%1000 <= 699:
                self.num_place1 = 6
            elif sscore%1000 >= 700 and sscore%1000 <= 799:
                self.num_place1 = 7
            elif sscore%1000 >= 800 and sscore%1000 <= 899:
                self.num_place1 = 8
            elif sscore%1000 >= 900 and sscore%1000 <= 999:
                self.num_place1 = 9
            self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 174, 520)

        if score%10 == 0:
            self.num_place1 = 0
        elif score%10 == 1:
            self.num_place1 = 1
        elif score%10 == 2:
            self.num_place1 = 2
        elif score%10 == 3:
            self.num_place1 = 3
        elif score%10 == 4:
            self.num_place1 = 4
        elif score%10 == 5:
            self.num_place1 = 5
        elif score%10 == 6:
            self.num_place1 = 6
        elif score%10 == 7:
            self.num_place1 = 7
        elif score%10 == 8:
            self.num_place1 = 8
        elif score%10 == 9:
            self.num_place1 = 9
        self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 200, 570)

        #ten's place
        if score>=10:
            if score%100 >= 0 and score%100 <= 9:
                self.num_place1 = 0
            elif score%100 >= 10 and score%100 <= 19:
                self.num_place1 = 1
            elif score%100 >= 20 and score%100 <= 29:
                self.num_place1 = 2
            elif score%100 >= 30 and score%100 <= 39:
                self.num_place1 = 3
            elif score%100 >= 40 and score%100 <= 49:
                self.num_place1 = 4
            elif score%100 >= 50 and score%100 <= 59:
                self.num_place1 = 5
            elif score%100 >= 60 and score%100 <= 69:
                self.num_place1 = 6
            elif score%100 >= 70 and score%100 <= 79:
                self.num_place1 = 7
            elif score%100 >= 80 and score%100 <= 89:
                self.num_place1 = 8
            elif score%100 >= 90 and score%100 <= 99:
                self.num_place1 = 9
            self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 162, 570)

        if score>=100:
          if score%1000 >= 0 and score%1000 <= 9:
              self.num_place1 = 0
          elif score%1000 >= 100 and score%1000 <= 199:
              self.num_place1 = 1
          elif score%1000 >= 200 and score%1000 <= 299:
              self.num_place1 = 2
          elif score%1000 >= 300 and score%1000 <= 399:
              self.num_place1 = 3
          elif score%1000 >= 400 and score%1000 <= 499:
              self.num_place1 = 4
          elif score%1000 >= 500 and score%1000 <= 599:
              self.num_place1 = 5
          elif score%1000 >= 600 and score%1000 <= 699:
              self.num_place1 = 6
          elif score%1000 >= 700 and score%1000 <= 799:
              self.num_place1 = 7
          elif score%1000 >= 800 and score%1000 <= 899:
              self.num_place1 = 8
          elif score%1000 >= 900 and score%1000 <= 999:
              self.num_place1 = 9
          self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 124, 570)


        #unit's place
        if aim.Ammo%10 == 0:
            self.num_place = 0
        elif aim.Ammo%10 == 1:
            self.num_place = 1
        elif aim.Ammo%10 == 2:
            self.num_place = 2
        elif aim.Ammo%10 == 3:
            self.num_place = 3
        elif aim.Ammo%10 == 4:
            self.num_place = 4
        elif aim.Ammo%10 == 5:
            self.num_place = 5
        elif aim.Ammo%10 == 6:
            self.num_place = 6
        elif aim.Ammo%10 == 7:
            self.num_place = 7
        elif aim.Ammo%10 == 8:
            self.num_place = 8
        elif aim.Ammo%10 == 9:
            self.num_place = 9
        self.Num_image.clip_draw(self.num_place * 64, 0, 64, 96, 1220, 500)

        #ten's place
        if aim.Ammo>=10:
            if aim.Ammo%100 >= 0 and aim.Ammo%100 <= 9:
                self.num_place = 0
            elif aim.Ammo%100 >= 10 and aim.Ammo%100 <= 19:
                self.num_place = 1
            elif aim.Ammo%100 >= 20 and aim.Ammo%100 <= 29:
                self.num_place = 2
            elif aim.Ammo%100 >= 30 and aim.Ammo%100 <= 39:
                self.num_place = 3
            elif aim.Ammo%100 >= 40 and aim.Ammo%100 <= 49:
                self.num_place = 4
            elif aim.Ammo%100 >= 50 and aim.Ammo%100 <= 59:
                self.num_place = 5
            elif aim.Ammo%100 >= 60 and aim.Ammo%100 <= 69:
                self.num_place = 6
            elif aim.Ammo%100 >= 70 and aim.Ammo%100 <= 79:
                self.num_place = 7
            elif aim.Ammo%100 >= 80 and aim.Ammo%100 <= 89:
                self.num_place = 8
            elif aim.Ammo%100 >= 90 and aim.Ammo%100 <= 99:
                self.num_place = 9
            self.Num_image.clip_draw(self.num_place * 64, 0, 64, 96, 1162, 500)


    def draw(self, aim):
        self.draw_Ammo(aim)
class Aim:
    HAND_GUN, MACHINE_GUN, SHOT_GUN = 0, 1, 2
    sound =None
    buy_sound = None
    hand_sound1 = None
    hand_sound2 = None
    hand_sound3 = None
    hand_sound4 = None
    hand_sound5 = None
    reload_sound= None
    headshot_sound=None
    #
    hand_attackupgrade=0
    hand_ammoupgrade=0
    hand_reloadupgrade=0
    hand_speedupgrade=0
    hand_rangeupgrade=0
    rifle_attackupgrade=0
    rifle_ammoupgrade=0
    rifle_reloadupgrade=0
    rifle_speedupgrade=0
    rifle_rangeupgrade=0
    sniper_attackupgrade=0
    sniper_ammoupgrade=0
    sniper_reloadupgrade=0
    sniper_speedupgrade=0
    sniper_rangeupgrade=0
    shot_attackupgrade=0
    shot_ammoupgrade=0
    shot_reloadupgrade=0
    shot_speedupgrade=0
    shot_rangeupgrade=0
    bajuca_attackupgrade=0
    bajuca_ammoupgrade=0
    bajuca_reloadupgrade=0
    bajuca_speedupgrade=0
    bajuca_rangeupgrade=0
    def __init__(self):
        self.image = load_image('./resource/Pointer.png')
        self.image2 = load_image('./resource/BPointer-S.png')
        self.image1 = load_image('./resource/Boom.png')
        self.headshot = load_image('./resource/헤드샷.png')
        self.headshotstate=0
        self.x = -100
        self.y = -100
        #self.Weapon = self.HAND_GUN
        self.avail_reload = True
        #기본총 능력치
        if(WEAPON_TYPE==1):
            self.ATK = 5
            self.Ammo = 10
            self.reload_timer = 0
            self.speed=0
            self.range=1
        #
        self.frame=0
        self.attackstate=0
        self.ddabal_time=0
        self.time=0
        #
        if Aim.buy_sound ==None:
            Aim.buy_sound =  load_wav('./resource/Buy.wav')
            Aim.buy_sound.set_volume(50)
        if Aim.headshot_sound == None:
            Aim.headshot_sound = load_wav('./resource/헤드샷소리.wav')
            Aim.headshot_sound.set_volume(50)

        if Aim.hand_sound1 == None:
            Aim.hand_sound1 = load_wav('./resource/Hand_Shot.wav')
            Aim.hand_sound1.set_volume(50)
        if Aim.hand_sound2 == None:
            Aim.hand_sound2 = load_wav('./resource/Rifle_Shot.wav')
            Aim.hand_sound2.set_volume(50)
        if Aim.hand_sound3 == None:
            Aim.hand_sound3 = load_wav('./resource/Sniper_Shot.wav')
            Aim.hand_sound3.set_volume(50)
        if Aim.hand_sound4 == None:
            Aim.hand_sound4 = load_wav('./resource/Shot_Shot.wav')
            Aim.hand_sound4.set_volume(50)
        if Aim.hand_sound5 == None:
            Aim.hand_sound5 = load_wav('./resource/Bazooka_Shot.wav')
            Aim.hand_sound5.set_volume(50)
        if Aim.reload_sound == None:
            Aim.reload_sound = load_wav('./resource/Reloading1.wav')
            Aim.reload_sound.set_volume(50)

    def Attack(self, x, y, Object_List):
        if(WEAPON_TYPE==1):
            if self.Ammo > 0:
                self.attackstate=1
                self.avail_reload = True
                self.reload_timer=0

                for i in range(0, len(Object_List)):
                    if Object_List[len(Object_List)-1-i].Type == BALANCE:
                        if (Object_List[len(Object_List)-1-i].x-18-self.range <= self.x) and \
                                (Object_List[len(Object_List)-1-i].x+22+self.range >= self.x) and \
                                (Object_List[len(Object_List)-1-i].y-24-self.range <= self.y) and \
                                (Object_List[len(Object_List)-1-i].y+7+self.range >= self.y) and \
                                (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                            if (Object_List[len(Object_List)-1-i].x-3-self.range <= self.x) and \
                                (Object_List[len(Object_List)-1-i].x+3+self.range >= self.x) and \
                                (Object_List[len(Object_List)-1-i].y-3-self.range <= self.y) and \
                                (Object_List[len(Object_List)-1-i].y+7+self.range >= self.y) and \
                                (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                                self.headshotstate=1
                                Aim.headshot_sound.play()
                                Object_List[len(Object_List)-1-i].HP -= self.ATK*3
                            Object_List[len(Object_List)-1-i].HP -= self.ATK



                            Check_Die(Object_List[len(Object_List)-1-i], len(Object_List)-1-i)
                            break
                self.Ammo -= 1
            else:
                self.avail_reload = False
        if(WEAPON_TYPE==3):
            if self.Ammo > 0:
                if(self.time>15):
                    self.avail_reload = True
                    self.reload_timer=0
                    for i in range(0, len(Object_List)):
                        if Object_List[len(Object_List)-1-i].Type == BALANCE:
                            if (Object_List[len(Object_List)-1-i].x-18 <= self.x) and \
                                    (Object_List[len(Object_List)-1-i].x+22 >= self.x) and \
                                    (Object_List[len(Object_List)-1-i].y-24 <= self.y) and \
                                    (Object_List[len(Object_List)-1-i].y+7 >= self.y) and \
                                    (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                                if (Object_List[len(Object_List)-1-i].x-3-self.range <= self.x) and \
                                (Object_List[len(Object_List)-1-i].x+3+self.range >= self.x) and \
                                (Object_List[len(Object_List)-1-i].y-3-self.range <= self.y) and \
                                (Object_List[len(Object_List)-1-i].y+7+self.range >= self.y) and \
                                (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                                    self.headshotstate=1
                                    Aim.headshot_sound.play()
                                    Object_List[len(Object_List)-1-i].HP -= self.ATK*3
                                Object_List[len(Object_List)-1-i].HP -= self.ATK
                                self.attackstate=1
                                Check_Die(Object_List[len(Object_List)-1-i], len(Object_List)-1-i)
                                break
                    self.Ammo -= 1
                elif(self.time>20):
                    self.time=0

            else:
                self.avail_reload = False

        if(WEAPON_TYPE==4):
            if self.Ammo > 0:
                self.attackstate=4
                self.avail_reload = True
                self.reload_timer=0

                for i in range(0, len(Object_List)):
                    if Object_List[len(Object_List)-1-i].Type == BALANCE:
                        for i in range(0, len(Object_List)):
                            if (Object_List[len(Object_List)-1-i].x-48 <= self.x) and \
                                    (Object_List[len(Object_List)-1-i].x+52 >= self.x) and \
                                    (Object_List[len(Object_List)-1-i].y-54 <= self.y) and \
                                    (Object_List[len(Object_List)-1-i].y+37 >= self.y) and \
                                    (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                                if (Object_List[len(Object_List)-1-i].x-3-self.range <= self.x) and \
                                (Object_List[len(Object_List)-1-i].x+3+self.range >= self.x) and \
                                (Object_List[len(Object_List)-1-i].y-3-self.range <= self.y) and \
                                (Object_List[len(Object_List)-1-i].y+7+self.range >= self.y) and \
                                (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                                    self.headshotstate=1
                                    Aim.headshot_sound.play()
                                    Object_List[len(Object_List)-1-i].HP -= self.ATK*3
                                Object_List[len(Object_List)-1-i].HP -= (self.ATK)
                                Check_Die(Object_List[len(Object_List)-1-i], len(Object_List)-1-i)
                                break
                self.Ammo -= 3
            else:
                self.avail_reload = False

        if(WEAPON_TYPE==5):
            if self.Ammo > 0:
                self.attackstate=5
                self.avail_reload = True
                self.reload_timer=0
                for i in range(0, len(Object_List)):
                    for i in range(0, len(Object_List)):
                       for i in range(0, len(Object_List)):
                           if Object_List[len(Object_List)-1-i].Type == BALANCE:
                               for i in range(0, len(Object_List)):
                                   if (Object_List[len(Object_List)-1-i].x-218 <= self.x) and \
                                           (Object_List[len(Object_List)-1-i].x+222 >= self.x) and \
                                           (Object_List[len(Object_List)-1-i].y-224 <= self.y) and \
                                           (Object_List[len(Object_List)-1-i].y+207 >= self.y) and \
                                           (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                                       if (Object_List[len(Object_List)-1-i].x-3-self.range <= self.x) and \
                                       (Object_List[len(Object_List)-1-i].x+3+self.range >= self.x) and \
                                       (Object_List[len(Object_List)-1-i].y-3-self.range <= self.y) and \
                                       (Object_List[len(Object_List)-1-i].y+7+self.range >= self.y) and \
                                       (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                                           self.headshotstate=1
                                           Aim.headshot_sound.play()
                                           Object_List[len(Object_List)-1-i].HP -= self.ATK*3
                                       Object_List[len(Object_List)-1-i].HP -= self.ATK
                                       Check_Die(Object_List[len(Object_List)-1-i], len(Object_List)-1-i)
                                       break
                self.Ammo -= 1
            else:
                self.avail_reload = False

        if(WEAPON_TYPE==1 and WEAPON_STATE==1):
            self.ATK = 5
            self.Ammo = 10
            self.reload_timer = 0
            self.speed=1
            self.range=1
        elif(WEAPON_TYPE==2 and WEAPON_STATE==2):
            self.ATK = 5
            self.Ammo = 30
            self.reload_timer = 0
            self.speed=99
            self.range=1
        elif(WEAPON_TYPE==3 and WEAPON_STATE==3):
            self.ATK = 15
            self.Ammo = 5
            self.reload_timer = 0
            self.speed=1
            self.range=1
        elif(WEAPON_TYPE==4 and WEAPON_STATE==4):
            self.ATK = 10
            self.Ammo = 20
            self.reload_timer = 0
            self.speed=1
            self.range=5
        elif(WEAPON_TYPE==3 and WEAPON_STATE==3):
            self.ATK = 20
            self.Ammo = 5
            self.reload_timer = 0
            self.speed=1
            self.range=10
    def Reloading(self):
        if WEAPON_TYPE==1:
            if self.reload_timer == 100:
                self.Ammo = 10+self.hand_ammoupgrade
                self.avail_reload = True
                self.reload_timer = 0+self.hand_reloadupgrade
        elif WEAPON_TYPE==2:
            if self.reload_timer == 100:
                self.Ammo = 50+self.rifle_ammoupgrade
                self.avail_reload = True
                self.reload_timer = 0+self.rifle_reloadupgrade
        elif WEAPON_TYPE==3:
            if self.reload_timer == 100:
                self.Ammo = 5+self.sniper_ammoupgrade
                self.avail_reload = True
                self.reload_timer = 0+self.sniper_reloadupgrade

        elif WEAPON_TYPE==4:
            if self.reload_timer == 100:
                self.Ammo = 30+self.shot_ammoupgrade
                self.avail_reload = True
                self.reload_timer = 0+self.shot_reloadupgrade

        elif WEAPON_TYPE==5:
            if self.reload_timer == 100:
                self.Ammo = 2+self.bajuca_ammoupgrade
                self.avail_reload = True
                self.reload_timer = 0+self.bajuca_reloadupgrade


    def handle_events(self, event):
        global itemgumeselect
        global buyselect
        global buyselectstate
        global buybig1,buybig2,buybig3,buybig4,buybig5
        self.x, self.y = event.x, 640-event.y

        if(self.x>255and self.x<345 and self.y>580and self.y<650):
            itemgumeselect=1
        elif(self.x>345and self.x<435 and self.y>580and self.y<650):
            itemgumeselect=2
        elif(self.x>440and self.x<530 and self.y>580and self.y<650):
            itemgumeselect=3
        elif(self.x>535and self.x<620 and self.y>580and self.y<650):
            itemgumeselect=4
        elif(self.x>620and self.x<720 and self.y>580and self.y<650):
            itemgumeselect=5
        else:
            itemgumeselect=0

        if(self.x>255and self.x<445 and self.y>580and self.y<650 and buyselectstate==1):
            buyselect=1
        elif(self.x>345and self.x<435 and self.y>580and self.y<650 and buyselectstate==2):
            buyselect=2
        elif(self.x>440and self.x<530 and self.y>580and self.y<650and buyselectstate==3):
            buyselect=3
        elif(self.x>535and self.x<620 and self.y>580and self.y<650and buyselectstate==4):
            buyselect=4
        elif(self.x>620and self.x<720 and self.y>580and self.y<650and buyselectstate==5):
            buyselect=5

        #300 545
        if(self.x>295and self.x<305 and self.y>540and self.y<550 and buyselect==1):
            buybig1=1
        elif(self.x>295and self.x<305 and self.y>508and self.y<518 and buyselect==1):
            buybig1=2
        elif(self.x>295and self.x<305 and self.y>473and self.y<483 and buyselect==1):
            buybig1=3
        elif(self.x>295and self.x<305 and self.y>436and self.y<446 and buyselect==1):
            buybig1=4
        elif(self.x>295and self.x<305 and self.y>397and self.y<407 and buyselect==1):
            buybig1=5
        else:
            buybig1=0

        if(self.x>385and self.x<395 and self.y>540and self.y<550 and buyselect==2):
            buybig2=1
        elif(self.x>385and self.x<395 and self.y>508and self.y<518 and buyselect==2):
            buybig2=2
        elif(self.x>385and self.x<395 and self.y>473and self.y<483 and buyselect==2):
            buybig2=3
        elif(self.x>385and self.x<395 and self.y>436and self.y<446 and buyselect==2):
            buybig2=4
        elif(self.x>385and self.x<395 and self.y>397and self.y<407 and buyselect==2):
            buybig2=5
        else:
            buybig2=0

        if(self.x>475and self.x<485 and self.y>540and self.y<550 and buyselect==3):
            buybig3=1
        elif(self.x>475and self.x<485 and self.y>508and self.y<518 and buyselect==3):
            buybig3=2
        elif(self.x>475and self.x<485 and self.y>473and self.y<483 and buyselect==3):
            buybig3=3
        elif(self.x>475and self.x<485 and self.y>436and self.y<446 and buyselect==3):
            buybig3=4
        elif(self.x>475and self.x<485 and self.y>397and self.y<407 and buyselect==3):
            buybig3=5
        else:
            buybig3=0

        if(self.x>565and self.x<575 and self.y>540and self.y<550 and buyselect==4):
            buybig4=1
        elif(self.x>565and self.x<575 and self.y>508and self.y<518 and buyselect==4):
            buybig4=2
        elif(self.x>565and self.x<575 and self.y>473and self.y<483 and buyselect==4):
            buybig4=3
        elif(self.x>565and self.x<575 and self.y>436and self.y<446 and buyselect==4):
            buybig4=4
        elif(self.x>565and self.x<575 and self.y>397and self.y<407 and buyselect==4):
            buybig4=5
        else:
            buybig4=0

        if(self.x>655and self.x<665 and self.y>540and self.y<550 and buyselect==5):
            buybig5=1
        elif(self.x>655and self.x<665 and self.y>508and self.y<518 and buyselect==5):
            buybig5=2
        elif(self.x>655and self.x<665 and self.y>473and self.y<483 and buyselect==5):
            buybig5=3
        elif(self.x>655and self.x<665 and self.y>436and self.y<446 and buyselect==5):
            buybig5=4
        elif(self.x>655and self.x<665 and self.y>397and self.y<407 and buyselect==5):
            buybig5=5
        else:
            buybig5=0




        #self.Out_Slot.clip_draw( 0, 0, 90, 70, 300, 605+(self.itemgumeselect[0]*20))
        #self.Out_Slot.clip_draw( 87, 0, 90, 70, 390, 605+(self.itemgumeselect[1]*20))
        #self.Out_Slot.clip_draw( 175, 0, 95, 70, 475, 605+(self.itemgumeselect[2]*20))
        #self.Out_Slot.clip_draw( 280, 0, 90, 70, 567, 605+(self.itemgumeselect[3]*20))
        #self.Out_Slot.clip_draw( 380, 0, 100, 70, 657, 605+(self.itemgumeselect[4]*20))
        #itemgumeselect=1



    def update(self):
        if(WEAPON_TYPE==1 and WEAPON_STATE==1):
            self.ATK = 5              +self.hand_attackupgrade
            self.Ammo = 10            +self.hand_ammoupgrade
            self.reload_timer = 0     +self.hand_reloadupgrade
            self.speed=1              +self.hand_speedupgrade
            self.range=1              +self.hand_rangeupgrade
        elif(WEAPON_TYPE==2 and WEAPON_STATE==2):
            self.ATK = 3            +self.rifle_attackupgrade
            self.Ammo = 50          +self.rifle_ammoupgrade
            self.reload_timer = 0   +self.rifle_reloadupgrade
            self.speed=99           +self.rifle_speedupgrade
            self.range=1            +self.rifle_rangeupgrade
        elif(WEAPON_TYPE==3 and WEAPON_STATE==3):
            self.ATK = 30          +self.sniper_attackupgrade
            self.Ammo = 5          +self.sniper_ammoupgrade
            self.reload_timer = 0  +self.sniper_reloadupgrade
            self.speed=1           +self.sniper_speedupgrade
            self.range=1           +self.sniper_rangeupgrade
        elif(WEAPON_TYPE==4 and WEAPON_STATE==4):
            self.ATK = 8            +self.shot_attackupgrade
            self.Ammo = 30          +self.shot_ammoupgrade
            self.reload_timer = 0   +self.shot_reloadupgrade
            self.speed=1            +self.shot_speedupgrade
            self.range=5            +self.shot_rangeupgrade
        elif(WEAPON_TYPE==5 and WEAPON_STATE==5):
            self.ATK = 20           +self.bajuca_attackupgrade
            self.Ammo =2            +self.bajuca_ammoupgrade
            self.reload_timer = 0   +self.bajuca_reloadupgrade
            self.speed=1            +self.bajuca_speedupgrade
            self.range=10           +self.bajuca_rangeupgrade


        if self.avail_reload == False:
            self.Reloading()
            self.reload_timer+=1
        if(DDABAL_STATE==1 and WEAPON_TYPE==2):
            self.ddabal_time+=1
            if(self.ddabal_time<2):
                if self.Ammo > 0:
                    Aim.hand_sound2.play()
                    self.attackstate=1
                    self.avail_reload = True
                    self.reload_timer=0

                    for i in range(0, len(Object_List)):
                        if Object_List[len(Object_List)-1-i].Type == BALANCE:
                            if (Object_List[len(Object_List)-1-i].x-18 <= self.x) and \
                                    (Object_List[len(Object_List)-1-i].x+22 >= self.x) and \
                                    (Object_List[len(Object_List)-1-i].y-24 <= self.y) and \
                                    (Object_List[len(Object_List)-1-i].y+7 >= self.y) and \
                                    (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                                if (Object_List[len(Object_List)-1-i].x-3-self.range <= self.x) and \
                                (Object_List[len(Object_List)-1-i].x+3+self.range >= self.x) and \
                                (Object_List[len(Object_List)-1-i].y-3-self.range <= self.y) and \
                                (Object_List[len(Object_List)-1-i].y+7+self.range >= self.y) and \
                                (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                                    self.headshotstate=1
                                    Aim.headshot_sound.play()
                                    Object_List[len(Object_List)-1-i].HP -= self.ATK*3
                                Object_List[len(Object_List)-1-i].HP -= self.ATK
                                Check_Die(Object_List[len(Object_List)-1-i], len(Object_List)-1-i)
                                break
                    self.Ammo -= 1
                else:
                    self.avail_reload = False
            else:
                self.ddabal_time=0
        if(SNIPER_STATE==1):
            self.time+=2
        elif(SNIPER_STATE==0):
            self.time=0








    def draw(self):
        if(WEAPON_TYPE==1 or WEAPON_TYPE==2 or WEAPON_TYPE==4):
            self.image.draw(self.x, self.y)
        elif(WEAPON_TYPE==3 or WEAPON_TYPE==5):
            self.image2.draw(self.x, self.y)
        if(self.attackstate==1):
            self.image1.clip_draw(self.frame*190+25, 380, 150, 200, self.x, self.y)
            self.frame+=1
        if(self.attackstate==4):
            self.image1.clip_draw(self.frame*190+25, 0, 150, 200, self.x, self.y)
            self.frame+=1
        if(self.attackstate==5):
            self.image1.clip_draw(self.frame*190+25, 180, 150, 200, self.x, self.y)
            self.frame+=1
        if(self.frame>10):
            self.frame=0
            self.attackstate=0
            self.headshotstate=0
        if(self.headshotstate==1):
            self.headshot.clip_draw(self.frame*100-5, 0, 100, 75, self.x, self.y+50)
            self.frame+=1


class Barricade:
    Wallx = 300
    Wally = 390
    HP=250
    HP1=500
    HP2=750
    HP3=1000
    HP4=1500
    First_HP=HP
    First_HP1=HP1
    First_HP2=HP2
    First_HP3=HP3
    First_HP4=HP4

    def __init__(self):
        self.image = load_image('./resource/tree01.png')
        self.image1 = load_image('./resource/tree1.png')
        self.image2 = load_image('./resource/tree2.png')
        self.image3 = load_image('./resource/tree3.png')
        self.image4 = load_image('./resource/tree4.png')
        self.HP_image = load_image('./resource/HP.png')
        self.explosion = load_image('./resource/Explosion.png')
        self.end= load_image('./resource/패배.png')
        self.endsound= load_wav('./resource/패배소리.wav')
        self.frame=0
        self.time=0
        self.time1=0
        self.time2=0
        self.time3=0
        self.time4=0

        self.stage=0


    def update(self):
        global running
        global stage
        if(self.time<20):
            if(Barricade.HP>0):
                self.image.clip_draw( 0, 0, 100, 150, 150, 150)
            else:
                self.time+=1
                self.frame+=1
                self.explosion.clip_draw(self.frame * 100, 350, 100, 300, 150,150)
                if(self.frame>4):
                    self.frame=0
        else:
            stage=1
            if(self.time1<20):
                if(stage==1):
                    if(Barricade.HP1>0):
                        self.image1.clip_draw( 0, 0, 100, 150, 150, 150)
                    else:
                        self.time1+=1
                        self.frame+=1
                        self.explosion.clip_draw(self.frame * 100, 350, 100, 300, 150,150)
                        if(self.frame>4):
                            self.frame=0
            else:
                stage=2
                if(self.time2<20):
                    if(stage==2):
                        if(Barricade.HP2>0):
                            self.image2.clip_draw( 0, 0, 100, 150, 150, 150)
                        else:
                            self.time2+=1
                            self.frame+=1
                            self.explosion.clip_draw(self.frame * 100, 350, 100, 300, 150,150)
                            if(self.frame>4):
                                self.frame=0
                else:
                    stage=3
                    if(self.time3<20):
                        if(stage==3):
                            if(Barricade.HP3>0):
                                self.image3.clip_draw( 0, 0, 100, 250, 130, 180)
                            else:
                                self.time3+=1
                                self.frame+=1
                                self.explosion.clip_draw(self.frame * 100, 350, 100, 300, 150,150)
                                if(self.frame>4):
                                    self.frame=0
                    else:
                        stage=4
                        if(self.time4<20):
                            if(stage==4):
                                if(Barricade.HP4>0):
                                    self.image4.clip_draw( 0, 0, 150, 350, 120, 230)
                                else:
                                    self.time4+=1
                                    self.frame+=1
                                    self.explosion.clip_draw(self.frame * 100, 255, 100, 100, 150,150)
                                    self.end.draw(630,330)
                                    self.endsound.play()
                                    if(self.frame>20):
                                        running =False
                                        self.frame=0





    def die(self):
        pass


        #if self.HP < 0:
            #running = False

    def draw(self):
        self.HP_image.clip_draw( (round( (Barricade.HP / Barricade.First_HP * 5) ) ) * 48, 0, 48, 6, 150, 250)
        if(stage==1):
            self.HP_image.clip_draw( (round( (Barricade.HP1 / Barricade.First_HP1 * 5) ) ) * 48, 0, 48, 6, 150, 250)
        elif(stage==2):
            self.HP_image.clip_draw( (round( (Barricade.HP2 / Barricade.First_HP2 * 5) ) ) * 48, 0, 48, 6, 150, 250)
        elif(stage==3):
            self.HP_image.clip_draw( (round( (Barricade.HP3 / Barricade.First_HP3 * 5) ) ) * 48, 0, 48, 6, 150, 250)
        elif(stage==4):
            self.HP_image.clip_draw( (round( (Barricade.HP4 / Barricade.First_HP4 * 5) ) ) * 48, 0, 48, 6, 150, 250)





class Item:
    image = None
    Type = 4

    def __init__(self):
        if Item.image == None:
            Item.image = load_image('./resource/Item.png')
        self.x = 1360
        self.y = random.randint(50, 250)
        self.frame = 0
        self.Move_Timer = 0

    def update(self):
        if self.Move_Timer == 10:
            self.frame = (self.frame+1)%4
            self.x = self.x - 10
            self.Move_Timer = 0
        self.Move_Timer += 1

    def draw(self):
        self.image.clip_draw(self.frame * 72, 0, 72, 72, self.x, self.y)
#----------------------------------------------Enemy---------------------------#


class Balance_Enemy: # Slime

    HP_Upgrade = 0
    ATK_Upgrade = 0
    Type = BALANCE
    image = None
    HP_image = None
    Dead_effect = None
    MOVE, ATTACK, DIE = 2, 1, 0
    diejombiemusic = None
    def __init__(self):
        if Balance_Enemy.diejombiemusic  == None:
            Balance_Enemy.diejombiemusic = load_wav('./resource/좀비죽을때.wav')
            Balance_Enemy.diejombiemusic.set_volume(10)
        if Balance_Enemy.Dead_effect == None:
            Balance_Enemy.Dead_effect = load_image('./resource/Effect_Blood.png')
        if Balance_Enemy.image == None:
            Balance_Enemy.image = load_image('./resource/좀비1.png')
        if Balance_Enemy.HP_image == None:
            Balance_Enemy.HP_image = load_image('./resource/HP.png')
        self.x = random.randint(1350, 1400)
        self.y = random.randint(40, 250)
        self.HP = 25 + Balance_Enemy.HP_Upgrade
        self.First_HP = self.HP
        self.frame = 0
        self.Timer = 0
        self.myindex = None
        self.state = self.MOVE
        self.ATK = 10 + Balance_Enemy.ATK_Upgrade

    def Move(self):
        global turn
        if self.Timer%10 == 0:
            self.frame = (self.frame+1)%4

        if self.Timer == 20:
            self.x = self.x-25
            self.Timer = 0
            if self.x <= (Barricade.Wallx - ( (Barricade.Wally - self.y) / 5.5 ) ):
                self.frame = 0
                self.state = self.ATTACK
                self.Timer = 0


        self.Timer += 1

    def Attack(self):
        if ( self.frame != 0 ) and ( self.Timer % 5 == 0 ):
            self.frame = (self.frame+1) % 4
            Barricade.HP -= self.ATK
            if(stage==1):
                Barricade.HP1 -= self.ATK
            elif(stage==2):
                Barricade.HP2 -= self.ATK
            elif(stage==3):
                Barricade.HP3 -= self.ATK
            elif(stage==4):
                Barricade.HP4 -= self.ATK


        elif self.Timer % 250 == 0:
            self.Timer = 0
            self.frame = (self.frame+1) % 4



        self.Timer += 1

    def Die(self):
        global Object_List
        global score
        global sscore
        Balance_Enemy.diejombiemusic.play()
        if self.frame == 4:
            Delete_Object_in_List(Object_List, self.myindex)
            score+=1
            sscore+=1
        elif self.Timer % 3 == 0:
            self.frame += 1
        self.Timer+=1


    handle_state = {
        MOVE : Move,
        ATTACK : Attack,
        DIE : Die
    }

    def update(self):
        self.handle_state[self.state] (self)
        self.Dead_effect.clip_draw(self.frame * 80 , 0, 80, 80, self.x-3, self.y-2)
    def draw(self):

        self.image.clip_draw(self.frame * 80 +10, 310, 100, 110, self.x, self.y)
        self.HP_image.clip_draw( (round( (self.HP / self.First_HP * 5) ) ) * 48, 0, 48, 6, self.x, self.y+20)

    def __del__(self):
        pass


class Balance_Enemy1: # Slime

    HP_Upgrade = 0
    ATK_Upgrade = 0
    Type = BALANCE1
    image = None
    HP_image = None
    MOVE, ATTACK, DIE = 2, 1, 0

    def __init__(self):
        if Balance_Enemy1.image == None:
            Balance_Enemy1.image = load_image('./resource/좀비2.png')
        if Balance_Enemy1.HP_image == None:
            Balance_Enemy1.HP_image = load_image('./resource/HP.png')
        self.x = random.randint(1350, 1400)
        self.y = random.randint(40, 250)
        self.HP = 50 + Balance_Enemy1.HP_Upgrade
        self.First_HP = self.HP
        self.frame = 0
        self.Timer = 0
        self.myindex = None
        self.state = self.MOVE
        self.ATK = 10 + Balance_Enemy1.ATK_Upgrade

    def Move(self):
        global turn
        if self.Timer%10 == 0:
            self.frame = (self.frame+1)%4

        if self.Timer == 20:
            self.x = self.x-15
            self.Timer = 0
            if self.x <= (Barricade.Wallx - ( (Barricade.Wally - self.y) / 5.5 ) ):
                self.frame = 0
                self.state = self.ATTACK
                self.Timer = 0


        self.Timer += 1

    def Attack(self):
        if ( self.frame != 0 ) and ( self.Timer % 5 == 0 ):
            self.frame = (self.frame+1) % 4
            Barricade.HP -= self.ATK
            if(stage==1):
                Barricade.HP1 -= self.ATK
            elif(stage==2):
                Barricade.HP2 -= self.ATK
            elif(stage==3):
                Barricade.HP3 -= self.ATK
            elif(stage==4):
                Barricade.HP4 -= self.ATK


        elif self.Timer % 250 == 0:
            self.Timer = 0
            self.frame = (self.frame+1) % 4



        self.Timer += 1

    def Die(self):
        global Object_List
        global score
        global sscore
        Balance_Enemy.diejombiemusic.play()
        if self.frame == 4:
            Delete_Object_in_List(Object_List, self.myindex)
            score+=1
            sscore+=2
        elif self.Timer % 3 == 0:
            self.frame += 1
        self.Timer+=1


    handle_state = {
        MOVE : Move,
        ATTACK : Attack,
        DIE : Die
    }

    def update(self):
        self.handle_state[self.state] (self)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 200, 100, 110, self.x, self.y)
        self.HP_image.clip_draw( (round( (self.HP / self.First_HP * 5) ) ) * 48, 0, 48, 6, self.x, self.y+50)

    def __del__(self):
        pass

class Balance_Enemy2: # Slime

    HP_Upgrade = 0
    ATK_Upgrade = 0
    Type = BALANCE1
    image = None
    HP_image = None
    MOVE, ATTACK, DIE = 2, 1, 0
    makesound=None
    attacksound=None
    winsound=None
    winimage=None

    def __init__(self):
        if Balance_Enemy2.image == None:
            Balance_Enemy2.image = load_image('./resource/발록.png')
        if Balance_Enemy2.HP_image == None:
            Balance_Enemy2.HP_image = load_image('./resource/HP.png')
        #
        if Balance_Enemy2.makesound  == None:
            Balance_Enemy2.makesound = load_wav('./resource/발록등장.wav')
        if Balance_Enemy2.attacksound  == None:
            Balance_Enemy2.attacksound = load_wav('./resource/발록공격.wav')

        if Balance_Enemy2.winsound  == None:
            Balance_Enemy2.winsound = load_wav('./resource/승리소리.wav')
        if Balance_Enemy2.winimage  == None:
            Balance_Enemy2.winimage = load_image('./resource/승리.png')
        Balance_Enemy2.makesound.play()
        self.x = random.randint(1350, 1400)
        self.y = random.randint(40, 250)
        self.HP = 5000 + Balance_Enemy1.HP_Upgrade
        self.First_HP = self.HP
        self.frame = 0
        self.Timer = 0
        self.myindex = None
        self.state = self.MOVE
        self.ATK = 100 + Balance_Enemy1.ATK_Upgrade
        self.attackstate=0

    def Move(self):
        global turn
        if self.Timer%10 == 0:
            self.frame = (self.frame+1)%5

        if self.Timer == 20:
            self.x = self.x-60
            self.Timer = 0
            if self.x-200 <= (Barricade.Wallx - ( (Barricade.Wally - self.y) / 5.5 ) ):
                self.frame = 0
                self.state = self.ATTACK
                self.Timer = 0


        self.Timer += 1

    def Attack(self):
        self.attackstate=1
        if ( self.frame != 0 ) and ( self.Timer % 5 == 0 ):
            Balance_Enemy2.attacksound.play()
            self.frame = (self.frame+1) % 4
            Barricade.HP -= self.ATK
            if(stage==1):
                Barricade.HP1 -= self.ATK
            elif(stage==2):
                Barricade.HP2 -= self.ATK
            elif(stage==3):
                Barricade.HP3 -= self.ATK
            elif(stage==4):
                Barricade.HP4 -= self.ATK


        elif self.Timer % 250 == 0:
            self.Timer = 0
            self.frame = (self.frame+1) % 4



        self.Timer += 1

    def Die(self):
        global Object_List
        global score
        global sscore
        global running
        self.attackstate=0

        if self.frame == 30:
            Delete_Object_in_List(Object_List, self.myindex)
            running=False
            #score+=1
            #sscore+=100
        elif self.Timer % 3 == 0:
            Balance_Enemy2.winsound.play()
            self.winimage.draw(600,300)
            self.frame += 1
        self.Timer+=1


    handle_state = {
        MOVE : Move,
        ATTACK : Attack,
        DIE : Die
    }

    def update(self):
        self.handle_state[self.state] (self)

    def draw(self):
        if(self.attackstate==1):
         self.image.clip_draw((self.frame-1) * 250+7, 500, 250, 160, 200, 150)
        self.image.clip_draw(self.frame * 186-5, 2100, 190, 180, self.x, self.y)
        self.HP_image.clip_draw( (round( (self.HP / self.First_HP * 5) ) ) * 48, 0, 48, 6, self.x, self.y+50)

    def __del__(self):
        pass

class Attack_Enemy: # Snake

    Upgrade = 0
    Type = ATTACK
    image = None

    def __init__(self):
        if Attack_Enemy.image == None:
            Attack_Enemy.image = load_image('./resource/LEnemy-Attack.png')
        self.x = 1360
        self.y = random.randint(40, 250)
        self.HP = 100 + Attack_Enemy.Upgrade
        self.frame = 0
        self.Move_Timer = 0

    def Move(self):
        if self.Move_Timer%5 == 0:
            self.frame = (self.frame+1)%4

        if self.Move_Timer == 10:
            if self.frame != 0:
                self.x = self.x-10
            self.Move_Timer = 0
        self.Move_Timer += 1

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 48, 0, 48, 48, self.x, self.y)

    def __del__(self):
        global score
        score += (20 * Attack_Enemy.Upgrade)

class Defense_Enemy: # Golem

    Upgrade = 0
    Type = DEFENSE
    image = None

    def __init__(self):
        if Defense_Enemy.image == None:
            Defense_Enemy.image = load_image('./resource/LEnemy-Defense.png')
        self.x = 1360
        self.y = random.randint(40, 250)
        self.HP = 500 + Defense_Enemy.Upgrade
        self.frame = 0
        self.Move_Timer = 0

    def Move(self):
        if self.Move_Timer == 50:
            self.frame = (self.frame+1)%4
            if self.frame%2 == 1:
                self.x = self.x-15
            else:
                self.x = self.x-10
            self.Move_Timer = 0
        self.Move_Timer += 1

    def Attack(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 105, 0, 105, 105, self.x, self.y)

    def __del__(self):
        global score
        score += (30 * Defense_Enemy.Upgrade)

#----------------------------------------------Enemy---------------------------#
def handle_events(aim, Object_List):
    global running
    global WEAPON_TYPE
    global DDABAL_STATE
    global SHOT_STATE
    global SNIPER_STATE
    global BAJUCA_STATE
    global itemgumeselect
    global buyselect
    global buyselectstate
    global WEAPON_STATE
    global score
    events = get_events()
    for event in events:
        if event.type == SDL_KEYUP:
            WEAPON_STATE=0
        elif event.key == SDLK_1:
            WEAPON_TYPE=1
            WEAPON_STATE=1
        elif event.key == SDLK_2:
            WEAPON_TYPE=2
            WEAPON_STATE=2
        elif event.key == SDLK_3:
            WEAPON_TYPE=3
            WEAPON_STATE=3
        elif event.key == SDLK_4:
            WEAPON_TYPE=4
            WEAPON_STATE=4
        elif event.key == SDLK_5:
            WEAPON_TYPE=5
            WEAPON_STATE=5
        if event.type == SDL_QUIT:
            game_framework.quit()
            running=False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):
            game_framework.push_state(shop_state)
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            #game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION:
            aim.handle_events(event)
        #
        elif event.button == SDL_BUTTON_LEFT and buybig1==1:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.hand_attackupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig1==2:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.hand_ammoupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig1==3:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.hand_reloadupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig1==4:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.hand_speedupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig1==5:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.hand_rangeupgrade+=1
        #
        elif event.button == SDL_BUTTON_LEFT and buybig2==1:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.rifle_attackupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig2==2:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.rifle_ammoupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig2==3:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.rifle_reloadupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig2==4:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.rifle_speedupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig2==5:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.rifle_rangeupgrade+=1
        #
        elif event.button == SDL_BUTTON_LEFT and buybig3==1:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.sniper_attackupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig3==2:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.sniper_ammoupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig3==3:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.sniper_reloadupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig3==4:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.sniper_speedupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig3==5:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.sniper_rangeupgrade+=1
        #
        elif event.button == SDL_BUTTON_LEFT and buybig4==1:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.shot_attackupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig4==2:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.shot_ammoupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig4==3:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.shot_reloadupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig4==4:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.shot_speedupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig4==5:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.shot_rangeupgrade+=1
        #
        elif event.button == SDL_BUTTON_LEFT and buybig5==1:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.bajuca_attackupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig5==2:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.bajuca_ammoupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig5==3:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.bajuca_reloadupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig5==4:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.bajuca_speedupgrade+=1
        elif event.button == SDL_BUTTON_LEFT and buybig5==5:
            if(score>0):
                score-=1
                Aim.buy_sound.play()
                Aim.bajuca_rangeupgrade+=1


        #
        elif event.button == SDL_BUTTON_LEFT and itemgumeselect==1:
            buyselect=1
        elif event.button == SDL_BUTTON_LEFT and itemgumeselect==2:
            buyselect=2
        elif event.button == SDL_BUTTON_LEFT and itemgumeselect==3:
            buyselect=3
        elif event.button == SDL_BUTTON_LEFT and itemgumeselect==4:
            buyselect=4
        elif event.button == SDL_BUTTON_LEFT and itemgumeselect==5:
            buyselect=5
        elif event.button == SDL_BUTTON_RIGHT:
            buyselect=0
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT and itemgumeselect==1:
            buyselectstate=1
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT and WEAPON_TYPE==1:
            aim.Attack(event.x, 640-event.y, Object_List)
            Aim.hand_sound1.play()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT and WEAPON_TYPE==3:
            aim.Attack(event.x, 640-event.y, Object_List)
            SNIPER_STATE=0
            Aim.hand_sound3.play()
        elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT and WEAPON_TYPE==3:
            SNIPER_STATE=1
        elif event.type == SDL_MOUSEBUTTONDOWN and WEAPON_TYPE==2:
            DDABAL_STATE=1
        elif event.type == SDL_MOUSEBUTTONUP and WEAPON_TYPE==2:
            DDABAL_STATE=0
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT and WEAPON_TYPE==4:
            aim.Attack(event.x, 640-event.y, Object_List)
            Aim.hand_sound4.play()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT and WEAPON_TYPE==5:
            aim.Attack(event.x, 640-event.y, Object_List)
            Aim.hand_sound5.play()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            Aim.reload_sound.play()
            Create_Object(BALANCE)
            Create_Object(BALANCE1)
            if aim.avail_reload == True:
                aim.avail_reload = False



def Delete_Object_in_List(List, index):
    del List[index]
    Pull_Index(List, index)

def Pull_Index(List, index):
    for i in range(index, len(List)):
        if List[i].state == List[i].DIE:
            List[i].myindex-=1

def Push_Index(List, index):
    for i in range(index, len(List)):
        if List[i].state == List[i].DIE:
            List[i].myindex+=1

def Check_Die(Object, index):
    if Object.HP <= 0:
        Object.state = Object.DIE
        Object.myindex = index

def Insert_And_Sort(List, Object):
    index = None

    for i in range(len(List)):
        if List[i].y < Object.y:
            index = i
            break

    if index == None:
        List.append(Object)
        index = len(List)
    else:
        List.insert(index, Object)

    Push_Index(List, index)

def Create_Object(Type):
    global Object_List

    Object_Data_File = open('./resource/object_data.txt', 'r')
    Object_Data = json.load( Object_Data_File )
    if Type == BALANCE:
        Object = Balance_Enemy()
        Object.x = Object_Data['BALANCE']['x'] + random.randint(0, 50)
        Object.y = Object_Data['BALANCE']['y'] + random.randint(50, 260)
        Object.HP = Object_Data['BALANCE']['HP'] + Balance_Enemy.HP_Upgrade
        Object.First_HP = Object.HP
        Object.ATK = Object_Data['BALANCE']['ATK'] + Balance_Enemy.ATK_Upgrade
        Insert_And_Sort(Object_List, Object)

    Object_Data_File.close()
def Create_Object1(Type):
    global Object_List1

    Object_Data_File = open('./resource/object_data1.txt', 'r')
    Object_Data = json.load( Object_Data_File )
    if Type == BALANCE1:
        Object = Balance_Enemy()
        Object.x = Object_Data['BALANCE1']['x'] + random.randint(0, 50)
        Object.y = Object_Data['BALANCE1']['y'] + random.randint(50, 260)
        Object.HP = Object_Data['BALANCE1']['HP'] + Balance_Enemy1.HP_Upgrade
        Object.First_HP = Object.HP
        Object.ATK = Object_Data['BALANCE1']['ATK'] + Balance_Enemy1.ATK_Upgrade
        Insert_And_Sort(Object_List1, Object)

    Object_Data_File.close()

class Create_Enemy_Timer():

    Balance_Enemy_Switch, Attack_Enemy_Switch, Defense_Enemy_Switch = False, False, False
    Balance_Enemy_Timer, Attack_Enemy_Switch, Defense_Enemy_Switch = 0, 0, 0
    B_E_Decrease_Time, A_E_Decrease_Time, D_E_Decrease_Time = 0, 0, 0
    B_E_Decrease_Timer, A_E_Decrease_Timer, D_E_Decrease_Timer = 0, 0, 0

    def __init__(self):
        pass

    def Create_Enemy(self, List):
        if self.Balance_Enemy_Switch == True:
            self.Create_Balance_Enemy(List)

    def Decrease_Create_Timer(self):
        if self.Balance_Enemy_Switch == True:
            self.Decrease_Timer_Balance()

    def Create_Balance_Enemy(self, List):
        if self.Balance_Enemy_Timer == 100 - self.B_E_Decrease_Time:
            Create_Object(BALANCE)
            self.Balance_Enemy_Timer = 0
        self.Balance_Enemy_Timer+=1

    def Create_Baricade(self, List):
        if self.Barricade_Timer == 100 - self.B_E_Decrease_Time:
            Create_Object(Barricade)
            self.Barricade_Timer = 0
        self.Barricade_Timer+=1

    def Decrease_Timer_Balance(self):
        if self.B_E_Decrease_Timer == 10000:
            Balance_Enemy.ATK_Upgrade+= 5
            Balance_Enemy.HP_Upgrade+= 100
            Balance_Enemy1.ATK_Upgrade+= 5
            Balance_Enemy1.HP_Upgrade+= 100
            self.B_E_Decrease_Timer = 0
            if self.B_E_Decrease_Time < 900:
                self.B_E_Decrease_Time += 50
        self.B_E_Decrease_Timer+=1

    def update(self, List):
        self.Create_Enemy(List)
        self.Decrease_Create_Timer()

def quit():
    global running
    running = False


def enter():
    pass

def exit():
    pass

def pause():
    pass

def resume():
    pass



TARGET_FPS = 60.0
TARGET_FRAME_TIME = 1.0 / TARGET_FPS
def update():
    global running
    global score
    global sscore
    global time
    global frame_time

   # start= StartMenu(1300,650)
    bg = BackGround(1300,650)
    barricade = Barricade()
    aim = Aim()
    UI = User_Interface()

    create_enemy_timer = Create_Enemy_Timer()
    create_enemy_timer.Balance_Enemy_Switch = True
    Object_List.append(Balance_Enemy())
    hide_cursor()
    running=True


    current_time = get_time()

    while(running):
        if(sscore>100):
            Object_List.append(Balance_Enemy2())
            sscore=0
        time+=1
        if(time>1000):
            Object_List.append(Balance_Enemy1())
        if(time>1001):
            time=0
        handle_events(aim, Object_List)
        clear_canvas()

        bg.draw()
        barricade.draw()
        UI.draw(aim)
        UI.draw_Play_Time()

        for Object in Object_List:
            Object.draw()

        aim.draw()

        for Object in Object_List:
            Object.update()
        frame_time = get_time() - current_time
        frame_rate = 1.0 / frame_time
        print("Frame Rate : %f fps, Frame Time : %f sec, Current Time : %f sec" %(frame_rate,frame_time,current_time))

        current_time += frame_time
        aim.update()
        bg.update()
        UI.update(frame_time)
        barricade.update()
        create_enemy_timer.update(Object_List)




        delay(0.01)

        update_canvas()

    # close_canvas()

def draw():
    pass





