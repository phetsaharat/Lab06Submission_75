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
        if mouseX >= self.x and mouseY >= self.y and mouseX <= (self.x+self.w) and mouseY <= (self.y+self.h):
            return True
        else:  
            return False
    pass

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class InputnumBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isnumeric(): 
                        self.text += event.unicode
                    else:
                        return False
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
        
pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(600,300,150,80,255,57,57)

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text1 = font.render('Firstname', True, (0,102,204))
text2 = font.render('Lastname', True, (0,102,204))
text3 = font.render('Age', True, (0,102,204)) # (text,is smooth?,letter color,background color)
text4 = font.render('submit', True, (0,102,204))


input_box1 = InputBox(100, 100, 140, 32)
input_box2 = InputBox(100, 200, 140, 32) # สร้าง InputBox1
input_box3 = InputnumBox(100, 300, 140, 32) # สร้าง InputBox2
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

run = True

state = False

while run:
    screen.fill((255, 255, 150))
    screen.blit(text1, (100,68))
    screen.blit(text2, (100,168))
    screen.blit(text3, (100,265))
    
    
    if btn.isMouseOn():
        if pg.mouse.get_pressed()[0]:
            btn.r = 178
            btn.g = 178
            btn.b = 178
            state = True
        if pg.mouse.get_pressed()[2]:
            btn.r = 178
            btn.g = 178
            btn.b = 178
            state = False
    else:
        btn.r = 255
        btn.g = 57
        btn.b = 57
        
    if state == True:
        font = pg.font.Font('freesansbold.ttf', 20)
        text5 = font.render('Hello '+input_box1.text+' '+input_box2.text+'! You are '+input_box3.text+' years old.', True, (0,102,204))
        screen.blit(text5, (350,200))
    btn.draw(screen)
    screen.blit(text4, (620,320))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    pg.time.delay(1)
    pg.display.update()