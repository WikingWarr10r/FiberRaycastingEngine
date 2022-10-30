import math
import pygame
import fiber_engine_keyboard_input as keyboard_input

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize variables
objects = []
collisions = []
colliding = False
fov = 60
res = 8

# Initialize the map
map_width = 10
map_height = 10
map_grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def render_map():
    global objects 
    objects = []
    for y in range(map_height):
        for x in range(map_width):
            if map_grid[y][x] == 1:
                object(x, y, 60, 60)
                objects[len(objects) - 1].update()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([1200, 1000])


# Define some basic objects
class character():
    def __init__(self, x, y, angle, width, height):
        self.x = x
        self.y = y
        self.angle = angle
        self.width = width
        self.height = height
        self.collider = pygame.rect.Rect(self.x, self.y, self.width, self.width)
    
    def update(self):
        pygame.draw.circle(screen, BLACK, [self.x, self.y], self.width)
        self.collider = pygame.rect.Rect(self.x, self.y, self.width, self.width)

    def move(self, steps):
        self.x += steps * math.cos(math.radians(self.angle - 33))
        for wall in objects:
            if map_grid[int(self.y / 60)][int(self.x / 60)] == 1:
                self.x -= steps * math.cos(math.radians(self.angle - 33))
        self.y += steps * math.sin(math.radians(self.angle - 33))
        for wall in objects:
            if map_grid[int(self.y / 60)][int(self.x / 60)] == 1:
                self.y -= steps * math.sin(math.radians(self.angle - 33))

class object():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collider = pygame.rect.Rect(self.x, self.y, self.width, self.width)
        objects.append(self)
    
    def update(self):
        pygame.draw.rect(screen, BLACK, [self.x * 60, self.y * 60, self.width, self.height])

player = character(90, 90, 0, 10, 10)