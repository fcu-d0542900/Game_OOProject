# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 03:58:38 2019

@author: YURU
"""

import pygame as pg
import sys
from os import path
from random import randint
from Structure import *

class RPGGame(AbstractGame):
    
    def __init__(self):
        # Weapon settings
        self.BARREL_OFFSET = vec(30, 10)
        self.BULLET_IMG = 'bullet.png'
        self.BULLET_SPEED = 1000
        self.BULLET_RATE = 150
        self.GUN_SPREAD = 5
        self.DAMAGE = 20
        self.last_shot = 0
        AbstractGame.__init__(self)
    
    def load_data(self):  #載入所有圖片
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.map.setFileName(self.setting.MAP)  #地圖
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, self.setting.PLAYER_IMG)).convert_alpha()
        self.treasure_img = pg.image.load(path.join(img_folder, self.setting.TREASURE_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder, self.setting.BULLET_IMG)).convert_alpha()
        self.zombie_img = pg.image.load(path.join(img_folder, self.setting.ZOMBIE_IMG)).convert_alpha()

    def new(self):  #角色初始位置
        self.win = True
        self.treasures = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.zombies = pg.sprite.Group()
        self.camera.setCamera(self.map.width, self.map.height)

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                print(tile_object.x, tile_object.y)
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name == 'treasure':
                x, y = randint(30,1570), randint(30,1570)
                self.treasure = Treasure(self, x, y, tile_object.width, tile_object.height)
            if tile_object.name == 'zombie':
                Zombie(self,tile_object.x, tile_object.y)

    def run(self):  #時間
        self.playing = True
        start_ticks = pg.time.get_ticks()
        while self.playing:
            seconds=(pg.time.get_ticks()-start_ticks) / 1000 
            time_left = self.setting.GAMETIME - seconds
            if time_left <= 0:
                self.win = False
                break
            self.dt = self.clock.tick(self.setting.FPS) / 1000.0  
            self.events()
            self.update()
            self.draw(time_left)
            
    def mouse(self):
       # self.mouse_pos = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0]:
            now = pg.time.get_ticks()
            if now - self.last_shot > self.BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + self.BARREL_OFFSET.rotate(-self.rot)
                Bullet(self.game, pos, dir)

    def update(self):  #更新角色
        self.mouse()
        self.treasure.update()
        self.player.update()
        for bullet in self.bullets:
            bullet.update()
        for zombie in self.zombies:
            zombie.update()
        self.camera.update(self.player)

    def draw(self, time_left):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        self.player.draw_health()
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        self.screen.blit(self.treasure.image, self.camera.apply(self.treasure))
        for bullet in self.bullets:
            self.screen.blit(bullet.image, self.camera.apply(bullet))
        for zombie in self.zombies:
            zombie.draw_health()
            self.screen.blit(zombie.image, self.camera.apply(zombie))

        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 50)
        textsurface = myfont.render(str(int(time_left))+' sec', False, (255, 0, 0))
        self.screen.blit(textsurface,(1000 ,self.setting.HEIGHT/10))

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def gg(self):
        self.screen.fill((0,0,0))
        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 80)
        if self.win:
            textsurface = myfont.render('You win!!!', False, (255, 0, 0))
        else:
            textsurface = myfont.render('You lose!!!', False, (255, 0, 0))

        self.screen.blit(textsurface,(300 ,self.setting.HEIGHT/3))
        pg.display.flip()
        pg.event.wait()
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False


if __name__ == '__main__':  #遊戲執行
    g = Game()
    while True:
        g.new()  #遊戲初始
        pg.mixer.music.load('music/faded.mp3')
        #pg.mixer.music.play(0)
        g.run()  #遊戲運作
        #pg.mixer.music.stop()
        g.gg()  #遊戲結束
        