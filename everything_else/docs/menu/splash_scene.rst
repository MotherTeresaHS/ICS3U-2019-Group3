.. _splash_scene:

Splash Scene
============

The splash screen displays the MT Studios logo and the creators of Ice Ice Baby, Liam and Joseph. It takes 2 seconds for the splash screen to transition to the menu screen.

.. code-block:: python

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

        game = stage.Stage(ugame.display, constants.FPS)
        game.layers = text + sprites + [background]
        game.render_block()

        image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")
        background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                                constants.SCREEN_GRID_Y)
        for x_location in range(constants.SCREEN_GRID_X):
            for y_location in range(constants.SCREEN_GRID_Y):
                background.tile(x_location, y_location, 15)
        sound.play(boot_up)
        time.sleep(2)
        menu_scene()
        game.tick()

Then it goes on to the menu scene.