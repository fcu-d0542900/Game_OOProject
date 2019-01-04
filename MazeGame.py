# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:45:07 2019

@author: YURU
"""

import pygame as pg
import sys
from os import path
from AbstractGame import * 
from Player import * 
from Wall import *
from Treasure import * 
from random import randint
from Setting import *


class MazeGame(AbstractGame):
    
    def load_data(self):  #載入所有圖片
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.map.setFileName(self.setting.MAP)  #地圖
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, self.setting.PLAYER_IMG)).convert_alpha()
        self.treasure_img = pg.image.load(path.join(img_folder, self.setting.TREASURE_IMG)).convert_alpha()

    def new(self):  #角色初始位置
        self.win = True
        self.treasures = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.camera.setCamera(self.map.width, self.map.height)

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                print(tile_object.x, tile_object.y)
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'treasure':
                self.treasure = Treasure(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

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

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):  #更新角色
        self.treasure.update()
        self.player.update()
        self.camera.update(self.player)

    def draw(self, time_left):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        self.screen.blit(self.treasure.image, self.camera.apply(self.treasure))

        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 50)
        textsurface = myfont.render(str(int(time_left))+' sec', False, (255, 0, 0))
        self.screen.blit(textsurface,(1000 ,HEIGHT/10))

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

        self.screen.blit(textsurface,(300 ,HEIGHT/3))
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