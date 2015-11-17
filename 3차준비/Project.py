from pico2d import *
import random
import json
import game_framework
import title_state

running = True
score = 0
time =10
stage=0
Object_List = []

# Object Type
BALANCE, ATTACK, DEFENSE, ITEM = 0, 1, 2, 3
class StartMenu:
    def __init__(self , w, h):
        pass
        #self.image = load_image('./resouce/타이틀.png')
    def draw(self):
        self.image.draw(640,320)

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
    def __init__(self):
        self.gume = load_image('./resource/구매식물.png')
        self.Num_image = load_image('./resource/Number.png')
        self.Num_image1 = load_image('./resource/Number1.png')
        self.Num_image2 = load_image('./resource/Time_Slot.png')
        self.OverTime = load_image('./resource/Number2.png')
        self.Slot = load_image('./resource/Slot.png')
        self.Out_Slot = load_image('./resource/Out_Slot.png')
        self.num_place = 0
        self.num_place1 = 0
        self.num_place2 = 0
        self.num_place3 = 0
        self.num_place4 = 0
        self.plantx=[210,270,330,390,620,470]
        self.planty=[600,600,600,600,600,600,600,600,600]
        self.plantsize=[0,0,0,0,0,0,0,0]
    def draw_Ammo(self, aim):
# 1280, 640
        self.gume.clip_draw(0, 250, 50,50,self.plantx[0], self.planty[0]+self.plantsize[0])
        self.gume.clip_draw(50, 250, 50,50,self.plantx[1], self.planty[1]+self.plantsize[1])
        self.gume.clip_draw(250,250, 50,50,self.plantx[2], self.planty[2]+self.plantsize[2])
        self.gume.clip_draw(300, 250, 50,50,self.plantx[3], self.planty[3]+self.plantsize[3])
        self.gume.clip_draw(0, 0, 50,50,self.plantx[4], self.planty[4]+self.plantsize[4])
        self.gume.clip_draw(0, 200, 50,50,self.plantx[5], self.planty[5]+self.plantsize[5])


        self.Slot.draw(1010,600)
        self.Out_Slot.draw(590,600)
        self.Num_image2.draw(1190,600)
        if time%10 == 0:
            self.num_place1 = 0
        elif time%10 == 1:
            self.num_place1 = 1
        elif time%10 == 2:
            self.num_place1 = 2
        elif time%10 == 3:
            self.num_place1 = 3
        elif time%10 == 4:
            self.num_place1 = 4
        elif time%10 == 5:
            self.num_place1 = 5
        elif time%10 == 6:
            self.num_place1 = 6
        elif time%10 == 7:
            self.num_place1 = 7
        elif time%10 == 8:
            self.num_place1 = 8
        elif time%10 == 9:
            self.num_place1 = 9
        self.OverTime.clip_draw(self.num_place1 * 32, 0, 32, 40, 1150, 600)
        self.OverTime.clip_draw(self.num_place1 * 32, 0, 32, 40, 1200, 600)
        self.OverTime.clip_draw(self.num_place1 * 32, 0, 32, 40, 1230, 600)

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
        self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 120, 570)

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
            self.Num_image1.clip_draw(self.num_place1 * 32, 0, 32, 40, 82, 570)


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

    def __init__(self):
        self.image = load_image('./resource/Pointer.png')
        self.x = -100
        self.y = -100
        self.ATK = 50
        self.Ammo = 10
        self.Weapon = self.HAND_GUN
        self.avail_reload = True
        self.reload_timer = 0

    def Attack(self, x, y, Object_List):
        if self.Ammo > 0:
            self.avail_reload = True
            self.reload_timer=0

            for i in range(0, len(Object_List)):
                if Object_List[len(Object_List)-1-i].Type == BALANCE:
                    if (Object_List[len(Object_List)-1-i].x-18 <= self.x) and \
                            (Object_List[len(Object_List)-1-i].x+22 >= self.x) and \
                            (Object_List[len(Object_List)-1-i].y-24 <= self.y) and \
                            (Object_List[len(Object_List)-1-i].y+7 >= self.y) and \
                            (Object_List[len(Object_List)-1-i].state != Object_List[len(Object_List)-1-i].DIE):
                        Object_List[len(Object_List)-1-i].HP -= self.ATK
                        Check_Die(Object_List[len(Object_List)-1-i], len(Object_List)-1-i)
                        break
            self.Ammo -= 1
        else:
            self.avail_reload = False

    def Reloading(self):
        if self.Weapon == self.HAND_GUN:
            if self.reload_timer == 100:
                self.Ammo = 10
                self.avail_reload = True
                self.reload_timer = 0

    def handle_events(self, event):
        self.x, self.y = event.x, 640-event.y

    def update(self):
        if self.avail_reload == False:
            self.Reloading()
            self.reload_timer+=1
    def draw(self):
        self.image.draw(self.x, self.y)

class Barricade:
    Wallx = 300
    Wally = 390
    HP=25
    HP1=50
    HP2=75
    HP3=100
    HP4=125
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
                                    if(self.frame>4):
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
    MOVE, ATTACK, DIE = 2, 1, 0

    def __init__(self):
        if Balance_Enemy.image == None:
            Balance_Enemy.image = load_image('./resource/좀비1.png')
        if Balance_Enemy.HP_image == None:
            Balance_Enemy.HP_image = load_image('./resource/HP.png')
        self.x = random.randint(1350, 1400)
        self.y = random.randint(40, 250)
        self.HP = 250 + Balance_Enemy.HP_Upgrade
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

        if self.frame == 4:
            Delete_Object_in_List(Object_List, self.myindex)
            score+=1
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
        self.image.clip_draw(self.frame * 80 +10, 310, 100, 110, self.x, self.y)
        self.HP_image.clip_draw( (round( (self.HP / self.First_HP * 5) ) ) * 48, 0, 48, 6, self.x, self.y+20)

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

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            aim.handle_events(event)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            aim.Attack(event.x, 640-event.y, Object_List)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            Create_Object(BALANCE)
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

    Object_Data_File = open('object_data.txt', 'r')
    Object_Data = json.load( Object_Data_File )
    if Type == BALANCE:
        Object = Balance_Enemy()
        Object.x = Object_Data['BALANCE']['x'] + random.randint(0, 50)
        Object.y = Object_Data['BALANCE']['y'] + random.randint(0, 210)
        Object.HP = Object_Data['BALANCE']['HP'] + Balance_Enemy.HP_Upgrade
        Object.First_HP = Object.HP
        Object.ATK = Object_Data['BALANCE']['ATK'] + Balance_Enemy.ATK_Upgrade
        Insert_And_Sort(Object_List, Object)

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
            self.B_E_Decrease_Timer = 0
            if self.B_E_Decrease_Time < 900:
                self.B_E_Decrease_Time += 50
        self.B_E_Decrease_Timer+=1

    def update(self, List):
        self.Create_Enemy(List)
        self.Decrease_Create_Timer()


def main():
    open_canvas(1280, 640)
    global running
    global score
    global time

    start= StartMenu(1300,650)
    bg = BackGround(1300,650)
    barricade = Barricade()
    aim = Aim()
    UI = User_Interface()

    create_enemy_timer = Create_Enemy_Timer()
    create_enemy_timer.Balance_Enemy_Switch = True
    Object_List.append(Balance_Enemy())

    hide_cursor()
    running=True

    while(running):
        time+=1
        handle_events(aim, Object_List)
        clear_canvas()

        bg.draw()
        barricade.draw()
        UI.draw(aim)
        for Object in Object_List:
            Object.draw()

        aim.draw()

        for Object in Object_List:
            Object.update()

        aim.update()
        bg.update()
        barricade.update()
        create_enemy_timer.update(Object_List)
        delay(0.01)

        update_canvas()

    close_canvas()

if __name__ == '__main__':
    main()
