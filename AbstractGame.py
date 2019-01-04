import pygame as pg
import sys
from os import path
from Setting import *
from sprites import *
from tilemap import *
from random import randint



class AbstractGame:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
		self.setting=Setting() 
		    
    def quit(self):
        pg.quit()
        sys.exit()

    @abstractmethod
    def load_data(self):  #載入所有圖片
        pass

    @abstractmethod
    def new(self):  #角色初始位置
        pass

    @abstractmethod
    def run(self):  #時間
        pass

    @abstractmethod
    def update(self):  #更新角色
        pass
        
	
        
    @abstractmethod
    def gg(self):
        pass


        