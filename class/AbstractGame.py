import pygame as pg
import sys
from os import path
from Setting import *
from TiledMap import *
from Camera import *

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


        