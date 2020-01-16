.. _background:

Background
==========

In the begininning of every function what uses a background, you must reference the image bank you wish to use. In this instance, its image_bank_1

.. code-block:: python

    image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")

To code the background of the splash screen, you must type this code after the reference code:

.. code-block:: python

    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 15)

In your menu sceen, after referencing which image bank you will use, you must type this:

.. code-block:: python

    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)


For level 1 of your game, you must type this code after referencing the image bank you choose to use:

.. code-block:: python

    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 3)
