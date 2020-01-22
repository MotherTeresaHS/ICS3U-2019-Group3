.. _start_scene:

Start Scene
===========

The menu screen offers the option for the player to press A to begin playing the game:

.. code-block:: python

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

        # get sound ready
        press_start_audio = open("press_start_audio.wav", 'rb')
        sound = ugame.audio
        sound.stop()
        sound.mute(False)

        lvl1 = None
        final_score = None

        while True:
            keys = ugame.buttons.get_pressed()
            if keys & ugame.K_X != 0:
                final_score = 0
                sound.play(press_start_audio)
                time.sleep(1)
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

Then the game goes to level 1.