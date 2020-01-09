#!/usr/bin/env python3

# Created by: Liam Hearty & Joseph Palermo
# Created on: January 2020
# This constants file is for IIB.py

# Circuitpython screen size is 160x120 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 8
TOTAL_NUMBER_OF_LASERS = 8
SHIP_SPEED = 1
CHARACTER_SPEED = 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
LASER_SPEED = 2
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60
SPRITE_MOVEMENT_SPEED = 1
SCORE_ADDER = 100

NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

SCORE_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                 b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

MT_GAME_STUDIO_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                          b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}
