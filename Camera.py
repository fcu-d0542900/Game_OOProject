# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:58:04 2019

@author: YURU
"""

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