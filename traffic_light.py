
import pygame
class Traffic_Light:
    def __init__(self,x,y,screen) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.advanceLeft = "Red"

        #lights colours
        self.color_red = (200,0,0)
        self.color_yellow = (200,200,0)
        self.color_green = (0,200,0)
        self.off_color = (40,40,40)
        #draw traffic light with x,y,orientation. add code here
        pygame.draw.rect(self.screen, (50, 50, 50), (self.x, self.y, 20, 60))
        
        self.setRed()
     
    def setGreen(self):
        self.clearTF()
        pygame.draw.circle(self.screen, self.color_green, (self.x + 10, self.y + 10 + 2*20),8)
    
    def setRed(self):
        self.clearTF()
        pygame.draw.circle(self.screen, self.color_yellow, (self.x + 10, self.y + 10 + 1*20),8)
        self.clearTF()
        pygame.draw.circle(self.screen, self.color_red, (self.x + 10, self.y + 10),8)

    def clearTF(self):
        pygame.draw.circle(self.screen, self.off_color, (self.x + 10, self.y + 10), 8)      
        pygame.draw.circle(self.screen, self.off_color, (self.x + 10, self.y + 30), 8)      
        pygame.draw.circle(self.screen, self.off_color, (self.x + 10, self.y + 50), 8) 

    def setAdvLeft(self):
        pygame.draw.rect(self.screen,self.color_green,(self.x + 25, self.y + 10, 8, 16)) # use rect as straight arrow.

    
    def cancelAdvLeft(self):
        pygame.draw.rect(self.screen,self.color_yellow,(self.x + 25, self.y + 10, 8, 16)) 
        pygame.draw.rect(self.screen,self.color_red,(self.x + 25, self.y + 10, 8, 16))
        





    





    