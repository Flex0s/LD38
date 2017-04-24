'''
Created on 23.04.2017

@author: Flex
'''
ENEMY_INFO = ['low', 'medium', 'hard', 'flying', 'boss']
CONST_ENEMY_DAMAGE = [0.5, 0.6, 1, 0.6, 5]
CONST_ENEMY_RANGE = [40, 40, 40, 40, 40]
CONST_ENEMY_SPEED = [0.4, 0.8, 0.5, 0.6, 0.2]
CONST_ENEMY_LOOT = [2, 3, 5, 7, 35]
CONST_ENEMY_HEALTH = [30, 16, 50, 40, 300]
CONST_ENEMY_COOLDOWN = [350,700,50,400,350]

from random import randint


class enemy(object):
    '''
    classdocs
    '''


    def __init__(self,name, type, path):
        '''
        Constructor
        '''
        self.name = name
        self.type = type
        self.set_health(CONST_ENEMY_HEALTH[type])
        self.set_location((0,0))
        self.path = path
        self.sector = 0
        self.target = (0,0)
        self.loot = CONST_ENEMY_LOOT[type]
        self.cooldown = 0
        self.inrange = False
    
    def set_health(self, health):
        self.health = health
    
    def get_health(self):
        return self.health

    def get_name(self):
        return self.name
     
    def set_location(self, location):
        self.location = location
               
    def get_location(self):
        return self.location
    
    def set_sector(self, sector):
        self.sector = sector
        
    def get_sector(self):
        return self.sector
    
    def get_type(self):
        return self.type
    
    def get_target(self):
        return self.target
    
    def set_target(self,target):
        #in percent
        random = 2
        self.target = (target[0] + randint(-1*random,random) * target[0]/100 , target[1] + randint(-1*random,random) * target[1]/100)
    
    def get_loot(self):
        return self.loot

    def get_path(self):
        return self.path
    
    def reset_cooldown(self,actual_time):
        self.cooldown = actual_time + CONST_ENEMY_COOLDOWN[self.type]
    
    def get_cooldown(self):
        return self.cooldown
    
    def set_inrange(self, in_range):
        self.inrange = in_range
    
    def get_inrange(self):
        return self.inrange
    
        