#!/usr/bin/env python3

# Created by: Liam Hearty & Joseph Palermo
# Created on: January 2020
# This program runs "Ice Ice Baby"

import ugame
import stage
import constants
import time

def splash_scene():

    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
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

    # get sound ready
    boot_up = open("boot_up.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    sprites = []
    text = []
    text2_list = []
    text1 = stage.Text(width=29, height=12, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    text2 = stage.Text(width=15, height=5, font=None,
                        palette=constants.NEW_PALETTE, buffer=None)
    text2.move(30, 100)
    text2.text("Made by        Liam & Joseph")
    text.append(text2)

    sound.play(boot_up)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + sprites + [background]
    game.render_block()

    image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 15)

    time.sleep(3)
    menu_scene()
    game.tick()


def menu_scene():

    image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 15)

    sprites = []
    text = []
    text3 = []
    text3_list = []
    text3 = stage.Text(width=29, height=12, font=None,
                       palette=constants.ICE_ICE_BABY_PALETTE, buffer=None)
    text3.move(30, 6)
    text3.text("Ice Ice Baby")
    text.append(text3)
    text4 = []
    text4_list = []
    text4 = stage.Text(width=17, height=5, font=None,
                       palette=constants.ICE_ICE_BABY_PALETTE, buffer=None)
    text4.move(16, 116)
    text4.text("Press A To Begin")
    text.append(text4)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + sprites + [background]
    game.render_block()

    lvl1 = None
    final_score = None

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X != 0:
            final_score = 0
            score = lvl_1()
            lvl1 = 1
        game.tick()
        if lvl1 == 1:
            final_score = lvl_2(score)
            lvl1 = 2
        game.tick()
        if lvl1 == 2:
            game_over(final_score)
        game.tick()

def lvl_1():
    vilheleme_list = []
    water_sprites = []
    ice_sprites = []
    key_list = []
    door_list = []
    finish_list = []
    wall_sprites = []

    # get sound ready
    press_start_audio = open("press_start_audio.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # get sound ready
    key_collect = open("key_collect.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # score and level
    score = 0
    level = 1

    # buttons that keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    up_button = constants.button_state["button_up"]
    down_button = constants.button_state["button_up"]
    left_button = constants.button_state["button_up"]
    right_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")

    # create vilheleme
    vilheleme = stage.Sprite(image_bank_1, 2, 16, 64)
    vilheleme_list.append(vilheleme)  # insert at the top of sprite list

    # create ice
    for ice_number in range(constants.TOTAL_NUMBER_OF_ICE):
        a_single_ice = stage.Sprite(image_bank_1, 7,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        ice_sprites.append(a_single_ice)

    # create walls
    for wall_number in range(constants.TOTAL_NUMBER_OF_WALLS):
        a_single_wall = stage.Sprite(image_bank_1, 14,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        wall_sprites.append(a_single_wall)

    # create water
    for water_number in range(constants.TOTAL_NUMBER_OF_WATER):
        a_single_water = stage.Sprite(image_bank_1, 4,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        water_sprites.append(a_single_water)

    # create key
    key = stage.Sprite(image_bank_1, 11, constants.OFF_SCREEN_X,
                           constants.OFF_SCREEN_Y)
    key_list.append(key)  # insert at the top of sprite list

    # create door
    door = stage.Sprite(image_bank_1, 12, constants.OFF_SCREEN_X,
                            constants.OFF_SCREEN_Y)
    door_list.append(door)  # insert at the top of sprite list

    # create finish
    finish = stage.Sprite(image_bank_1, 13, constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
    finish_list.append(finish)  # insert at the top of sprite list

    # create background
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 3)

    counter = 0
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(0, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(0, 64)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(0, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(16, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(16, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(32, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(32, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(48, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(48, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(64, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(64, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(80, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(80, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(96, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(96, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(112, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(112, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(128, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(128, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(144, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(144, 64)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(144, 80)
        counter += 1

    counter = 0
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(16, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(32, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(48, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(64, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(80, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(96, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(112, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(128, 64)
        counter += 1

    counter = 0
    if key_list[counter].x < 0:
        key_list[counter].move(64, 64)
        counter += 1

    counter = 0
    if door_list[counter].x < 0:
        door_list[counter].move(96, 64)
        counter += 1

    counter = 0
    if finish_list[counter].x < 0:
        finish_list[counter].move(128, 64)
        counter += 1

    # V If game lags, change this V
    game = stage.Stage(ugame.display, constants.FPS)

    sound.play(press_start_audio)

    counter_r = 0

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_UP != 0:  # up button possible positions
            if up_button == constants.button_state["button_up"]:
                up_button = constants.button_state["button_just_pressed"]
            elif up_button == constants.button_state["button_just_pressed"]:
                up_button = constants.button_state["button_still_pressed"]
        else:
            if up_button == constants.button_state["button_still_pressed"]:
                up_button = constants.button_state["button_released"]
            else:
                up_button = constants.button_state["button_up"]

        if keys & ugame.K_DOWN != 0:  # down button possible positions
            if down_button == constants.button_state["button_up"]:
                down_button = constants.button_state["button_just_pressed"]
            elif down_button == constants.button_state["button_just_pressed"]:
                down_button = constants.button_state["button_still_pressed"]
        else:
            if down_button == constants.button_state["button_still_pressed"]:
                down_button = constants.button_state["button_released"]
            else:
                down_button = constants.button_state["button_up"]

        if keys & ugame.K_LEFT != 0:  # left button possible positions
            if left_button == constants.button_state["button_up"]:
                left_button = constants.button_state["button_just_pressed"]
            elif left_button == constants.button_state["button_just_pressed"]:
                left_button = constants.button_state["button_still_pressed"]
        else:
            if left_button == constants.button_state["button_still_pressed"]:
                left_button = constants.button_state["button_released"]
            else:
                left_button = constants.button_state["button_up"]

        if keys & ugame.K_RIGHT != 0:  # right button possible positions
            if right_button == constants.button_state["button_up"]:
                right_button = constants.button_state["button_just_pressed"]
            elif right_button == constants.button_state["button_just_pressed"]:
                right_button = constants.button_state["button_still_pressed"]
        else:
            if right_button == constants.button_state["button_still_pressed"]:
                right_button = constants.button_state["button_released"]
            else:
                right_button = constants.button_state["button_up"]

        # add text at top of screen for score
        score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
        score_text.clear()
        score_text.cursor(0, 0)
        score_text.move(1, 1)
        score_text.text("{0}".format(score))

        # add text at top of screen for level
        level_text = stage.Text(width=20, height=15, font=None, palette=constants.LEVEL_PALETTE, buffer=None)
        level_text.clear()
        level_text.cursor(12, 0)
        level_text.move(1, 1)
        level_text.text("Level {0}".format(level))

        # V add layers here V
        game.layers = vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites + [score_text] + [level_text] + [background]
        game.render_block()

        # keys
        if keys & ugame.K_RIGHT != 0:  # right
            if right_button == constants.button_state["button_just_pressed"]:
                vilheleme.move(vilheleme.x + constants.SPRITE_SIZE, vilheleme.y)
                for ice_number in range(len(ice_sprites)):
                    if vilheleme.x > 0:
                        if stage.collide(ice_sprites[ice_number].x, ice_sprites[ice_number].y,
                                         ice_sprites[ice_number].x + 15, ice_sprites[ice_number].y + 15,
                                         vilheleme_list[0].x, vilheleme_list[0].y,
                                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                            if water_sprites[counter_r].x < 0:
                                water_sprites[counter_r].move(vilheleme.x - constants.SPRITE_SIZE, vilheleme.y)
                                counter_r += 1
                                score += 100

            game.render_sprites(vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites)

        if keys & ugame.K_LEFT != 0:  # left
            if left_button == constants.button_state["button_just_pressed"]:
                if vilheleme.x > 16:
                    vilheleme.move(vilheleme.x - constants.SPRITE_SIZE, vilheleme.y)

            game.render_sprites(vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites)
            game.tick()


        if stage.collide(key_list[0].x, key_list[0].y,
                         key_list[0].x + 15, key_list[0].y + 15,
                         vilheleme_list[0].x, vilheleme_list[0].y,
                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
            key.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
            door.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        if stage.collide(finish_list[0].x, finish_list[0].y,
                         finish_list[0].x + 15, finish_list[0].y + 15,
                         vilheleme_list[0].x, vilheleme_list[0].y,
                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
            score += 1000
            counter_r = 0
            sound.play(key_collect)
            return(score)

        for water_number in range(len(water_sprites)):
            if stage.collide(water_sprites[water_number].x, water_sprites[water_number].y,
                             water_sprites[water_number].x + 15, water_sprites[water_number].y + 15,
                             vilheleme_list[0].x, vilheleme_list[0].y,
                             vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                final_score = score
                game_over(final_score)
        
                game.render_sprites(vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites)
                game.tick()


def lvl_2(score):

    vilheleme_list = []
    water_sprites = []
    ice_sprites = []
    key_list = []
    door_list = []
    finish_list = []
    wall_sprites = []

    # get sound ready
    press_start_audio = open("press_start_audio.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # get sound ready
    key_collect = open("key_collect.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    level = 2

    # buttons that keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    up_button = constants.button_state["button_up"]
    down_button = constants.button_state["button_up"]
    left_button = constants.button_state["button_up"]
    right_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")

    # create vilheleme
    vilheleme = stage.Sprite(image_bank_1, 2, 16, 48)
    vilheleme_list.append(vilheleme)  # insert at the top of sprite list

    # create ice
    for ice_number in range(constants.TOTAL_NUMBER_OF_ICE_2):
        a_single_ice = stage.Sprite(image_bank_1, 7,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        ice_sprites.append(a_single_ice)

    # create walls
    for wall_number in range(constants.TOTAL_NUMBER_OF_WALLS_2):
        a_single_wall = stage.Sprite(image_bank_1, 14,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        wall_sprites.append(a_single_wall)

    # create water
    for water_number in range(constants.TOTAL_NUMBER_OF_WATER_2):
        a_single_water = stage.Sprite(image_bank_1, 4,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        water_sprites.append(a_single_water)

    # create key
    key = stage.Sprite(image_bank_1, 11, constants.OFF_SCREEN_X,
                           constants.OFF_SCREEN_Y)
    key_list.append(key)  # insert at the top of sprite list

    # create door
    door = stage.Sprite(image_bank_1, 12, constants.OFF_SCREEN_X,
                            constants.OFF_SCREEN_Y)
    door_list.append(door)  # insert at the top of sprite list

    # create finish
    finish = stage.Sprite(image_bank_1, 13, constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
    finish_list.append(finish)  # insert at the top of sprite list

    # create background
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 3)

    counter = 0
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(0, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(0, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(0, 64)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(0, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(0, 96)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(16, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(16, 96)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(32, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(32, 96)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(48, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(48, 96)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(64, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(64, 96)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(80, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(80, 96)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(96, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(96, 96)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(112, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(112, 96)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(128, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(128, 96)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(144, 32)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(144, 48)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(144, 64)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(144, 80)
        counter += 1
    if wall_sprites[counter].x < 0:
        wall_sprites[counter].move(144, 96)
        counter += 1

    counter = 0
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(16, 48)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(32, 48)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(48, 48)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(64, 48)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(80, 48)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(96, 48)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(112, 48)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(128, 48)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(16, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(32, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(48, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(64, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(80, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(96, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(112, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(128, 64)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(16, 80)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(32, 80)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(48, 80)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(64, 80)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(80, 80)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(96, 80)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(112, 80)
        counter += 1
    if ice_sprites[counter].x < 0:
        ice_sprites[counter].move(128, 80)
        counter += 1

    counter = 0
    if key_list[counter].x < 0:
        key_list[counter].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        counter += 1

    counter = 0
    if door_list[counter].x < 0:
        door_list[counter].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        counter += 1

    counter = 0
    if finish_list[counter].x < 0:
        finish_list[counter].move(128, 80)
        counter += 1

    # V If game lags, change this V
    game = stage.Stage(ugame.display, constants.FPS)


    sound.play(press_start_audio)

    counter_r = 0

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_UP != 0:  # up button possible positions
            if up_button == constants.button_state["button_up"]:
                up_button = constants.button_state["button_just_pressed"]
            elif up_button == constants.button_state["button_just_pressed"]:
                up_button = constants.button_state["button_still_pressed"]
        else:
            if up_button == constants.button_state["button_still_pressed"]:
                up_button = constants.button_state["button_released"]
            else:
                up_button = constants.button_state["button_up"]

        if keys & ugame.K_DOWN != 0:  # down button possible positions
            if down_button == constants.button_state["button_up"]:
                down_button = constants.button_state["button_just_pressed"]
            elif down_button == constants.button_state["button_just_pressed"]:
                down_button = constants.button_state["button_still_pressed"]
        else:
            if down_button == constants.button_state["button_still_pressed"]:
                down_button = constants.button_state["button_released"]
            else:
                down_button = constants.button_state["button_up"]

        if keys & ugame.K_LEFT != 0:  # left button possible positions
            if left_button == constants.button_state["button_up"]:
                left_button = constants.button_state["button_just_pressed"]
            elif left_button == constants.button_state["button_just_pressed"]:
                left_button = constants.button_state["button_still_pressed"]
        else:
            if left_button == constants.button_state["button_still_pressed"]:
                left_button = constants.button_state["button_released"]
            else:
                left_button = constants.button_state["button_up"]

        if keys & ugame.K_RIGHT != 0:  # right button possible positions
            if right_button == constants.button_state["button_up"]:
                right_button = constants.button_state["button_just_pressed"]
            elif right_button == constants.button_state["button_just_pressed"]:
                right_button = constants.button_state["button_still_pressed"]
        else:
            if right_button == constants.button_state["button_still_pressed"]:
                right_button = constants.button_state["button_released"]
            else:
                right_button = constants.button_state["button_up"]

        # add text at top of screen for score
        score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
        score_text.clear()
        score_text.cursor(0, 0)
        score_text.move(1, 1)
        score_text.text("{0}".format(score))

        # add text at top of screen for level
        level_text = stage.Text(width=20, height=15, font=None, palette=constants.LEVEL_PALETTE, buffer=None)
        level_text.clear()
        level_text.cursor(12, 0)
        level_text.move(1, 1)
        level_text.text("Level {0}".format(level))

        # V add layers here V
        game.layers = vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites + [score_text] + [level_text] + [background]
        game.render_block()

        # keys
        if keys & ugame.K_RIGHT != 0:  # right
            if right_button == constants.button_state["button_just_pressed"]:
                vilheleme.move(vilheleme.x + constants.SPRITE_SIZE, vilheleme.y)
                for ice_number in range(len(ice_sprites)):
                    if vilheleme.x > 0:
                        if stage.collide(ice_sprites[ice_number].x, ice_sprites[ice_number].y,
                                         ice_sprites[ice_number].x + 15, ice_sprites[ice_number].y + 15,
                                         vilheleme_list[0].x, vilheleme_list[0].y,
                                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                            if water_sprites[counter_r].x < 0:
                                water_sprites[counter_r].move(vilheleme.x - constants.SPRITE_SIZE, vilheleme.y)
                                counter_r += 1
                                score += 100
                for wall_number in range(len(wall_sprites)):
                    if vilheleme.x > 0:
                        if stage.collide(wall_sprites[wall_number].x, wall_sprites[wall_number].y,
                                         wall_sprites[wall_number].x + 15, wall_sprites[wall_number].y + 15,
                                         vilheleme_list[0].x, vilheleme_list[0].y,
                                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                            vilheleme.move(vilheleme.x - constants.SPRITE_SIZE, vilheleme.y)

            game.render_sprites(vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites)

        if keys & ugame.K_LEFT != 0:  # left
            if left_button == constants.button_state["button_just_pressed"]:
                if vilheleme.x > 16:
                    vilheleme.move(vilheleme.x - constants.SPRITE_SIZE, vilheleme.y)
                    for ice_number in range(len(ice_sprites)):
                        if vilheleme.x > 0:
                            if stage.collide(ice_sprites[ice_number].x, ice_sprites[ice_number].y,
                                             ice_sprites[ice_number].x + 15, ice_sprites[ice_number].y + 15,
                                             vilheleme_list[0].x, vilheleme_list[0].y,
                                             vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                                if water_sprites[counter_r].x < 0:
                                    water_sprites[counter_r].move(vilheleme.x + constants.SPRITE_SIZE, vilheleme.y)
                                    counter_r += 1
                                    score += 100

            game.render_sprites(vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites)
            game.tick()

        if keys & ugame.K_UP:  # up
            if up_button == constants.button_state["button_just_pressed"]:
                vilheleme.move(vilheleme.x, vilheleme.y - constants.SPRITE_SIZE)
                for ice_number in range(len(ice_sprites)):
                    if vilheleme.x > 0:
                        if stage.collide(ice_sprites[ice_number].x, ice_sprites[ice_number].y,
                                         ice_sprites[ice_number].x + 15, ice_sprites[ice_number].y + 15,
                                         vilheleme_list[0].x, vilheleme_list[0].y,
                                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                            if water_sprites[counter_r].x < 0:
                                water_sprites[counter_r].move(vilheleme.x, vilheleme.y + constants.SPRITE_SIZE)
                                counter_r += 1
                                score += 100
                for wall_number in range(len(wall_sprites)):
                    if vilheleme.x > 0:
                        if stage.collide(wall_sprites[wall_number].x, wall_sprites[wall_number].y,
                                         wall_sprites[wall_number].x + 15, wall_sprites[wall_number].y + 15,
                                         vilheleme_list[0].x, vilheleme_list[0].y,
                                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                            vilheleme.move(vilheleme.x, vilheleme.y + constants.SPRITE_SIZE)

            game.render_sprites(vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites)
            game.tick()

        if keys & ugame.K_DOWN:  # down
            if down_button == constants.button_state["button_just_pressed"]:
                vilheleme.move(vilheleme.x, vilheleme.y + constants.SPRITE_SIZE)
                for ice_number in range(len(ice_sprites)):
                    if vilheleme.x > 0:
                        if stage.collide(ice_sprites[ice_number].x, ice_sprites[ice_number].y,
                                         ice_sprites[ice_number].x + 15, ice_sprites[ice_number].y + 15,
                                         vilheleme_list[0].x, vilheleme_list[0].y,
                                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                            if water_sprites[counter_r].x < 0:
                                water_sprites[counter_r].move(vilheleme.x, vilheleme.y - constants.SPRITE_SIZE)
                                counter_r += 1
                                score += 100
                for wall_number in range(len(wall_sprites)):
                    if vilheleme.x > 0:
                        if stage.collide(wall_sprites[wall_number].x, wall_sprites[wall_number].y,
                                         wall_sprites[wall_number].x + 15, wall_sprites[wall_number].y + 15,
                                         vilheleme_list[0].x, vilheleme_list[0].y,
                                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                            vilheleme.move(vilheleme.x, vilheleme.y - constants.SPRITE_SIZE)


        if stage.collide(key_list[0].x, key_list[0].y,
                         key_list[0].x + 15, key_list[0].y + 15,
                         vilheleme_list[0].x, vilheleme_list[0].y,
                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
            key.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
            door.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        if stage.collide(finish_list[0].x, finish_list[0].y,
                         finish_list[0].x + 15, finish_list[0].y + 15,
                         vilheleme_list[0].x, vilheleme_list[0].y,
                         vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
            score += 1000
            counter_r = 0
            vilheleme_list = None
            water_sprites = None
            ice_sprites = None
            key_list = None
            door_list = None
            finish_list = None
            wall_sprites = None
            sound.play(key_collect)
            game_over(score)

            game.render_sprites(vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites)
            game.tick()

        for water_number in range(len(water_sprites)):
            if stage.collide(water_sprites[water_number].x, water_sprites[water_number].y,
                             water_sprites[water_number].x + 15, water_sprites[water_number].y + 15,
                             vilheleme_list[0].x, vilheleme_list[0].y,
                             vilheleme_list[0].x + 15, vilheleme_list[0].y + 15):
                game.render_sprites(vilheleme_list + wall_sprites + key_list + door_list + finish_list + water_sprites + ice_sprites)
                game.tick()
                final_score = score
                return final_score


def game_over(final_score):

    image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 3)

    sprites = []
    text = []
    text_game_over = []
    text_game_over_list = []
    text_game_over = stage.Text(width=29, height=12, font=None,
                       palette=constants.ICE_ICE_BABY_PALETTE, buffer=None)
    text_game_over.move(45, 35)
    text_game_over.text("Game Over")
    text.append(text_game_over)

    # V If game lags, change this V
    game = stage.Stage(ugame.display, constants.FPS)

    # add text at top of screen for score
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(16, 100)
    score_text.text("Final Score: {0}".format(final_score))

    restart_text = stage.Text(width=11, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    restart_text.clear()
    restart_text.cursor(0, 0)
    restart_text.move(35, 70)
    restart_text.text("Press Startto restart".format(final_score))

    game.layers = [score_text] + [text_game_over] + [restart_text]+ [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START != 0:
            return menu_scene()

if __name__ == "__main__":
    splash_scene()
