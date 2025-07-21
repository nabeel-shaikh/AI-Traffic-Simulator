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

# colours
black = (0,0,0)
white = (255,255,255)
grey = (120,120,120)
red = (200,0,0)
green = (0,200,0)
yellow = (255, 255, 0)

# init
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Traffic Sim")
clock = pygame.time.Clock()

def draw_dashed_line(start, end, color, width=2, dash_length=20, gap=15):
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    distance = max(abs(dx), abs(dy))
    steps = distance // (dash_length + gap)
    for i in range(int(steps)):
        start_dash = (x1 + i * (dash_length + gap) * (dx / distance),
                      y1 + i * (dash_length + gap) * (dy / distance))
        end_dash = (start_dash[0] + dash_length * (dx / distance),
                    start_dash[1] + dash_length * (dy / distance))
        pygame.draw.line(screen, color, start_dash, end_dash, width)

def draw_intersection():
    screen.fill(grey)

    mid_x = screen_width // 2
    mid_y = screen_height // 2
    line_width = 4

    # Black roads
    pygame.draw.rect(screen, black, (0, mid_y - road_width//2, screen_width, road_width))  # horizontal
    pygame.draw.rect(screen, black, (mid_x - road_width//2, 0, road_width, screen_height))  # vertical

    # Yellow center dividers
    pygame.draw.line(screen, yellow, (mid_x, 0), (mid_x, mid_y - road_width//2), line_width)          # top
    pygame.draw.line(screen, yellow, (mid_x, mid_y + road_width//2), (mid_x, screen_height), line_width)  # bottom
    pygame.draw.line(screen, yellow, (0, mid_y), (mid_x - road_width//2, mid_y), line_width)           # left
    pygame.draw.line(screen, yellow, (mid_x + road_width//2, mid_y), (screen_width, mid_y), line_width)  # right

    # White dashed lanes
    edge_offset = road_width // 2
    white_offset = road_width // 4  # CORRECT: Halfway from center to edge

    # Vertical dashed lines
    draw_dashed_line((mid_x - white_offset, 0), (mid_x - white_offset, mid_y - edge_offset), white)
    draw_dashed_line((mid_x + white_offset, 0), (mid_x + white_offset, mid_y - edge_offset), white)
    draw_dashed_line((mid_x - white_offset, screen_height), (mid_x - white_offset, mid_y + edge_offset), white)
    draw_dashed_line((mid_x + white_offset, screen_height), (mid_x + white_offset, mid_y + edge_offset), white)

    # Horizontal dashed lines
    draw_dashed_line((0, mid_y - white_offset), (mid_x - edge_offset, mid_y - white_offset), white)
    draw_dashed_line((0, mid_y + white_offset), (mid_x - edge_offset, mid_y + white_offset), white)
    draw_dashed_line((screen_width, mid_y - white_offset), (mid_x + edge_offset, mid_y - white_offset), white)
    draw_dashed_line((screen_width, mid_y + white_offset), (mid_x + edge_offset, mid_y + white_offset), white)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_intersection()

        # Place traffic lights
        Tf1 = Traffic_Light(700, 300, screen, angle=0)     # top
        Tf2 = Traffic_Light(300, 700, screen, angle=180)   # bottom
        Tf3 = Traffic_Light(275, 300, screen, angle=90)    # left
        Tf4 = Traffic_Light(700, 700, screen, angle=-90)   # right

        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()
