import pygame as pg
import funcs

BLACK = pg.Color('black')
WHITE = pg.Color('white')
RED = pg.Color('red')
GREEN = pg.Color('green')
GREY = pg.Color('grey')

rng = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
       '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']


heroWalkRight = [pg.transform.scale(funcs.load_image('Walk00{}.png'.format(i), 'sprite/Walk', -1), [300, 300]) for i in rng]
heroWalkLeft = [pg.transform.flip(pg.transform.scale(funcs.load_image('Walk00{}.png'.format(i),
                                          'sprite/Walk', -1), [300, 300]), True, False) for i in rng]

heroStandLeft = [pg.transform.flip(pg.transform.scale(funcs.load_image('Stand00{}.png'.format(i), 'sprite/Stand', -1), [300, 300]), True, False) for i in rng]
heroStandRight = [pg.transform.scale(funcs.load_image('Stand00{}.png'.format(i), 'sprite/Stand', -1), [300, 300]) for i in rng]


heroFallLeft = [pg.transform.flip(pg.transform.scale(funcs.load_image('JNF00{}.png'.format(str(i)), 'sprite/Fall', -1), [300, 300]), True, False) for i in range(13, 22)]
heroFallRight = [pg.transform.scale(funcs.load_image('JNF00{}.png'.format(str(i)), 'sprite/Fall', -1), [300, 300]) for i in range(13, 22)]

heroJumpLeft = [pg.transform.flip(pg.transform.scale(funcs.load_image('JNF00{}.png'.format(str(i)), 'sprite/Jump', -1), [300, 300]), True, False) for i in rng + ['21']]
heroJumpRight = [pg.transform.scale(funcs.load_image('JNF00{}.png'.format(str(i)), 'sprite/Jump', -1), [300, 300]) for i in rng + ['21']]

plat = pg.transform.scale(funcs.load_image('line_r.png', '128textures', -1), [850, 80])
