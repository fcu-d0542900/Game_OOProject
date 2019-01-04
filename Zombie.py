# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:15:33 2019

@author: User
"""

import pygame as pg

class Zombie(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):

        self.groups = game.zombies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.zombie_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = ZOMBIE_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y)
        self.rot = 0
        self.health = ZOMBIE_HEALTH
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
    def op(self):
        super.op()
        update()        
        
    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        #self.image = pg.transform.rotate(self.game.zombie_img, self.rot)
        self.rect = self.image.get_rect()
        move = (self.game.player.pos - self.pos)
        move.x, move.y = ZOMBIE_SPEED *  move.x / math.sqrt(move.x ** 2 + move.y ** 2), ZOMBIE_SPEED * move.y / math.sqrt(move.x ** 2 + move.y ** 2)
        self.pos += move
        self.hit_rect.centerx = self.pos.x
        collide(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        got_hit(self, self.game.bullets)
        if self.health <= 0:
            x, y = randint(30,1570), randint(30,1570)
            self.rect.center = (x,y)
            self.pos = vec(x, y)
            self.health = ZOMBIE_HEALTH
            #self.kill()
    
    def draw_health(self):
        if self.health > 60:
            col = (0,255,0)
        elif self.health > 30:
            col = (0,255,255)
        else:
            col = (255,0,0)
        width = int(self.rect.width * self.health / ZOMBIE_HEALTH)
        self.health_bar = pg.Rect(0, 0, width, 7)
        if self.health < ZOMBIE_HEALTH:
            pg.draw.rect(self.image, col, self.health_bar)
