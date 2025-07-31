import pygame

class Car:
    def __init__(self, x, y, screen, direction, traffic_light, stop_line):
        self.x = x
        self.y = y
        self.screen = screen
        self.direction = direction
        self.speed = 2
        self.traffic_light = traffic_light
        self.stop_line = stop_line
        self.crossed = False

        car_image_file = "car1.png" if direction in ['up', 'down'] else "car2.png"
        self.image = pygame.image.load(car_image_file)
        self.image = pygame.transform.scale(self.image, (40, 80) if direction in ['up', 'down'] else (80, 40))

    
    def move(self):
    # Check if car has crossed the stop line
        if not self.crossed:
            if self.direction == 'up':
                if self.y <= self.stop_line:
                    self.crossed = True
                elif self.traffic_light.state == 'red':
                    return
            elif self.direction == 'down':
                if self.y >= self.stop_line:
                    self.crossed = True
                elif self.traffic_light.state == 'red':
                    return
            elif self.direction == 'left':
                if self.x <= self.stop_line:
                    self.crossed = True
                elif self.traffic_light.state == 'red':
                    return
            elif self.direction == 'right':
                if self.x >= self.stop_line:
                    self.crossed = True
                elif self.traffic_light.state == 'red':
                    return

        # Move
        if self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed




    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
