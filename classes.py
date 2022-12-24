import pygame
import math

def coord(y,height):
    return height-y

def redraw(win):
    win.fill((0,0,0))
    for rec in rectangle.activeObject:
        rec.draw(win)
    pygame.display.update()

class vector:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        if isinstance(other,float) or isinstance(other,int):
            return vector(self.x*other,self.y*other)
    
    def __truediv__(self,other):
        if isinstance(other,int):
            return vector(self.x*1/other,self.y*1/other)
    
    def __repr__(self):
        return f'{self.x},{self.y}'

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
        
    def unitVector(self):
        return vector(self.x/self.magnitude(),self.y/self.magnitude())


class rectangle:

    activeObject = []
    G = 0.000000000066/60*60
    G = 1

    def __init__(self,x,y,mass,colour,sizex,sizey):
        
        self.mass = mass
        self.colour = colour
        self.sizex=sizex
        self.sizey=sizey
        
        self.pos = vector(x,y)
        self.vel = vector()
        self.accel = vector()

        rectangle.activeObject.append(self)
    
    def force(self,f):
        self.accel+=f*1/self.mass

    def gravity(self):
        for rec in rectangle.activeObject:
            distance = rec.pos-self.pos
            distancemag = distance.magnitude()
            #since there is no collision detection, when the objects gets really close the gravitational force becomes really high, hence the if statement
            if distancemag >5:
                gravMagnitude = rectangle.G*rec.mass*self.mass/distancemag**2
                self.force(distance.unitVector()*gravMagnitude)

    def update(self):
        self.gravity()
        self.pos+=self.vel
        self.vel+=self.accel
        self.accel = vector()

    def getRect(self):
        return pygame.Rect(self.pos.x+self.sizex/2,self.pos.y+self.sizey/2,self.sizex,self.sizey)

    def draw(self,win):
        pygame.draw.rect(win,self.colour,(self.pos.x+self.sizex/2,coord(self.pos.y,win.get_size()[1])+self.sizey/2,self.sizex,self.sizey))

    @classmethod
    def collision(cls):
        for i in range(len(cls.activeObject)):
            for j in range(i+1,len(cls.activeObject)):
                if pygame.Rect.colliderect(cls.activeObject[i].getRect(),cls.activeObject[j].getRect()):
                    #pls
                    pass
    
    @classmethod
    def classUpdate(cls):
        for rec in cls.activeObject:
            rec.update()
            print(rec.vel)
        cls.collision()

        
