#!/usr/bin/env python3

# Created by: Liam Hearty & Joseph Palermo
# Created on: December 2019
# This program runs "Ice Ice Baby"

import ugame
import stage
import time
import random
import constants


def splash_scene():
    image_bank_1 = stage.Bank.from_bmp16("IIB_sprites.bmp")
    background = stage.Grid(image_bank_1, 160, 120)
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    while True:
        time.sleep(1.0)
        menu_scene()


def menu_scene():
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_2, constants.SCREEN_X,
                            constants.SCREEN_Y)
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    sprites = []
    text = []
    text1 = stage.Text(width=29, height=12, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + sprites + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START != 0:
            game_scene()
        game.tick()


def game_scene():
    sprites = []

    # buttons that keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    image_bank_1 = stage.Bank.from_bmp16("IIB_sprites.bmp")

    vilheleme = stage.Sprite(image_bank_1, 2, int(constants.SCREEN_X / 2 -
                        constants.SPRITE_SIZE / 2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE +
                        constants.SPRITE_SIZE / 2))
    sprites.append(vilheleme)  # insert at the top of sprite list

    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)

    game = stage.Stage(ugame.display, constants.FPS)
    # V add layers here V
    game.layers = sprites + [background]
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # (keys)
        if keys & ugame.K_X:  # a button
            pass
        if keys & ugame.K_O:  # b
            pass
        if keys & ugame.K_START:  # start
            pass
        if keys & ugame.K_SELECT:  # select
            pass
        if keys & ugame.K_RIGHT != 0:  # right
            if vilheleme.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                vilheleme.move(constants.SCREEN_X - constants.SPRITE_SIZE,
                               vilheleme.y)
            else:
                vilheleme.move(vilheleme.x + 1, vilheleme.y)
            pass
        if keys & ugame.K_LEFT:  # left
            pass
        if keys & ugame.K_UP:  # up
            pass
        if keys & ugame.K_DOWN:  # down
            pass

if __name__ == "__main__":
    splash_scene()