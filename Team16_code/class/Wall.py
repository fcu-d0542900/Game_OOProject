# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:03:40 2019

@author: User
"""

import pygame as pg
from Setting import *
    
class Wall(pg.sprite.Sprite,Setting):
    
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        Setting.__init__(self)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        
