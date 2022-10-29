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
from fiber_engine_helper import *
from fiber_engine_functions import *

# Initialize pygame
pygame.init()

player = character(90, 90, 0, 10, 10)

# Set the title of the window
set_window_title("Fiber Engine Display")

# Loop until the user clicks the close button.
done = False

# Initialize some variables
fov = 60
res = 8

# -------- Main Program Loop -----------
while not done:
    if(player.angle > 360):
        player.angle = 0
    if(player.angle < 0):
        player.angle = 360

    # --- Main event loop
    event_loop()
    
    # Player Input:
    keys = keyboard_input.get_keyboard_input()

    if keys[keyboard_input.left_arrow]:
        player.angle -= 4
    if keys[keyboard_input.right_arrow]:
        player.angle += 4
    if keys[keyboard_input.w]:
        player.move(-4)
    if keys[keyboard_input.s]:
        player.move(4)
    if keys[keyboard_input.d]:
        player.angle -= 90
        player.move(4)
        player.angle += 90
    if keys[keyboard_input.a]:
        player.angle += 90
        player.move(4)
        player.angle -= 90
    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    clear_screen()

    # Draw the map
    render_map()

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
    update_map()
    # --- Limit to 60 frames per second
    limit_fps(60)

# Close the window and quit.
close_game()