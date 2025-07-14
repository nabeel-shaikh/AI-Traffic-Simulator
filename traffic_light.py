import time
import pygame
class Traffic_Light:
    def __init__(self,x,y,orientation,screen) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.orientation = orientation #north/south/east/west.
        self.advanceLeft = "Red"

        #lights colours
        self.color_red = (200,0,0)
        self.color_yellow = (200,200,0)
        self.color_green = (0,200,0)
        self.off_color = (40,40,40)
        #draw traffic light with x,y,orientation.
        #make sure traffic light red

        
    def setGreen(self):
        pygame.draw.circle(self.screen, self.color_green, (self.x + 10, self.y + 10 + 2*20),8)
    
    def setRed(self):

        pygame.draw.circle(self.screen, self.color_yellow, (self.x + 10, self.y + 10 + 1*20),8)
        time.sleep(3)
        pygame.draw.circle(self.screen, self.color_red, (self.x + 10, self.y + 10),8)


    
    def setAdvLeft(self):
        pygame.draw.rect(self.screen,self.color_green,(self.x + 25, self.y + 10, 8, 16)) # use rect as straight arrow.

    
    def cancelAdvLeft(self):
        pygame.draw.rect(self.screen,self.color_yellow,(self.x + 25, self.y + 10, 8, 16)) 
        time.sleep(3)
        pygame.draw.rect(self.screen,self.color_red,(self.x + 25, self.y + 10, 8, 16))
        





    





    