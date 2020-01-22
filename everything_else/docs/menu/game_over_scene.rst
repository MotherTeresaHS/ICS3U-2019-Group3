.. _game_over_scene:

Game Over Scene
===============

The game moves to the game over scene when the player either wins the game or makes contact with the water. The game over scene displays the final score at the time of death. Press the start button to restart from the menu scene.

.. code-block:: python

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
        text_game_over = stage.Text(width=29, height=12, font=None, palette=constants.ICE_ICE_BABY_PALETTE, buffer=None)
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

The game then goes back to the menu screen