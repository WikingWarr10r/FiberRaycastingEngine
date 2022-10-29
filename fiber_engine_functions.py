import pygame
from fiber_engine_helper import BLACK
from fiber_engine_helper import map_height
from fiber_engine_helper import map_width
from fiber_engine_helper import map_grid
from fiber_engine_helper import screen
from fiber_engine_helper import clock
from fiber_engine_helper import object
from fiber_engine_helper import objects

def set_window_title(caption):
    pygame.display.set_caption(caption)

def event_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

def clear_screen():
    screen.fill(BLACK)

def update_map():
    pygame.display.flip()

def limit_fps(fps):
    clock.tick(fps)

def close_game():
    pygame.quit()