.. _vilheleme:

Vilheleme
==========

Vilheleme is the little penguin controlled by the D pad. When a player touches a key on the D pad, Vilheleme moves in the corrosponding direction. This is the code to make vilheleme show up:

.. code-block:: python

    def lvl_1():
        vilheleme_list = []

        image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")

        # create vilheleme
        vilheleme = stage.Sprite(image_bank_1, 2, 16, 64)
        vilheleme_list.append(vilheleme)  # insert at the top of sprite list
