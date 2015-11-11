from pico2d import *
import random
import json

running = True
score =0
Object_List = []

BALANCE, ATTACK, DEFENSE, ITEM =0,1,2,3

class BackGround:
    def __init__(self):
        self.image = load_image('BackGround.png')
        self.image1 = load_image('구매창.png')

    def draw(self):
        self.image.draw(640,320)
        self.image1.draw(550,605)

    def First(self):
        self.image = load_image('BackGround.png')

class User_Interface:
    def __init__(self):
        self.Num_image= load_image('Number.png')
        self.num_place=0

    def draw_Ammo(self, aim):

        if aim.Ammo%10 ==0:
            self.num_place=0
        elif aim.Ammo%10 == 1:
            self.num_place=1
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
        self.Num_image.clip_draw(self.num_place * 64, 0, 64, 96, 1220, 570)


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
            self.Num_image.clip_draw(self.num_place * 64, 0, 64, 96, 1162, 570)

    def draw(self, aim):
        self.draw_Ammo(aim)

class Aim:
    HAND_GUN, MACHINE_GUN, SHOT_GUN = 0,1,2

    def __init__(self):
        self.image = load_image('Pointer.png')
        self.x =-100
        self.y =-100
        self.ATK = 50
        self.Ammo =10
        self.Weapon = self.HAND_GUN
        self.avail_reload =True
        self.reload_timer=0

    def Attack(self, x, y, Object_List):
        if self.Ammo > 0:
            self.avail_reload = True
            self.reload_timer=0

            for i in range(0, len(Object_List)):
                if Object_List[len(Object_List)-1-i].Type == BALANCE:
                    if (Object_List[len(Object_List)-1-i].x-18 <= self.x)and \
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
                self.reload_timer =0

    def handle_events(self, event):
        self.x, self.y = event.x, 640-event.y

    def update(self):
        if self.avail_reload == False:
            self.Reloading()
            self.reload_timer+=1
    def draw(self):
        self.image.draw(self.x, self.y)

class Barricade:
    Wallx =300
    Wally =390
    HP = 2500

    def __init__(self):
        self.image = load_image('타워1.png')

    def update(self):
        global running

    def draw(self):
        self.image.draw(150,150)

class Item:
    image = None
    Type = 4

    def __init__(self):
        if Item.image == None:
            Item.image = load_image('Item.png')
        self.x = 1360
        self.y = random.randint(50,250)
        self.frame = 0
        self.Move_Timer =0

    def update(self):
        if self.Move_Timer == 10:
            self.frame = (self.frame+1)%4
            self.x = self.x -10
            self.Move_Timer = 0
        self.Move_Timer +=1

    def draw(self):
        self.image.clip_draw(self.frame * 72, 0 , 72 , 72 , self.x ,self.y)

class Balance_Enemy:

    HP_Upgrade =0
    ATK_Upgrade =0
    Type = BALANCE
    image = None
    HP_image = None
    MOVE, ATTACK, DIE =2,1,0

    def __init__(self):
        if Balance_Enemy.image == None:
            Balance_Enemy.image = load_image('좀비1.png')
        if Balance_Enemy.HP_image == None:
            Balance_Enemy.HP_image = load_image('HP.png')
        self.x = random.randint(1350,1400)
        self.y = random.randint(40,250)
        self.HP = 250 + Balance_Enemy.HP_Upgrade
        self.First_HP = self.HP
        self.frame =0
        self.Timer=0
        self.myindex = None
        self.state = self.MOVE
        self.ATK = 10 + Balance_Enemy.ATK_Upgrade

    def Move(self):
        if self.Timer%10 ==0:
            self.frame = (self.frame+1)%8

        if self.Timer ==20:
            self.x = self.x-50
            self.Timer =0
            if self.x <= (Barricade.Wallx - ( (Barricade.Wally - self.y) /5.5)):
                self.frame =0
                self.state = self.ATTACK
                self.Tier =0

        self.Timer +=1

    def Attack(self):
        if ( self.frame != 0) and (self.Timer% 5 == 0):
            self.frame = (self.frame+1) % 4
            if self.frame ==2:
                Barricade.HP -= self.ATK
        elif self.Timer % 200 ==0:
            self.Timer =0
            self.frame = (self.frame+1) % 4

        self.Timer +=1

    def Die(self):
        global Object_List


        if self.frame ==4:
            Delete_Object_in_List(Object_List, self.myindex)
        elif self.Timer % 3 ==0:
            self.frame +=1

        self.Timer+=1

    handle_state = {
        MOVE : Move,
        ATTACK : Attack,
        DIE : Die
    }

    def update(self):
        self.handle_state[self.state](self)

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
            Attack_Enemy.image = load_image('LEnemy-Attack.png')
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
            Defense_Enemy.image = load_image('LEnemy-Defense.png')
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
           #for i in range(0, len(Object_List)):

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
                aim.avail_reload == False

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
            List[i].myindex-=1

def Check_Die(Object, index):
    if Object.HP<=0:
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
    Object_Data = json.load(Object_Data_File)
    if Type == BALANCE:
        Object = Balance_Enemy()
        Object.x = Object_Data['BALANCE']['x'] + random.randint(0,50)
        Object.y = Object_Data['BALANCE']['y'] + random.randint(0,210)
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
        if self.Balance_Enemy_Timer == 1000 - self.B_E_Decrease_Time:
            Create_Object(BALANCE)
            self.Balance_Enemy_Timer = 0
        self.Balance_Enemy_Timer+=1

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

    bg = BackGround()
    barricade = Barricade()
    UI = User_Interface()
    aim= Aim()

    create_enemy_timer = Create_Enemy_Timer()
    create_enemy_timer.Balance_Enemy_Switch = True
    Object_List.append(Balance_Enemy())

    hide_cursor()
    running=True

    while(running):
        handle_events(aim,Object_List)
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

        create_enemy_timer.update(Object_List)

        update_canvas()

    close_canvas()

if __name__ == '__main__':
    main()
