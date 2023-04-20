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

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        btn.r = 178
        btn.g = 178
        btn.b = 178
        btn.w = 200
        btn.h = 300
        if pg.mouse.get_pressed()[0]:
            btn.r = 204
            btn.g = 0
            btn.b = 204
    else:
        btn.r = 255
        btn.g = 57
        btn.b = 57
        btn.w = 100
        btn.h = 100
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False