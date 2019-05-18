import pygame as pg
import os
import sys
import CONSTS


def terminate():
    pg.quit()
    sys.exit()


def load_image(name, dir, colorkey=None):
    fullname = os.path.join(dir, name)
    try:
        image = pg.image.load(fullname)
        if colorkey == -2:
            image.convert_alpha()
        elif colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image
    except pg.error:
        print('error', name)



def highpoly_load(coords, texture):
    pass