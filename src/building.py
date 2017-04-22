'''
Created on 22.04.2017

@author: Flex
'''

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
        if towertype == 't1':
            self.damage = damage_t1
            self.range = range_t1 
        elif towertype == 't2':
            self.damage = damage_t2
            self.range = range_t2
        elif towertype == 't3':
            self.damage = damage_t3
            self.range = range_t3        
        elif towertype == 't4':
            self.damage = damage_t4
            self.range = range_t4
        elif towertype == 't5':
            self.damage = damage_t5
            self.range = range_t5
    
    def set_health(self, new_health_value):
        self.health = new_health_value
    
       