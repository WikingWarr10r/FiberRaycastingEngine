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

from fiber_engine_helper import *
from fiber_engine_functions import *

# Initialize pygame
fiber_engine_init()

# Set the title of the window
set_window_title("Fiber Engine Display")

# Loop until the user clicks the close button.
done = False

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
    raycast()

    # --- Update the screen with what we've drawn.
    update_map()
    # --- Limit to 60 frames per second
    limit_fps(60)

# Close the window and quit.
close_game()