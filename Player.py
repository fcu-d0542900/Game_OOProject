# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:13:10 2019

@author: User
"""

import pygame as pg

class Player(pg.sprite.Sprite,Setting):
    
    def __init__(self, game, x, y):
  
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y)
        self.vel = vec(0,0)
        self.rot = 0
        self.health = PLAYER_HEALTH
        self.last_shot = 0
    
    def op(self):
        super.op()
        update()

        
    def get_mouse(self):
        self.mouse_pos = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0]:
            now = pg.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
                Bullet(self.game, pos, dir)

    '''取得按下的按鍵, 並判斷移動方向'''
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.pos[0] -= 3
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.pos[0] += 3
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.pos[1] -= 3
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.pos[1] += 3

    '''取得轉動角度值'''
    def get_angle(self):
        direction = self.mouse_pos - self.game.camera.pos - self.pos
        return math.atan2(-direction[1],direction[0])

    def update(self):
        self.get_keys()
        self.get_mouse()
        
        #角色面朝著滑鼠方向
        self.rot = self.get_angle() * 180 / math.pi 
        self.image = pg.transform.rotate(self.game.player_img, self.rot)

        #鍵盤方向
        self.rect = self.image.get_rect()
        collide(self, self.game.treasures, 'x')
        collide(self, self.game.treasures, 'y')
        self.hit_rect.centerx = self.pos.x
        collide(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide(self, self.game.walls, 'y')
        self.rect.center = self.pos
        got_hit(self, self.game.zombies)

    def draw_health(self):
        if self.health > 800:
            col = (0,255,0)
        elif self.health > 300:
            col = (0,255,255)
        else:
            col = (255,0,0)
        width = int(self.rect.width * self.health / PLAYER_HEALTH)
        self.health_bar = pg.Rect(0, 0, width, 7)
        if self.health < PLAYER_HEALTH:
            pg.draw.rect(self.image, col, self.health_bar)