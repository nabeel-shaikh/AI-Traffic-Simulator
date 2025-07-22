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

        if direction in ['up', 'down']:
            self.image = pygame.image.load("car1.png")
        else:
            self.image = pygame.image.load("car2.png")

        if direction in ['up', 'down']:
            self.image = pygame.image.load("car1.png")
            self.image = pygame.transform.scale(self.image, (40, 80))
        else:
            self.image = pygame.image.load("car2.png")
            self.image = pygame.transform.scale(self.image, (80, 40))

    def move(self):
        print(self.y, self.stop_line, self.traffic_light.state)
        if not self.crossed:
            if self.direction == 'up' and self.y - self.speed <= self.stop_line and self.traffic_light.state == 'red':
                return
            if self.direction == 'down' and self.y >= self.stop_line and self.traffic_light.state == 'red':
                return
            if self.direction == 'left' and self.x <= self.stop_line and self.traffic_light.state == 'red':
                return
            if self.direction == 'right' and self.x >= self.stop_line and self.traffic_light.state == 'red':
                return

        self.crossed = True
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
