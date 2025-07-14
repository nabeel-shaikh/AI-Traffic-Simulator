import pygame 
import sys
from traffic_light import Traffic_Light
import time

screen_width = 1000
screen_height = 1000
road_width = 300
light_size = 40
fps = 60
car_size = (20,40)

#colours:
black = (0,0,0)
white = (255,255,255)
grey = (120,120,120)
red= (200,0,0)
green = (0,200,0)


#init
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Traffic Sim")
clock = pygame.time.Clock()

def draw_intersection():
    screen.fill(grey)

    #horizontal road
    pygame.draw.rect(screen, black,(0,screen_height//2-road_width//2, screen_width, road_width))

    #vertical road
    pygame.draw.rect(screen,black,(screen_width//2-road_width//2, 0, road_width, screen_height))

    Tf1 = Traffic_Light(460, 300, screen)#need to pass arguments
    Tf2 = Traffic_Light(520, 600, screen)#need to pass arguments
    Tf3 = Traffic_Light(300, 460, screen)#need to pass arguments
    Tf4 = Traffic_Light(600, 520, screen)#need to pass arguments
    time.sleep(3)
    Tf1.setGreen()
    time.sleep(3)
    Tf1.setRed()




def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_intersection()
        pygame.display.flip()
        
        clock.tick(fps)
        

if __name__ == "__main__":
    main()
