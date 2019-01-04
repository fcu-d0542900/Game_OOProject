import pygame as pg
import sys
from os import path
from Setting import *

class AbstractGame:

    def __init__(self):
        pg.init()
        self.setting = Setting()
        self.screen = pg.display.set_mode((setting.WIDTH, setting.HEIGHT))
        pg.display.set_caption(setting.TITLE)
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


        