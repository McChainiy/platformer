import pygame as pg
import CONSTS
import funcs
import classes as cl


def draw_sprites():
    screen.fill(CONSTS.GREY)
    cl.heros.draw(screen)
    cl.plats.draw(screen)
    cl.borders.draw(screen)
    pg.display.flip()

running = True

pg.init()

width, height = size = [1080, 720]
screen = pg.display.set_mode(size)


hero = cl.Hero([0, 0], cl.heros)
platform = cl.Platform([0, 640], CONSTS.plat, cl.plats)


ADDEVENT = 10

pg.time.set_timer(ADDEVENT, 40)

pg.mouse.set_visible(True)

screen.fill(CONSTS.WHITE)

pg.display.flip()

clock = pg.time.Clock()

speed = 10

while running:
    clock.tick(60)
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT:
            funcs.terminate()
        if keys[pg.K_LEFT]:
            hero.move_left(speed)
        elif keys[pg.K_RIGHT]:
            hero.move_right(speed)
        else:
            hero.move_stop()
        if keys[pg.K_SPACE]:
            hero.jump()
    hero.update()
    draw_sprites()

