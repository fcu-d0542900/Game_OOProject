# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 02:57:19 2019

@author: YURU
"""

import pygame as pg
import pytmx
import sys
import math
from random import uniform,randint
vec = pg.math.Vector2

class AbstractGame:
    
    def __init__(self):
        pg.init()
        self.setting = Setting()
        self.map = TiledMap()
        self.camera = Camera()
        print(self.setting.WIDTH, self.setting.HEIGHT,self.setting.TITLE)
        self.screen = pg.display.set_mode((self.setting.WIDTH, self.setting.HEIGHT))
        pg.display.set_caption(self.setting.TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
		    
    def quit(self):
        pg.quit()
        sys.exit()
        
    def events(self):
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def load_data(self):  #載入所有圖片
        pass

    def new(self):  #角色初始位置
        pass

    def run(self):  #時間
        pass

    def update(self):  #更新角色
        pass
    
    def gg(self):
        pass
    
class TiledMap:  #地圖載入
    def __init__(self):
        pass
    
    def setFileName(self, filename):
        tm = pytmx.load_pygame(filename)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
    
class Camera:  #顯示部分地圖
    
    def __init__(self):
        self.setting = Setting()
        
    def setCamera(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.pos = vec(0,0)

    def apply(self, entity):
        #物件在鏡頭中的移動
        return entity.rect.move(self.camera.topleft)
       
    def apply_rect(self, rect):
        #地圖在鏡頭中的移動
        return rect.move(self.camera.topleft)

    '''Camera update 用到setting'''
    def update(self, target):
        #更新Camera的位置 跟著人物移動
        x = -target.rect.centerx + int(self.setting.WIDTH/2)
        y = -target.rect.centery + int(self.setting.HEIGHT/2)
        x = min(0,x)
        y = min(0,y)
        x = max(-(self.width - self.setting.WIDTH),x)
        y = max(-(self.height - self.setting.HEIGHT),y)
        self.pos = vec(x,y)
        self.camera = pg.Rect(x,y,self.width,self.height)
        
class Setting:

    def __init__(self):	
        self.COLLIDE = None
        
        # game settings
        self.WIDTH = 64 * 20  
        self.HEIGHT = 64 * 10 
        self.FPS = 60
        self.TILESIZE = 64
        self.GAMETIME = 60
        self.TITLE = 'Maze'
        self.MAP = 'RPG.tmx'
        
        # Player settings
        self.PLAYER_IMG = 'manBlue_gun.png'
        self.PLAYER_SPEED = 3
        self.PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
        self.PLAYER_HEALTH = 1000
        
        # Weapon settings
        self.BARREL_OFFSET = vec(30, 10)
        self.BULLET_IMG = 'nobullet.png'
        self.BULLET_SPEED = 1000
        self.BULLET_RATE = 150
        self.GUN_SPREAD = 5
        self.DAMAGE = 20
        
        # Mob settings
        self.ZOMBIE_IMG = 'monster.png'
        self.ZOMBIE_SPEED = 1
        self.ZOMBIE_HIT_RECT = pg.Rect(0, 0, 30, 30)
        self.ZOMBIE_HEALTH = 100
        
        # Treasure
        self.TREASURE_IMG = 'treasure.png'
        
    
    def hasCollide(self):
        if self.COLLIDE == None :
            self.COLLIDE = Collide()
    
    def setPlayer(self):
        pass
    
    def setTitle(self):
        pass
    
    def setMap(self):
        pass
    
    def setTreasure(self):
        pass


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class Collide(pg.sprite.Sprite,Setting):
    
    def __init__(self):
        Setting.__init__(self)

    def got_hit(self,sprite, group):
        hits = pg.sprite.spritecollide(sprite,group,False,collide_hit_rect)
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
            hits = pg.sprite.spritecollide(sprite, group, False,collide_hit_rect)
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
            hits = pg.sprite.spritecollide(sprite, group, False,collide_hit_rect)
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
                    
                    
class Player(pg.sprite.Sprite,Setting):
    
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        Setting.__init__(self)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = self.PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y)
        self.vel = vec(0,0)
        self.rot = 0
        self.health = self.PLAYER_HEALTH
        self.last_shot = 0
    
        
    def get_mouse(self):
        self.mouse_pos = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0]:
            now = pg.time.get_ticks()
            if now - self.last_shot > self.BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + self.BARREL_OFFSET.rotate(-self.rot)
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
        self.hasCollide()
        self.COLLIDE.collide(self, self.game.treasures, 'x')
        self.COLLIDE.collide(self, self.game.treasures, 'y')
        self.hit_rect.centerx = self.pos.x
        self.COLLIDE.collide(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        self.COLLIDE.collide(self, self.game.walls, 'y')
        self.rect.center = self.pos
        self.COLLIDE.got_hit(self, self.game.zombies)

    def draw_health(self):
        if self.health > 800:
            col = (0,255,0)
        elif self.health > 300:
            col = (0,255,255)
        else:
            col = (255,0,0)
        width = int(self.rect.width * self.health / self.PLAYER_HEALTH)
        self.health_bar = pg.Rect(0, 0, width, 7)
        if self.health < self.PLAYER_HEALTH:
            pg.draw.rect(self.image, col, self.health_bar)
            
class Zombie(pg.sprite.Sprite,Setting):
    
    def __init__(self, game, x, y):

        self.groups = game.zombies
        pg.sprite.Sprite.__init__(self, self.groups)
        Setting.__init__(self)
        self.game = game
        self.image = game.zombie_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = self.ZOMBIE_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y)
        self.rot = 0
        self.health = self.ZOMBIE_HEALTH
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)  
        
    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        #self.image = pg.transform.rotate(self.game.zombie_img, self.rot)
        self.rect = self.image.get_rect()
        move = (self.game.player.pos - self.pos)
        move.x, move.y = self.ZOMBIE_SPEED *  move.x / math.sqrt(move.x ** 2 + move.y ** 2), self.ZOMBIE_SPEED * move.y / math.sqrt(move.x ** 2 + move.y ** 2)
        self.pos += move
        self.hit_rect.centerx = self.pos.x
        self.hasCollide()
        self.COLLIDE.collide(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        self.COLLIDE.collide(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        self.COLLIDE.got_hit(self, self.game.bullets)
        if self.health <= 0:
            #x, y = randint(30,1570), randint(30,1570)
            #self.rect.center = (x,y)
            #self.pos = vec(x, y)
            #self.health = self.ZOMBIE_HEALTH
            self.kill()
    
    def draw_health(self):
        if self.health > 60:
            col = (0,255,0)
        elif self.health > 30:
            col = (0,255,255)
        else:
            col = (255,0,0)
        width = int(self.rect.width * self.health / self.ZOMBIE_HEALTH)
        self.health_bar = pg.Rect(0, 0, width, 7)
        if self.health < self.ZOMBIE_HEALTH:
            pg.draw.rect(self.image, col, self.health_bar)

class Bullet(pg.sprite.Sprite,Setting):
    
    def __init__(self, game, pos, dir):
        
        self.groups = game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        Setting.__init__(self)
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


class Treasure(pg.sprite.Sprite,Setting):
    
    def __init__(self, game, x, y, w, h):
        self.groups = game.treasures
        
        Setting.__init__(self)
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
        self.hasCollide()
        self.COLLIDE.collide(self, self.game.walls, 'x')
        self.COLLIDE.collide(self, self.game.walls, 'y')
        self.rect.center = self.pos
        
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
        

