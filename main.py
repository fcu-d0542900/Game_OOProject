import pygame as pg
from os import path
from MazeGame import *
from RPGGame import *



if __name__ == '__main__':  #遊戲執行
    g = MazeGame()
    #g = RPGGame()
    while True:
        g.new()  #遊戲初始
        pg.mixer.music.load('music/Old MacDonald.mp3')
        pg.mixer.music.play(0)
        g.run()  #遊戲運作
        pg.mixer.music.stop()
        g.gg()  #遊戲結束
        