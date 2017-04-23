'''
Created on 23.04.2017

@author: Flex
'''
CONST_ENEMY_DAMAGE = [1, 2, 3, 4, 5]
CONST_ENEMY_RANGE = [10, 20, 30, 40, 50]
CONST_ENEMY_SPEED = [1, 3, 4, 2, 3]
CONST_ENEMY_LOOT = [1, 2, 3, 4, 5]
CONST_ENEMY_HEALTH = [100, 110, 120, 130, 140]

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

        
    
    
    
        