import pygame

class Traffic_Light:
    def __init__(self, x, y, screen, angle=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle  # Degrees: 0, 90, 180, -90

        # Colors
        self.color_red = (200, 0, 0)
        self.color_yellow = (200, 200, 0)
        self.color_green = (0, 200, 0)
        self.off_color = (40, 40, 40)

        self.state = 'red'  # default

        self.width = 20
        self.height = 60

        self.draw()  # draw initial state

    def draw(self):
        # Create light surface
        light_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        light_surface.fill((50, 50, 50))  # light casing

        # Draw lights based on current state
        pygame.draw.circle(light_surface, self.color_red if self.state == 'red' else self.off_color, (10, 10), 8)
        pygame.draw.circle(light_surface, self.color_yellow if self.state == 'yellow' else self.off_color, (10, 30), 8)
        pygame.draw.circle(light_surface, self.color_green if self.state == 'green' else self.off_color, (10, 50), 8)

        # Rotate the surface
        rotated_surface = pygame.transform.rotate(light_surface, self.angle)
        rect = rotated_surface.get_rect(center=(self.x, self.y))

        # Draw to screen
        self.screen.blit(rotated_surface, rect.topleft)

    def setGreen(self):
        self.state = 'green'
        self.draw()

    def setRed(self):
        self.state = 'red'
        self.draw()

    def setYellow(self):
        self.state = 'yellow'
        self.draw()

    # Keeping advanceLeft functions in case needed later
    def setAdvLeft(self):
        pass

    def cancelAdvLeft(self):
        pass
