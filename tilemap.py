import pygame as pg
import pytmx
from settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class TiledMap:  #地圖載入
    def __init__(self, filename):
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
    def __init__(self, width, height):
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

    def update(self, target):
        #更新Camera的位置 跟著人物移動
        x = -target.rect.centerx + int(WIDTH/2)
        y = -target.rect.centery+ int(HEIGHT/2)
        x = min(0,x)
        y = min(0,y)
        x = max(-(self.width - WIDTH),x)
        y = max(-(self.height - HEIGHT),y)
        self.pos = vec(x,y)
        self.camera = pg.Rect(x,y,self.width,self.height)




