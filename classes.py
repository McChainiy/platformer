import pygame as pg
import CONSTS

heros = pg.sprite.Group()
plats = pg.sprite.Group()
borders = pg.sprite.Group()


class Platform(pg.sprite.Sprite):
    def __init__(self, coords, texture, group):
        super().__init__(group)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        self.top = Border(self, 'top', borders)


class Border(pg.sprite.Sprite):
    def __init__(self, owner, type, group, rect=[]):
        self.owner = owner
        self.type = type
        self.owner_coords = [self.owner.rect.x, self.owner.rect.y]
        super().__init__(group)
        if type == 'bottom':
            self.rect = pg.Rect(owner.rect.x, owner.rect.y + owner.rect.height - 1, owner.rect.width, 1)
        elif type == 'right':
            self.rect = pg.Rect(owner.rect.x + owner.rect.width - 1, owner.rect.y, 1, owner.rect.height)
        elif type == 'left':
            self.rect = pg.Rect(owner.rect.x + 1, owner.rect.y, 1, owner.rect.height)
        elif type == 'top':
            self.rect = pg.Rect(owner.rect.x, owner.rect.y + 1, owner.rect.width, 1)
        elif type == 'custom':
            self.rect = pg.Rect(rect[0], rect[1], rect[2], rect[3])
        self.image = pg.Surface((self.rect.w, self.rect.h), pg.SRCALPHA, 32)
        self.image.fill(CONSTS.GREEN)

    def check_owner(self):
        if self.type == 'right':
            self.rect.x = self.owner.rect.x + self.owner.rect.width
            self.rect.y = self.owner.rect.y

        elif self.type == 'bottom':
            self.rect.x = self.owner.rect.x
            self.rect.y = self.owner.rect.y + self.owner.rect.height

        elif self.type in ['left', 'top']:
            self.rect.x = self.owner.rect.x
            self.rect.y = self.owner.rect.y

        elif self.type == 'custom':
            self.rect.x += self.owner.rect.x - self.owner_coords[0]
            self.rect.y += self.owner.rect.y - self.owner_coords[1]
        self.owner_coords = [self.owner.rect.x, self.owner.rect.y]

        #print(self.rect.x, self.rect.y)


class Hero(pg.sprite.Sprite):
    def __init__(self, coords, group):
        super().__init__(group)
        self.image = CONSTS.heroStandRight[0]
        self.rect = self.image.get_rect()
        self.animWalkCount = 0
        self.animStandCount = 0
        self.animJumpCount = 0
        self.animLandCount = 0
        self.fallSpeed = 0
        self.jumpSpeed = 56
        self.left = False
        self.right = False
        self.was_left = False
        self.was_right = True
        self.isJump = False
        self.isLand = False
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        self.bottom = Border(self, 'custom', borders, rect=[100, 230, 100, 1])

    def move_left(self, speed):
        self.rect.x -= speed
        if not (self.isJump or self.isLand):
            self.left = True
            self.right = False
            self.animWalkCount += 1
            self.animStandCount = 0
        else:
            self.was_left = True
            self.was_right = False
        #self.update()

    def move_right(self, speed):
        self.rect.x += speed
        if not (self.isJump or self.isLand):
            self.left = False
            self.right = True
            self.animWalkCount += 1
            self.animStandCount = 0
        else:
            self.was_right = True
            self.was_left = False
        #self.update()

    def move_stop(self):
        if self.left:
            self.was_left = True
            self.was_right = False
        elif self.right:
            self.was_right = True
            self.was_left = False
        self.left = False
        self.right = False
        self.animWalkCount = 0
        self.animStandCount += 1
        #self.update()

    def jump(self):
        for plat in plats:
            if pg.sprite.collide_rect(self.bottom, plat.top) and not self.isLand:
                self.isJump = True
                self.rect.y -= 1
                self.bottom.check_owner()
                break

    def update(self):
        for plat in plats:
            if pg.sprite.collide_rect(self.bottom, plat.top):
                self.isLand = False
                if self.animWalkCount >= 20:
                    self.animWalkCount = 0
                if self.animStandCount >= 20:
                    self.animStandCount = 0
                if self.left:
                    self.image = CONSTS.heroWalkLeft[self.animWalkCount]
                elif self.right:
                    self.image = CONSTS.heroWalkRight[self.animWalkCount]
                else:
                    if self.was_right:
                        self.image = CONSTS.heroStandRight[self.animStandCount]
                    elif self.was_left:
                        self.image = CONSTS.heroStandLeft[self.animStandCount]
                self.fallSpeed = 0
                self.jumpSpeed = 56
                break
        else:
            #print(self.isJump)
            if self.isJump:
                self.animJumpCount += 1
                if self.animJumpCount >= 21:
                    self.animJumpCount = 0
                if self.was_right:
                    self.image = CONSTS.heroJumpRight[self.animJumpCount]
                else:
                    self.image = CONSTS.heroJumpLeft[self.animJumpCount]
                for i in range(self.jumpSpeed//4):
                    self.rect.y -= 1
                self.jumpSpeed -= 1
                if self.jumpSpeed <= 0:
                    self.isJump = False
            else:
                self.isLand = True
                self.isJump = False
                self.animLandCount += 1
                if self.animLandCount >= 9:
                    self.animLandCount = 0
                if self.was_right:
                    self.image = CONSTS.heroFallRight[self.animLandCount]
                else:
                    self.image = CONSTS.heroFallLeft[self.animLandCount]
                run = True
                for i in range(self.fallSpeed):
                    if not run:
                        break
                    self.rect.y += 1
                    self.bottom.check_owner()
                    for plat in plats:
                        if pg.sprite.collide_rect(self.bottom, plat.top):
                            run = False
                            break
                    #print(self.rect.y)
                self.fallSpeed += 1
        self.bottom.check_owner()


