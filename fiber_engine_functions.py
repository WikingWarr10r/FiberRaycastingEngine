import pygame
import math

from fiber_engine_helper import BLACK
from fiber_engine_helper import screen
from fiber_engine_helper import clock
from fiber_engine_helper import map_grid
from fiber_engine_helper import map_width
from fiber_engine_helper import map_height
from fiber_engine_helper import player
from fiber_engine_helper import fov
from fiber_engine_helper import res

def fiber_engine_init():
    pygame.init()

def set_window_title(caption):
    pygame.display.set_caption(caption)

def event_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

def clear_screen():
    screen.fill(BLACK)

def raycast():
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

def update_map():
    pygame.display.flip()

def limit_fps(fps):
    clock.tick(fps)

def close_game():
    pygame.quit()