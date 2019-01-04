import pygame as pg
from os import path
from MazeGame import *
from RPGGame import *



if __name__ == '__main__':  #遊戲執行
<<<<<<< HEAD
    #g = MazeGame()
    g = RPGGame()
=======
    while True:
        c = input("選擇想玩遊戲: 1.迷宮 2.打怪吃寶物  >>")
        if c in ('1','2'):
            break
        print("請輸入 1 或 2")
    if c == '1':
        g = MazeGame()
    else:
        g = RPGGame()
>>>>>>> 39602abcc0a611c8e61fd118d1bb8f94adf81eed
    while True:
        g.new()  #遊戲初始
        pg.mixer.music.load('music/Old MacDonald.mp3')
        #pg.mixer.music.play(0)
        g.run()  #遊戲運作
        #pg.mixer.music.stop()
        g.gg()  #遊戲結束
        