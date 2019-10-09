#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# Creates a sprite on pybadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# a list of sprites that will be updated every frame
sprites = []


def main():
    # this function sets the background

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # create a sprite
    # parameters (image_bank_1, image # in bank, x, y)
    alien = stage.Sprite(image_bank_1, 9, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 5, 74, 56)
    sprites.insert(0, ship)  # insert at top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = sprites + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    while True:
         # get user inputs
        keys = ugame.buttons.get_pressed()
        # print(keys)
        
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 2)
            pass
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 2)
            pass
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 2, ship.y)
            pass
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 2, ship.y)
            pass
        # update game logic

        # redraw sprtie list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()
