#!/usr/bin/env python3

# Created by: Liam Hearty & Joseph Palermo
# Created on: January 2020
# This constants file is for IIB.py

# Circuitpython screen size is 160x128 and sprites are 16x16,
# So 10x8 sprite sized screen.
SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ICE = 25
TOTAL_NUMBER_OF_WATER = 25
TOTAL_NUMBER_OF_WALLS = 25
TOTAL_NUMBER_OF_KEYS = 1
TOTAL_NUMBER_OF_DOORS = 1
TOTAL_NUMBER_OF_FINISHES = 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 20
SCORE_ADDER = 100

NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

SCORE_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                 b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

LEVEL_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                 b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

MT_GAME_STUDIO_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                          b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

ICE_ICE_BABY_PALETTE = (b'\xbb\x43\x00\x55\xcey\x26\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                          b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}