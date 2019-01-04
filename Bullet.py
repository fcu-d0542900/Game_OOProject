# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:26:59 2019

@author: User
"""

import pygame as pg
from Setting import *

class Bullet(pg.sprite.Sprite,Setting):
    
    def __init__(self, game, pos, dir):
        
        self.groups = game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-self.GUN_SPREAD, self.GUN_SPREAD)
        self.vel = dir.rotate(spread) * self.BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()
        
        
    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()
