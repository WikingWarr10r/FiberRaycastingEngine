# Copyright 2022 WikingWarr10r
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pygame
import math

# Initialize pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1200, 1000])

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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
        self.x += steps * math.cos(math.radians(self.angle))
        for wall in objects:
            if map_grid[int(self.y / 60)][int(self.x / 60)] == 1:
                self.x -= steps * math.cos(math.radians(self.angle))
        self.y += steps * math.sin(math.radians(self.angle))
        for wall in objects:
            if map_grid[int(self.y / 60)][int(self.x / 60)] == 1:
                self.y -= steps * math.sin(math.radians(self.angle))

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

# Set the title of the window
pygame.display.set_caption('Fiber Engine Display')

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize some variables
fov = 60
res = 8
objects = []
collisions = []
colliding = False

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

# -------- Main Program Loop -----------
while not done:
    if(player.angle > 360):
        player.angle = 0
    if(player.angle < 0):
        player.angle = 360

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys=pygame.key.get_pressed()

    # Player Input:
    if keys[pygame.K_LEFT]:
        player.angle -= 4
    if keys[pygame.K_RIGHT]:
        player.angle += 4
    if keys[pygame.K_w]:
        player.move(-4)
    if keys[pygame.K_s]:
        player.move(4)
    if keys[pygame.K_d]:
        player.angle -= 90
        player.move(4)
        player.angle += 90
    if keys[pygame.K_a]:
        player.angle += 90
        player.move(4)
        player.angle -= 90
    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    # Draw the map
    objects = []
    for y in range(map_height):
        for x in range(map_width):
            if map_grid[y][x] == 1:
                object(x, y, 60, 60)
                objects[len(objects) - 1].update()

    # Draw the player
    player.update()

    # Simulate the rays
    draw_x = 0
    for ray in range(0, int(fov / float(res))*int(res), 1):
        # Calculate the angle of the ray
        ray_angle = (player.angle + ray) - ((float(fov)/2) * float(res))

        # Calculate the distance to the wall
        distance = 0
        while True:
            # Calculate the x and y coordinates of the ray
            ray_x = player.x + distance * math.cos(math.radians(ray_angle))
            ray_y = player.y + distance * math.sin(math.radians(ray_angle))

            # Check if the ray is out of bounds
            if ray_x < 0 or ray_x > map_width * 60 or ray_y < 0 or ray_y > map_height * 60:
                break

            # Check if the ray has hit a wall
            if map_grid[int(ray_y / 60)][int(ray_x / 60)] == 1:
                break

            # Increment the distance
            distance += 1

        distance += 0.0001
        height = 2 * (4000 / distance)

        # Draw the ray
        pygame.draw.line(screen, (255 - distance/4, 255 - distance/4, 255 - distance/4), [draw_x, height + 400], [draw_x, (0 - height) + 300], 2 * res)
        draw_x = draw_x + 2 * res

    # --- Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()