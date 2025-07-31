import pygame
import time

class Traffic_Light:
    def __init__(self, x, y, screen, angle=0):
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = angle
        self.state = "red"
        self.width = 30
        self.height = 70
        self.radius = 8
        self.last_switch = pygame.time.get_ticks()
        self.interval = 1000  # Time in milliseconds for each light state


    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_switch>self.interval:
            self.last_switch = now
            if self.state == "red":
                self.state = "green"
            elif self.state == "green":
                self.state = "yellow"
            elif self.state == "yellow":
                self.state = "red"  

    def draw(self):
        light_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(light_surf, (40, 40, 40), (0, 0, self.width, self.height))

        pos = {
            'red': (self.width // 2, 15),
            'yellow': (self.width // 2, self.height // 2),
            'green': (self.width // 2, self.height - 15)
        }

        for color, position in pos.items():
            pygame.draw.circle(
                light_surf,
                (255, 0, 0) if color == "red" and self.state == "red" else
                (255, 255, 0) if color == "yellow" and self.state == "yellow" else
                (0, 255, 0) if color == "green" and self.state == "green" else
                (60, 60, 60),
                position, self.radius
            )

        rotated_surf = pygame.transform.rotate(light_surf, self.angle)
        rotated_rect = rotated_surf.get_rect(center=(self.x, self.y))
        self.screen.blit(rotated_surf, rotated_rect)
