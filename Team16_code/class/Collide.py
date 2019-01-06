# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:17:39 2019

@author: YURU
"""

import pygame as pg
from Setting import *
from Treasure import *

class Collide(pg.sprite.Sprite):
    '''
    def collide_hit_rect(one, two):
        return one.hit_rect.colliderect(two.rect)
    '''
    def got_hit(self,sprite, group):
        hits = pg.sprite.spritecollide(sprite,group,False)
        if hits:
           sprite.health -= self.DAMAGE
           if isinstance(hits[0],Bullet):
               hits[0].kill()
           if sprite.health<0 & isinstance(sprite,Player):
               sprite.game.win = False
               sprite.game.playing = False
    
    def collide(self,sprite, group, dir):
        #檢查x方向的碰撞
        if dir == 'x':
            hits = pg.sprite.spritecollide(sprite, group, False)
            if hits:
                if hits[0].rect.centerx > sprite.hit_rect.centerx:
                    sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
                elif hits[0].rect.centerx < sprite.hit_rect.centerx:
                    sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
                sprite.hit_rect.centerx = sprite.pos.x
                sprite.vel.x = 0
                if isinstance(hits[0], Treasure):
                    sprite.game.win = True
                    sprite.game.playing = False
        #檢查y方向的碰撞
        if dir == 'y':
            hits = pg.sprite.spritecollide(sprite, group, False)
            if hits:
                if hits[0].rect.centery > sprite.hit_rect.centery:
                    sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
                elif hits[0].rect.centery < sprite.hit_rect.centery:
                    sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
                sprite.hit_rect.centery = sprite.pos.y
                sprite.vel.y = 0
                if isinstance(hits[0], Treasure):
                    sprite.game.win = True
                    sprite.game.playing = False