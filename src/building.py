'''
Created on 22.04.2017

@author: Flex
'''

# be careful, use same field in main.py! not global!
CONST_TOWER_NAME = ['Pulse','Negotiator','Peacemaker','Equalizer','Undertaker','Lawbringer']
CONST_TOWER_DAMAGE = [8,12,15,20,12,20]
CONST_TOWER_RANGE = [90,120,200,300,300,250]
CONST_TOWER_PRICE = [26,40,110,300,650,1000]
CONST_TOWER_COOLDOWN = [400,700,300,400,100,50]
white = (255,255,255)
black = (0,0,0)

class building(object):
    '''
    classdocs
    '''

    def __init__(self, row, column, towertype, health):
        '''
        Constructor
        '''
        self.row = row
        self.column = column
        self.health = health
        self.set_towertype(towertype)  
        self.cooldown = 0
     
        
    def get_towertype(self):
        return self.towertype
    
    def get_health(self):
        return self.health
    
    def set_towertype(self, towertype):
        self.towertype = towertype
        if towertype == -1:
            self.damage = 0
            self.range = 0
        else:
            self.damage = CONST_TOWER_DAMAGE[towertype]
            self.range = CONST_TOWER_RANGE[towertype]
        
    
    def set_health(self, new_health_value):
        self.health = new_health_value
    
    def get_range(self):
        return self.range
    
    def get_damage(self):
        return self.damage
    
    def reset_cooldown(self,actual_time):
        self.cooldown = actual_time + CONST_TOWER_COOLDOWN[self.towertype]
    
    def get_cooldown(self):
        return self.cooldown



       
