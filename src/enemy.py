'''
Created on 23.04.2017

@author: Flex
'''

class enemy(object):
    '''
    classdocs
    '''


    def __init__(self, name, speed, health, damage, loot, path):
        '''
        Constructor
        '''
        self.name = name
        self.speed = speed
        self.damage = damage
        self.loot = loot
        self.set_health(health)
        self.set_location((0,0))
        self.path = path
        self.sector = 0
    
    def set_health(self, health):
        self.health = health
    
    def get_health(self):
        return self.health
    
    def get_damage(self):
        return self.damage
    
    def get_loot(self):
        return self.loot
    
    def get_name(self):
        return self.name
    
    def get_speed(self):
        return self.speed
    
    def set_location(self, location):
        self.location = location
        
    def get_location(self):
        return self.location
    
    def set_sector(self, sector):
        self.sector = sector
        
    def get_sector(self):
        return self.sector
    
    def get_path(self):
        return self.path
        
    
    
    
        