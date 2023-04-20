import sys 
import pygame as pg
class Rec:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r 
        self.g = g
        self.b = b
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))
class Button(Rec):
    def __init__(self, x=0, y=0, w=0, h=0,r=0,g=0,b=0):
        Rec.__init__(self, x, y, w, h,r,g,b)
    
    def isMouseOn(self):
        mouseX , mouseY = pg.mouse.get_pos()
        if mouseX >= self.x and mouseY >= self.y and mouseX <= self.w and mouseY <= self.h:
            return True
        else:
            return False
    pass

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,255,57,57) # สร้าง Object จากคลาส Button ขึ้นมา
switch_w = False
switch_a = False
switch_s = False
switch_d = False

while(run):
    screen.fill((255, 255, 255))
    btn.draw(screen)
    if switch_d :
        btn.x +=1
    if switch_a :
        btn.x -=1
    if switch_w :
        btn.y -=1
    if switch_s :
        btn.y +=1
        pg.time.delay(1)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key D down")
            switch_d = True
        if event.type == pg.KEYUP and event.key == pg.K_d: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key D up")
            switch_d = False
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key a down")
            switch_a = True
        if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key a up")
            switch_a = False
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key w down")
            switch_w = True
        if event.type == pg.KEYUP and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key w up")
            switch_w = False
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key s down")
            switch_s = True
        if event.type == pg.KEYUP and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key s up")
            switch_s = False