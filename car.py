import pygame

class Car:
    def __init__(self, x, y, direction, speed, color=(0, 0, 255), size=(20, 40)):
        self.x = x
        self.y = y
        self.direction = direction  # angle in degrees: 0=right, 90=down, 180=left, 270=up
        self.speed = speed
        self.color = color
        self.size = size

    def move(self):
        # Move the car in its current direction
        vec = pygame.math.Vector2(self.speed, 0).rotate(-self.direction)
        self.x += vec.x
        self.y += vec.y

    def draw(self, screen):
        car_surf = pygame.Surface(self.size)
        car_surf.fill(self.color)
        rotated_surf = pygame.transform.rotate(car_surf, self.direction)
        rect = rotated_surf.get_rect(center=(self.x + self.size[0] // 2, self.y + self.size[1] // 2))
        screen.blit(rotated_surf, rect.topleft)
