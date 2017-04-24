'''
Created on 23.04.2017

@author: Flex
'''

class house(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.health = 1000
        self.alert = 0
        
    def set_alert(self):
        self.alert = self.alert +1
    
    def reset_alert(self):
        self.alert = self.alert -1
        if self.alert < 0:
            print("WARNING: PROGRAM SHOULDNT BE HERE")
    
    def get_alert(self):
        return self.alert
    
    def set_health(self, health):
        if health < 0:
            health = 0
        self.health = health
    
    def get_health(self):
        return self.health
    

    
        
        