import pygame
import sys
from traffic_light import Traffic_Light
from car import Car

screen_width = 1000
screen_height = 1000
road_width = 300
fps = 60

black = (0, 0, 0)
white = (255, 255, 255)
grey = (120, 120, 120)
yellow = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Traffic Sim")
clock = pygame.time.Clock()

def draw_dashed_line(start, end, color, width=2, dash_length=20, gap=15):
    x1, y1 = start
    x2, y2 = end
    dx, dy = x2 - x1, y2 - y1
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
    white_offset = road_width // 4
    edge_offset = road_width // 2

    pygame.draw.rect(screen, black, (0, mid_y - edge_offset, screen_width, road_width))
    pygame.draw.rect(screen, black, (mid_x - edge_offset, 0, road_width, screen_height))

    pygame.draw.line(screen, yellow, (mid_x, 0), (mid_x, mid_y - edge_offset), line_width)
    pygame.draw.line(screen, yellow, (mid_x, mid_y + edge_offset), (mid_x, screen_height), line_width)
    pygame.draw.line(screen, yellow, (0, mid_y), (mid_x - edge_offset, mid_y), line_width)
    pygame.draw.line(screen, yellow, (mid_x + edge_offset, mid_y), (screen_width, mid_y), line_width)

    draw_dashed_line((mid_x - white_offset, 0), (mid_x - white_offset, mid_y - edge_offset), white)
    draw_dashed_line((mid_x + white_offset, 0), (mid_x + white_offset, mid_y - edge_offset), white)
    draw_dashed_line((mid_x - white_offset, screen_height), (mid_x - white_offset, mid_y + edge_offset), white)
    draw_dashed_line((mid_x + white_offset, screen_height), (mid_x + white_offset, mid_y + edge_offset), white)
    draw_dashed_line((0, mid_y - white_offset), (mid_x - edge_offset, mid_y - white_offset), white)
    draw_dashed_line((0, mid_y + white_offset), (mid_x - edge_offset, mid_y + white_offset), white)
    draw_dashed_line((screen_width, mid_y - white_offset), (mid_x + edge_offset, mid_y - white_offset), white)
    draw_dashed_line((screen_width, mid_y + white_offset), (mid_x + edge_offset, mid_y + white_offset), white)

def main():
    mid_x = screen_width // 2
    mid_y = screen_height // 2
    left_lane = mid_x - road_width // 2.6
    right_lane = mid_x + road_width // 2.6
    top_lane = mid_y - road_width // 2.6
    bottom_lane = mid_y + road_width // 2.6

    tf1 = Traffic_Light(275, 300, screen, angle=90) #top left
    tf2 = Traffic_Light(700, 300, screen, angle=0) # top right

    tf3 = Traffic_Light(275, 700, screen, angle=180) # bottom left
    tf4 = Traffic_Light(700, 700, screen, angle=-90) # bottom right
    #tf4.state = "green"
    #tf1.state="green"
    tf2.state = "green"
    #tf3.state = "green"

    traffic_lights = [tf1, tf2, tf3, tf4]

    car1 = Car(375, 1000, screen, 'up', tf4, stop_line=530)       # bottom to top
    car2 = Car(1000, 375, screen, 'left', tf2, stop_line=530)     # right to left

    cars = [car1, car2]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_intersection()

        for light in traffic_lights:
            light.update()
            light.draw()

        for car in cars:
            car.move()
            car.draw()

        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()
