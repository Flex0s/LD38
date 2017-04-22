'''
Created on 22.04.2017

@author: Flex
'''
#be careful, this is not global!
CONST_TOWER_DAMAGE = [5,10,15,20,25]
CONST_TOWER_RANGE = [5,10,15,20,25]

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
    
       