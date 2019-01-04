# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:38:35 2019

@author: User
"""
import pygame as pg
vec = pg.math.Vector2
from Setting import *

class Tresure(pg.sprite.Sprite,Setting):
    
    def __init__(self, game, x, y, w, h):
        Setting.__init__(self)
        pg.sprite.Sprite.__init__(self, self.groups)
        
        self.groups = game.treasures
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
        self.COLLIDE.collide(self, self.game.walls, 'x')
        self.COLLIDE.collide(self, self.game.walls, 'y')
        self.rect.center = self.pos


