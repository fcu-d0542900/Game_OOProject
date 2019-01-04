import pygame as pg
vec = pg.math.Vector2

'''參數設定'''

class Setting:

    def __init__(self):	
        
        # game settings
        self.WIDTH = 64 * 20  
        self.HEIGHT = 64 * 10 
        self.FPS = 60
        self.TILESIZE = 64
        self.GAMETIME = 60
        self.TITLE = 'Maze'
        self.MAP = 'Maze1.tmx'
        
        # Player settings
        self.PLAYER_IMG = 'manBlue_gun.png'
        self.PLAYER_SPEED = 3
        self.PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
        self.PLAYER_HEALTH = 1000
        
        # Weapon settings
        self.BARREL_OFFSET = vec(30, 10)
        self.BULLET_IMG = ''
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
    
    def setPlayer(self):
        pass
    
    def setTitle(self):
        pass
    
    def setMap(self):
        pass
    
    def setTreasure(self):
        pass
			
