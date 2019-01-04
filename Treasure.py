# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:38:35 2019

@author: User
"""

import pygame as pg

class Treasure(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.treasures
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.treasure_img
        self.game = game
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(x,y)
        self.vel = vec(0,0)
        self.rect.center = vec(x,y)

    def update(self):
        self.image = pg.transform.rotate(self.game.treasure_img, 0)
        self.rect = self.image.get_rect()
        collide(self, self.game.walls, 'x')
        collide(self, self.game.walls, 'y')
        self.rect.center = self.pos

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
