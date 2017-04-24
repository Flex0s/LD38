'''
Created on 22.04.2017

@author: Flex

beware: i mixed up the names for row and columns, 
'''
from optparse import check_builtin
from building import building
from enemy import enemy
from math import sqrt
import numpy as np
from pip import locations
from time import *
from house import house

if __name__ == '__main__':
    pass

import pygame

pygame.init()
pygame.font.init()

CONST_DISPLAY_WIDTH = 1024
CONST_DISPLAY_HEIGHT = 768

# be careful, change also in building.py! not global!
CONST_TOWER_NAME = ['Pulse','Negotiator','Peacemaker','Equalizer','Undertaker','Lawbringer']
CONST_TOWER_DAMAGE = [8,12,15,20,12,25]
CONST_TOWER_RANGE = [90,120,200,300,350,100]
CONST_TOWER_PRICE = [26,40,110,300,650,1000]
CONST_TOWER_COOLDOWN = [300,700,300,400,100,50]

# be careful, change also in enemy.py! not global!
ENEMY_INFO = ['low', 'medium', 'hard', 'flying', 'boss']
CONST_ENEMY_DAMAGE = [0.5, 0.6, 1, 0.6, 5]
CONST_ENEMY_RANGE = [40, 40, 40, 40, 40]
CONST_ENEMY_SPEED = [0.4, 0.8, 0.5, 0.6, 0.25]
CONST_ENEMY_LOOT = [2, 5, 4, 7, 35]
CONST_ENEMY_HEALTH = [30, 120, 50, 85, 550]
CONST_ENEMY_COOLDOWN = [350,700,50,400,350]

CONST_HOME = (520,367)
homebase = house()

techtree_font_headline = pygame.font.SysFont("Arial", 20)  
techtree_font = pygame.font.SysFont("Arial", 15)  
wavecounter_font = pygame.font.SysFont("Arial", 20)  
roundcounter_font = pygame.font.SysFont("Arial", 25) 
homebasehealth_font = pygame.font.SysFont("Arial", 30)  
gameover_font = pygame.font.SysFont("Impact", 150)
gamewon_font = pygame.font.SysFont("Impact", 130)

imgpath = '..\sprites\\'

gameDisplay = pygame.display.set_mode((CONST_DISPLAY_WIDTH,CONST_DISPLAY_HEIGHT))
pygame.display.set_caption('LD38 - A small world - by Flex')
clock = pygame.time.Clock()

info_font = pygame.font.SysFont("Arial", 10)

techtree_x_offset = [30, 120, 210, 300, 390, 480]
tower_img =[ pygame.image.load(imgpath + 'Tower1.png') , pygame.image.load(imgpath + 'Tower2.png') , pygame.image.load(imgpath + 'Tower3.png') , pygame.image.load(imgpath + 'Tower4.png') , pygame.image.load(imgpath + 'Tower5.png'), pygame.image.load(imgpath + 'Tower6.png')]
enemy_img = [ pygame.image.load(imgpath + 'enemy_1.png') , pygame.image.load(imgpath + 'enemy_2.png') , pygame.image.load(imgpath + 'enemy_3.png'), pygame.image.load(imgpath + 'enemy_4.png'), pygame.image.load(imgpath + 'enemy_5.png')]
alert_img = pygame.image.load(imgpath + 'alert.png')

healthbar_img_names = ['Healthbar_schwarz.png','Healthbar_gruen.png','Healthbar_gelb.png','Healthbar_rot.png']

#starting coins
balance = 100



white = (255,255,255)
black = (0,0,0)
olive = (0,51,51)

globeimg = pygame.image.load(imgpath + 'world.png').convert_alpha()
gridimg = pygame.image.load(imgpath + 'world_grid.png').convert_alpha() 
rangeimg = pygame.image.load(imgpath + 'range.png').convert_alpha() 
dashboardimg = pygame.image.load(imgpath + 'dashboard.png') 
dashboardimg2 = pygame.image.load(imgpath + 'dashboard_red.png') 

offs_x= CONST_DISPLAY_WIDTH*0.5-(globeimg.get_width()/2)
offs_y= CONST_DISPLAY_HEIGHT*0.5-(globeimg.get_height()/2)


    
    
def game_over(game_level):
    gameDisplay.fill(black) 
    label = gameover_font.render("GAME OVER"  , True, white)
    gameDisplay.blit(label, (190, 130))  
    
    label = roundcounter_font.render("Thank you for playing!"  , True, white)
    gameDisplay.blit(label, (410, 300))    
    label = roundcounter_font.render("You died in Round %d" %game_level  , True, white)
    gameDisplay.blit(label, (420, 500))  
       
    label = roundcounter_font.render("Please press Return to Exit"  , True, white)
    gameDisplay.blit(label, (380, 700))     
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True  
            if event.type == pygame.KEYDOWN:
                #check for key-input
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    quit()
        pygame.display.update() 
    pygame.quit()
    quit()
  
def game_won():
    gameDisplay.fill(black) 
    label = gamewon_font.render("CONGRATULATIONS!"  , True, white)
    gameDisplay.blit(label, (10, 130))  
    
    label = roundcounter_font.render("You saved the World!"  , True, white)
    gameDisplay.blit(label, (410, 300))    


       
    label = roundcounter_font.render("Please press Return to Exit"  , True, white)
    gameDisplay.blit(label, (380, 700))     
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True  
            if event.type == pygame.KEYDOWN:
                #check for key-input
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    quit()
        pygame.display.update() 
    pygame.quit()
    quit()    

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def globe(x,y):
    gameDisplay.blit(globeimg, (x,y))

def dashboard():
    gameDisplay.blit(dashboardimg, (0,0))

def grid(x,y):      
    gameDisplay.blit(gridimg,(x,y))
    
def coins(x,y):
    label = homebasehealth_font.render("Coins: %d" % balance, True, black)
    gameDisplay.blit(label, (x, y))   

def homehealth(x,y):
    label = homebasehealth_font.render("Home Health: %d / 1000" % homebase.get_health() , True, black)
    gameDisplay.blit(label, (x, y))    
    if homebase.get_alert() > 0:    
        gameDisplay.blit(alert_img,(455,330))

def snapgrid(chosen_tower,x,y):
    
    (row, column) = findpos()
    
    valid = True    
        
    if (row == 0 or row == 10) and (column == 0 or column == 1 or column ==  2 or column ==  3 or column == 7 or column == 8 or column ==  9 or column ==  10):
        valid = False
    
    if (row == 1 or row == 9 ) and (column == 0 or column == 1 or column ==  9 or column ==  10):
        valid = False
        
    if (row == 2 or row == 3 ) and (column == 0 or  column == 1 or column ==  10):
        valid = False
        
    if (row == 4 ) and (column == 1 or column ==  4 or column ==  5 or column ==  6):
        valid = False    
        
    if (row == 5 ) and (column == 1 or column ==  4 or column ==  5 or column ==  6 or column == 7 or column == 8 or column == 9):
        valid = False 

    if (row == 6 ) and (column == 2 or column ==  4 or column ==  5 or column ==  6 or column ==  9):
        valid = False
                         
    if (row == 7 ) and (column == 0 or column == 3 or column ==  4 or column ==  5 or  column == 9 or column ==  10):
        valid = False
    
    if (row == 8 ) and (column == 0 or column == 9 or column ==  10):
        valid = False        

    if valid == True:
        if chosen_tower != -1:
            gameDisplay.blit(tower_img[chosen_tower],(x+row*40+10,y+column*40+10))
            show_range((row,column),chosen_tower)
        
def techtree(techtree_font):
    # show the techtree


    if chosen_tower != -1:
        gameDisplay.blit(dashboardimg2, (25+90*chosen_tower, CONST_DISPLAY_HEIGHT - 92) )          

    for i in range(0, len(CONST_TOWER_DAMAGE)):
        label = techtree_font.render(CONST_TOWER_NAME[i] , True, white)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 90))    
        gameDisplay.blit(tower_img[i],(techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 70))     
        label = info_font.render("Cost: %d " % CONST_TOWER_PRICE[i], True, white)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 50))           
        label = info_font.render("Range: %d" % CONST_TOWER_RANGE[i], True, white)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 40))              
        label = info_font.render("Damage: %d" % CONST_TOWER_DAMAGE[i], True, white)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 30)) 
        label = info_font.render("Cooldown: %.1fs" % (CONST_TOWER_COOLDOWN[i]/1000), True, white)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT -20))         
      
def findpos():
    p = pygame.mouse.get_pos()
    row = int((p[0]-offs_x)/40)
    if row <0:
        row =0
    if row > 10:
        row = 10
    column = int((p[1]-offs_y)/40)
    if column < 0:
        column = 0
    if column > 10:
        column = 10
    return(row,column)

def findtower(chosen_tower):
    p = pygame.mouse.get_pos()

   
    if  p[1] > CONST_DISPLAY_HEIGHT - 80 :
        if p[0] <= techtree_x_offset[0]+70:    
            answer =  0
        elif p[0] > techtree_x_offset[0]+70 and p[0] <= techtree_x_offset[1]+60:
            answer = 1
        elif p[0] > techtree_x_offset[1]+60 and p[0] <= techtree_x_offset[2]+60:
            answer = 2  
        elif p[0] > techtree_x_offset[2]+60 and p[0] <= techtree_x_offset[3]+60:
            answer = 3
        elif p[0] > techtree_x_offset[3]+60 and p[0] <= techtree_x_offset[4]+60:
            answer = 4               
        elif p[0] > techtree_x_offset[3]+60 and p[0] <= techtree_x_offset[5]+60:
            answer = 5         
        else:
            answer -1
    else:
        answer = chosen_tower
    if balance < CONST_TOWER_PRICE[answer]:
        answer = -1    
    return answer
    
def check_if_valid():
    valid = True
    if (row == 0 or row == 10) and (column == 0 or column == 1 or column ==  2 or column ==  3 or column == 7 or column == 8 or column ==  9 or column ==  10):
        valid = False
    
    if (row == 1 or row == 9 ) and (column == 0 or column == 1 or column ==  9 or column ==  10):
        valid = False
        
    if (row == 2 or row == 3 ) and (column == 0 or  column == 1 or column ==  10):
        valid = False
        
    if (row == 4 ) and (column == 1 or column ==  4 or column ==  5 or column ==  6):
        valid = False    
        
    if (row == 5 ) and (column == 1 or column ==  4 or column ==  5 or column ==  6 or column == 7 or column == 8 or column == 9):
        valid = False 

    if (row == 6 ) and (column == 2 or column ==  4 or column ==  5 or column ==  6 or column ==  9):
        valid = False
                         
    if (row == 7 ) and (column == 0 or column == 3 or column ==  4 or column ==  5 or  column == 9 or column ==  10):
        valid = False
    
    if (row == 8 ) and (column == 0 or column == 9 or column ==  10):
        valid = False 
    
    return valid

def cog(r,c):
    cog_x = offs_x+r*40+20
    cog_y = offs_y+c*40+20
    return (cog_x, cog_y)

def show_range(coordinates,chosen_tower):
    
    if chosen_tower != -1:
        tower_range = CONST_TOWER_RANGE[chosen_tower]
        if tower_range != 0:
            scaled_img = pygame.transform.scale( rangeimg , (tower_range*2,tower_range*2))
            coord_x = offs_x+coordinates[0]*40-tower_range+20
            coord_y = offs_y+coordinates[1]*40-tower_range+20
            gameDisplay.blit(scaled_img,  (coord_x,coord_y)  )  
 

#create paths
walking_path = []
path_offset_x = CONST_DISPLAY_WIDTH*0.5-(globeimg.get_width()/2)
path_offset_y = CONST_DISPLAY_HEIGHT*0.5-(globeimg.get_height()/2)
#path north with slightly different starting points
walking_path.append([(363,220),(453,219),(527,243),(580,297),(590,379),(543,425),(526,389)])
walking_path.append([(335,249),(453,219),(527,243),(580,297),(590,379),(543,425),(526,389)])
walking_path.append([(414,186),(453,219),(527,243),(580,297),(590,379),(543,425),(526,389)])

#path south with slightly different starting points
walking_path.append([(659,543),(572,550),(515,539),(513,460),(540,428),(547,371)])
walking_path.append([(614,577),(572,550),(515,539),(513,460),(540,428),(547,371)])
walking_path.append([(690,512),(572,550),(515,539),(513,460),(540,428),(547,371)])

#flying path west
walking_path.append([(307,455),(340,412),(392,389),(423,308),(488,406),(503,375)])
walking_path.append([(312,470),(340,412),(392,389),(423,308),(488,406),(503,375)])

#flying path east
walking_path.append([(592,182),(613,225),(626,308),(595,360),(537,352),(497,342)])
walking_path.append([(719,318),(613,225),(626,308),(595,360),(537,352),(497,342)])

#initialize Buildings with 'none'
fields = []

#initialize events
event_counter = 0
game_level = 0

for row in range(0,11):
    for column in range(0,11):
        fields.append(building(row,column,-1,0))

#initialize enemies
enemies= []
delete_enemies = []  

crashed = False

chosen_tower = -1


while not crashed:
    for event in pygame.event.get():
           
        if event.type == pygame.QUIT:
            crashed = True          
          
        if True:    
            
            if event.type == pygame.MOUSEBUTTONUP:              
                chosen_tower = findtower(chosen_tower)     
                p = pygame.mouse.get_pos()
                
                if chosen_tower != -1 and p[1] <= CONST_DISPLAY_HEIGHT - 80:
                    
                    (row,column) = findpos()
                 
                    index = row*11 + column    
                    if check_if_valid() == True:   
                        if balance - CONST_TOWER_PRICE[chosen_tower] >= 0 : 
                            if fields[index].get_towertype() == -1:                
                                fields[index].set_towertype(chosen_tower)   
                                balance = balance - CONST_TOWER_PRICE[chosen_tower]     
                                chosen_tower = -1

                    

        if event.type == pygame.KEYDOWN:
            #check for key-input
            if event.key == pygame.K_x:
                chosen_tower = -1
            if event.key == pygame.K_1:   
                if balance < CONST_TOWER_PRICE[0]:
                    chosen_tower = -1 
                else:
                    chosen_tower = 0
            if event.key == pygame.K_2:   
                if balance < CONST_TOWER_PRICE[1]:
                    chosen_tower = -1 
                else:
                    chosen_tower = 1
            if event.key == pygame.K_3:   
                if balance < CONST_TOWER_PRICE[2]:
                    chosen_tower = -1 
                else:
                    chosen_tower = 2                    
            if event.key == pygame.K_4:   
                if balance < CONST_TOWER_PRICE[3]:
                    chosen_tower = -1 
                else:
                    chosen_tower = 3                        
            if event.key == pygame.K_5:   
                if balance < CONST_TOWER_PRICE[4]:
                    chosen_tower = -1 
                else:
                    chosen_tower = 4 
        
    #clean view    
    gameDisplay.fill(white)   

    #show world
    #show coin balance and globe
    x= CONST_DISPLAY_WIDTH*0.5-(globeimg.get_width()/2)
    y= CONST_DISPLAY_HEIGHT*0.5-(globeimg.get_height()/2)
    dashboard()
    globe(x,y)
    coins(650,665)
    homehealth(650,720)
    
    
    #generate enemies
    INTRO_DURATION = 0    
    LEVEL_1_START = INTRO_DURATION + 5000   
    LEVEL_2_START = LEVEL_1_START + 35000 
    LEVEL_3_START = LEVEL_2_START + 30000
    LEVEL_4_START = LEVEL_3_START + 30000
    LEVEL_5_START = LEVEL_4_START + 50000
    LEVEL_6_START = LEVEL_5_START + 30000
    actual_time = pygame.time.get_ticks()
    if game_level == 0:    
        time_to_next_wave = (LEVEL_1_START - actual_time) /1000
        label = wavecounter_font.render("Next wave in: %d seconds" % int(time_to_next_wave) , True, black)
        gameDisplay.blit(label, (780, 130))    
   
    

        
    if actual_time > LEVEL_1_START and game_level == 0:
        game_level = 1
        
    if game_level == 1:
        label = roundcounter_font.render("ROUND 1: Evil Munchers"  , True, black)
        gameDisplay.blit(label, (390, 130))  
        time_to_next_wave = (LEVEL_2_START - actual_time) /1000
        label = wavecounter_font.render("Next wave in: %d seconds" % int(time_to_next_wave) , True, black)
        gameDisplay.blit(label, (780, 130))            
        if event_counter <1:
            enemies.append(enemy("Arsch1", 0, 0))
            enemies.append(enemy("Arsch1", 0, 1))
            enemies.append(enemy("Arsch1", 0, 2))
            event_counter = 1         
        
        if actual_time > LEVEL_1_START+500 and event_counter <2:
            enemies.append(enemy("Arsch1", 0, 0))
            enemies.append(enemy("Arsch1", 0, 2))
            event_counter = 2
            
        if actual_time > LEVEL_1_START+1000 and event_counter <3:
            enemies.append(enemy("Arsch1", 0, 0))
            enemies.append(enemy("Arsch1", 0, 2))
            event_counter = 3
    
        if actual_time > LEVEL_1_START+1500 and event_counter <4:
            enemies.append(enemy("Arsch1", 0, 0))
            enemies.append(enemy("Arsch1", 0, 2))  
            event_counter = 4            
                        
        if actual_time > LEVEL_1_START+2000 and event_counter <5:
            enemies.append(enemy("Arsch1", 0, 0))
            enemies.append(enemy("Arsch1", 0, 1))
            enemies.append(enemy("Arsch1", 0, 2)) 
            event_counter = 5      
    
        if actual_time > LEVEL_1_START+2500 and event_counter <6:
            enemies.append(enemy("Arsch1", 0, 0))
            enemies.append(enemy("Arsch1", 0, 1))
            enemies.append(enemy("Arsch1", 0, 2)) 
            event_counter = 6       
      
        if actual_time > LEVEL_1_START+9500 and event_counter <7:
            enemies.append(enemy("Arsch2", 0, 3))

            enemies.append(enemy("Arsch2", 0, 5))
            event_counter = 7         

        if actual_time > LEVEL_1_START+10000 and event_counter <8:
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 4))
            event_counter = 8
            
        if actual_time > LEVEL_1_START+10500 and event_counter <9:
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 4))
            event_counter = 9
    
        if actual_time > LEVEL_1_START+11000 and event_counter <10:
            enemies.append(enemy("Arsch2", 0, 5))
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 4))
            event_counter = 10            
                        
        if actual_time > LEVEL_1_START+11500 and event_counter <11:
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 4)) 
            event_counter = 11      
    
        if actual_time > LEVEL_1_START+12000 and event_counter <12:
            enemies.append(enemy("Arsch2", 0, 5))
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 4))
            event_counter = 12         
        
    if actual_time > LEVEL_2_START and game_level == 1:
        game_level = 2
        event_counter = 0    
    
    if game_level == 2:
        label = roundcounter_font.render("ROUND 2: Feisty Phallus"  , True, black)
        gameDisplay.blit(label, (390, 130))  
        time_to_next_wave = (LEVEL_3_START - actual_time) /1000
        label = wavecounter_font.render("Next wave in: %d seconds" % int(time_to_next_wave) , True, black)
        gameDisplay.blit(label, (780, 130)) 
        if event_counter <1:
            enemies.append(enemy("Arsch1", 2, 0))
            enemies.append(enemy("Arsch2", 2, 1))
            enemies.append(enemy("Arsch2", 2, 1))
            event_counter = 1         

        if actual_time > LEVEL_2_START+500 and event_counter <2:
            enemies.append(enemy("Arsch1", 2, 0)) 
            enemies.append(enemy("Arsch1", 2, 2))  
            enemies.append(enemy("Arsch2", 2, 1))
            event_counter = 2
            
        if actual_time > LEVEL_2_START+1000 and event_counter <3:
            enemies.append(enemy("Arsch1", 2, 2))   
            enemies.append(enemy("Arsch2", 2, 1))
            enemies.append(enemy("Arsch2", 2, 1))
            event_counter = 3
    
        if actual_time > LEVEL_2_START+1500 and event_counter <4:
            enemies.append(enemy("Arsch4", 2, 2))   
            enemies.append(enemy("Arsch4", 2, 2))
            enemies.append(enemy("Arsch5", 2, 1))  
            event_counter = 4            
                        
        if actual_time > LEVEL_2_START+2000 and event_counter <5:
            enemies.append(enemy("Arsch4", 2, 0))   
            enemies.append(enemy("Arsch5", 2, 1)) 
            enemies.append(enemy("Arsch5", 2, 2)) 
            event_counter = 5      
    
        if actual_time > LEVEL_2_START+2500 and event_counter <6:
            enemies.append(enemy("Arsch4", 2, 0))   
            enemies.append(enemy("Arsch5", 2, 1))
            enemies.append(enemy("Arsch5", 2, 1))
            enemies.append(enemy("Arsch5", 2, 0))       
            event_counter = 6   
        
        if actual_time > LEVEL_2_START+8000 and event_counter <7:
            enemies.append(enemy("Arsch4", 2, 3))   
            enemies.append(enemy("Arsch5", 2, 3))  
            enemies.append(enemy("Arsch5", 2, 5)) 
            enemies.append(enemy("Arsch5", 2, 5))         
            event_counter = 7
                               
        if actual_time > LEVEL_2_START+3500 and event_counter <8:
            enemies.append(enemy("Arsch5", 2, 4))   
            enemies.append(enemy("Arsch5", 2, 4))
            enemies.append(enemy("Arsch5", 2, 3))
            enemies.append(enemy("Arsch5", 2, 5))          
            event_counter = 8
               
        if actual_time > LEVEL_2_START+3500 and event_counter <9:
            enemies.append(enemy("Arsch5", 2, 4))   
            enemies.append(enemy("Arsch5", 2, 4))
            enemies.append(enemy("Arsch5", 2, 3))
            enemies.append(enemy("Arsch5", 2, 5))   
            enemies.append(enemy("Arsch5", 2, 4))   
            enemies.append(enemy("Arsch5", 2, 4))
            enemies.append(enemy("Arsch5", 2, 3))
            enemies.append(enemy("Arsch5", 2, 5))       
            event_counter = 9
            
    if actual_time > LEVEL_3_START and game_level ==2:
        game_level = 3
        event_counter = 0    

    if game_level == 3:
        label = roundcounter_font.render("ROUND 3: Flying Fuckheads"  , True, black)
        gameDisplay.blit(label, (390, 130))  
        time_to_next_wave = (LEVEL_4_START - actual_time) /1000
        label = wavecounter_font.render("Next wave in: %d seconds" % int(time_to_next_wave) , True, black)
        gameDisplay.blit(label, (780, 130)) 
        
        if actual_time > LEVEL_3_START and event_counter <1:
            enemies.append(enemy("Arsch1", 3, 6))
            enemies.append(enemy("Arsch2", 3, 7))
            enemies.append(enemy("Arsch2", 3, 7))
            event_counter = 1         

        if actual_time > LEVEL_3_START+500 and event_counter <2:
            enemies.append(enemy("Arsch1", 3, 6)) 
  
            enemies.append(enemy("Arsch2", 3, 6))
            event_counter = 2
            
        if actual_time > LEVEL_3_START+1000 and event_counter <3:
            enemies.append(enemy("Arsch1", 3, 7))   

            enemies.append(enemy("Arsch2", 3, 7))
            event_counter = 3
    
        if actual_time > LEVEL_3_START+1500 and event_counter <4:
            enemies.append(enemy("Arsch4", 3, 6))   
            enemies.append(enemy("Arsch4", 3, 7))
 

            event_counter = 4            
                        
        if actual_time > LEVEL_3_START+2000 and event_counter <5:
            enemies.append(enemy("Arsch4", 3, 9))   
            enemies.append(enemy("Arsch5", 3, 9)) 

            event_counter = 5      
    
        if actual_time > LEVEL_3_START+2500 and event_counter <6:
            enemies.append(enemy("Arsch4", 3, 7))   
            enemies.append(enemy("Arsch5", 3, 8))
            enemies.append(enemy("Arsch5", 3, 8))
     
            event_counter = 6   
        
        if actual_time > LEVEL_3_START+3000 and event_counter <7:
            enemies.append(enemy("Arsch4", 3, 7))   
            enemies.append(enemy("Arsch5", 3, 7))  
            enemies.append(enemy("Arsch5", 3, 6)) 
       
            event_counter = 7
         
    
    if actual_time > LEVEL_4_START and game_level ==3:
        game_level = 4
        event_counter = 0    

    if game_level == 4:
        label = roundcounter_font.render("ROUND 4: BOSS ROBOTS"  , True, black)
        gameDisplay.blit(label, (390, 130))  
        time_to_next_wave = (LEVEL_5_START - actual_time) /1000
        label = wavecounter_font.render("Next wave in: %d seconds" % int(time_to_next_wave) , True, black)
        gameDisplay.blit(label, (780, 130)) 
        
        if actual_time > LEVEL_4_START and event_counter <1:
            enemies.append(enemy("Arsch1", 4, 0))
            enemies.append(enemy("Arsch2", 4, 1))
            enemies.append(enemy("Arsch2", 4, 2))
            event_counter = 1         

        if actual_time > LEVEL_4_START+2000 and event_counter <2:
            enemies.append(enemy("Arsch1", 4, 3)) 
            enemies.append(enemy("Arsch1", 4, 4))  
            enemies.append(enemy("Arsch2", 4, 5))
            event_counter = 2
            
        if actual_time > LEVEL_4_START+10000 and event_counter <3:
            enemies.append(enemy("Arsch1", 4, 0))   
            enemies.append(enemy("Arsch2", 4, 1))
            enemies.append(enemy("Arsch2", 4, 2))
            event_counter = 3
    
        if actual_time > LEVEL_4_START+10500 and event_counter <4:
            enemies.append(enemy("Arsch4", 4, 3))   
            enemies.append(enemy("Arsch4", 4, 4))
            enemies.append(enemy("Arsch5", 4, 5))  
            event_counter = 4            

    if actual_time > LEVEL_5_START and game_level ==4:
        game_level = 5
        event_counter = 0    

    if game_level == 5:
        label = roundcounter_font.render("ROUND 5: Greasy Plumbers" , True, black)
        gameDisplay.blit(label, (390, 130))  
        time_to_next_wave = (LEVEL_6_START - actual_time) /1000
        label = wavecounter_font.render("Next wave in: %d seconds" % int(time_to_next_wave) , True, black)
        gameDisplay.blit(label, (780, 130)) 
        
        if actual_time > LEVEL_5_START and event_counter <1:
            enemies.append(enemy("Arsch1", 1, 0))
            enemies.append(enemy("Arsch2", 1, 1))
            enemies.append(enemy("Arsch2", 1, 2))
            event_counter = 1         

        if actual_time > LEVEL_5_START+500 and event_counter <2:
            enemies.append(enemy("Arsch1", 1, 3)) 
            enemies.append(enemy("Arsch1", 1, 4))  
            enemies.append(enemy("Arsch2", 1, 5))
            event_counter = 2
            
        if actual_time > LEVEL_5_START+1000 and event_counter <3:
            enemies.append(enemy("Arsch1", 1, 0))   
            enemies.append(enemy("Arsch2", 1, 1))
            enemies.append(enemy("Arsch2", 1, 2))
            event_counter = 3
    
        if actual_time > LEVEL_5_START+1500 and event_counter <4:
            enemies.append(enemy("Arsch4", 1, 3))   
            enemies.append(enemy("Arsch4", 1, 4))
            enemies.append(enemy("Arsch5", 1, 5))  
            event_counter = 4                
        if actual_time > LEVEL_5_START+2000 and event_counter <5:
            enemies.append(enemy("Arsch1", 1, 0))
            enemies.append(enemy("Arsch2", 1, 1))
            enemies.append(enemy("Arsch2", 1, 2))
            event_counter = 5         

        if actual_time > LEVEL_5_START+2500 and event_counter <6:
            enemies.append(enemy("Arsch1", 1, 3)) 
            enemies.append(enemy("Arsch1", 1, 4))  
            enemies.append(enemy("Arsch2", 1, 5))
            event_counter = 6
            
        if actual_time > LEVEL_5_START+3000 and event_counter <7:
            enemies.append(enemy("Arsch1", 1, 0))   
            enemies.append(enemy("Arsch2", 1, 1))
            enemies.append(enemy("Arsch2", 1, 2))
            event_counter = 7
    
        if actual_time > LEVEL_5_START+3500 and event_counter <8:
            enemies.append(enemy("Arsch4", 1, 3))   
            enemies.append(enemy("Arsch4", 1, 4))
            enemies.append(enemy("Arsch5", 1, 5))  
            event_counter = 8  
            
    if actual_time > LEVEL_6_START and game_level ==5:
        game_level = 6
        event_counter = 0  
          
    if game_level == 6:
        label = roundcounter_font.render("FINAL ROUND: ALL TOGETHER!"  , True, black)
        gameDisplay.blit(label, (370, 130))  

        if actual_time > LEVEL_6_START and event_counter <1:
            enemies.append(enemy("Arsch1", 0, 0))
            enemies.append(enemy("Arsch1", 1, 2))
            enemies.append(enemy("Arsch2", 0, 1))
            enemies.append(enemy("Arsch2", 3, 9))
            enemies.append(enemy("Arsch2", 3, 9))
            enemies.append(enemy("Arsch2", 3, 9))
            enemies.append(enemy("Arsch2", 4, 4))
            event_counter = 1         

        if actual_time > LEVEL_6_START+500 and event_counter <2:
            enemies.append(enemy("Arsch1", 1, 3)) 
            enemies.append(enemy("Arsch1", 0, 4))  
            enemies.append(enemy("Arsch2", 4, 1))
            enemies.append(enemy("Arsch1", 2, 3)) 
            enemies.append(enemy("Arsch1", 4, 3))  
            enemies.append(enemy("Arsch2", 0, 5))
            enemies.append(enemy("Arsch2", 1, 5))
            enemies.append(enemy("Arsch2", 0, 4))
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 0))
            
            event_counter = 2
            
        if actual_time > LEVEL_6_START+1000 and event_counter <3:
            enemies.append(enemy("Arsch1", 3, 6))   
            enemies.append(enemy("Arsch2", 3, 6))
            enemies.append(enemy("Arsch2", 3, 7))
            enemies.append(enemy("Arsch2", 3, 7))
            enemies.append(enemy("Arsch2", 0, 4))
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 0))
            enemies.append(enemy("Arsch1", 3, 8))   
            enemies.append(enemy("Arsch2", 3, 8))
            enemies.append(enemy("Arsch2", 3, 9))
            enemies.append(enemy("Arsch2", 3, 9))
            event_counter = 3
    
        if actual_time > LEVEL_6_START+1500 and event_counter <4:
            enemies.append(enemy("Arsch4", 0, 3))   
            enemies.append(enemy("Arsch4", 4, 4))
            enemies.append(enemy("Arsch5", 0, 5))  
            enemies.append(enemy("Arsch2", 0, 4))
            enemies.append(enemy("Arsch2", 0, 3))
            enemies.append(enemy("Arsch2", 0, 0))
            
            
            event_counter = 4                
        if actual_time > LEVEL_6_START+2000 and event_counter <5:
            enemies.append(enemy("Arsch1", 3, 6))   
            enemies.append(enemy("Arsch2", 3, 6))
            enemies.append(enemy("Arsch2", 3, 7))
            enemies.append(enemy("Arsch2", 3, 7))
            enemies.append(enemy("Arsch1", 2, 0))
            enemies.append(enemy("Arsch2", 2, 1))
            enemies.append(enemy("Arsch2", 2, 2))
            event_counter = 5         

        if actual_time > LEVEL_6_START+2500 and event_counter <6:
            enemies.append(enemy("Arsch1", 3, 6))   
            enemies.append(enemy("Arsch2", 3, 6))
            enemies.append(enemy("Arsch2", 3, 7))
            enemies.append(enemy("Arsch2", 3, 7))
            enemies.append(enemy("Arsch1", 2, 3)) 
            enemies.append(enemy("Arsch1", 1, 4))  
            enemies.append(enemy("Arsch2", 0, 5))
            event_counter = 6
            
        if actual_time > LEVEL_6_START+3000 and event_counter <7:
            enemies.append(enemy("Arsch1", 3, 6))   
            enemies.append(enemy("Arsch2", 3, 6))
            enemies.append(enemy("Arsch2", 3, 7))
            enemies.append(enemy("Arsch2", 3, 7))
            enemies.append(enemy("Arsch1", 0, 0))   
            enemies.append(enemy("Arsch2", 2, 1))
            enemies.append(enemy("Arsch2", 1, 2))
            enemies.append(enemy("Arsch1", 3, 8))   
            enemies.append(enemy("Arsch2", 3, 8))
            enemies.append(enemy("Arsch2", 3, 9))
            enemies.append(enemy("Arsch2", 3, 9))
            event_counter = 7
    
        if actual_time > LEVEL_6_START+3500 and event_counter <8:
            enemies.append(enemy("Arsch4", 1, 3))   
            enemies.append(enemy("Arsch4", 2, 4))
            enemies.append(enemy("Arsch5", 2, 5))  
            enemies.append(enemy("Arsch1", 3, 8))   
            enemies.append(enemy("Arsch2", 3, 8))
            enemies.append(enemy("Arsch2", 3, 9))
            enemies.append(enemy("Arsch2", 3, 9))
            event_counter = 8      
    
    
    
    
    if actual_time > LEVEL_6_START+30000 and len(enemies) == 0:
        game_won()

    
    
    
    # enemy movement + damage from enemy + enemy visualization
    for i in range(0,len(enemies)):
        
        if enemies[i].get_health() > 0:
            activepath = walking_path[enemies[i].get_path()]
            actual_location = enemies[i].get_location()
            sector = enemies[i].get_sector()
            if sector == 0:
                #new enemy
                enemies[i].set_location(activepath[0])
                enemies[i].set_target(activepath[1])
                enemies[i].set_sector(1)
            
            else:
                target_location = enemies[i].get_target()
                speed = CONST_ENEMY_SPEED[enemies[i].get_type()]
                distance_to_next_waypoint = sqrt( pow( (target_location[0] - actual_location[0]), 2) + pow( (target_location[1] - actual_location[1]), 2))         
                if distance_to_next_waypoint < speed:


                    if sector < len(activepath):
                        #switch to next sector, if not on last waypoint
                        enemies[i].set_target(activepath[sector])
                        enemies[i].set_sector(sector+1)  
                        new_target = enemies[i].get_target()
                    else:
                        enemies[i].set_target(activepath[sector-1])

                else:
                    speed_factor = speed/distance_to_next_waypoint
            
                    vector = np.subtract(target_location, actual_location)
            
                    new_position = np.add(actual_location, vector * speed_factor)
            
            
                    enemies[i].set_location(new_position)
            
                    #show enemies
                    vector[0] = target_location[0] - new_position[0] 
                    vector[1] = target_location[1] - new_position[1]

                    angle = np.degrees(np.arctan(target_location- new_position))+180
                    
                    

                    image = enemy_img[enemies[i].get_type()]
                    enemy_rotated = rot_center(image,angle[1])

                    gameDisplay.blit(enemy_rotated,enemies[i].get_location()) 
                    health = enemies[i].get_health()
                    health_rel = 100* health / CONST_ENEMY_HEALTH[enemies[i].get_type()]


                    if health_rel > 50:
                        resolution_x = 21
                        file = (imgpath+healthbar_img_names[0])
                        image = pygame.image.load(file)                          
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  )    
                        resolution_x = 21*health/CONST_ENEMY_HEALTH[enemies[i].get_type()]
                        file = (imgpath+healthbar_img_names[1])
                        image = pygame.image.load(file)                         
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  )
                    elif health_rel > 25:
                        resolution_x = 21
                        file = (imgpath+healthbar_img_names[0])
                        image = pygame.image.load(file)                          
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  ) 
                        resolution_x = 21*health/CONST_ENEMY_HEALTH[enemies[i].get_type()]
                        file = (imgpath+healthbar_img_names[2])
                        image = pygame.image.load(file)                         
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  )
                    elif health_rel > 0:
                        resolution_x = 21
                        file = (imgpath+healthbar_img_names[0])
                        image = pygame.image.load(file)                          
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  ) 
                        resolution_x = 21*health/CONST_ENEMY_HEALTH[enemies[i].get_type()]
                        file = (imgpath+healthbar_img_names[3])
                        image = pygame.image.load(file)                         
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  )

        #calculate damage from enemies
        enemy_location = enemies[i].get_location()
        enemy_range = CONST_ENEMY_RANGE[enemies[i].get_type()]
        
        distance_to_home = sqrt(pow( (CONST_HOME[0] - enemy_location[0]), 2) + pow( (CONST_HOME[1] - enemy_location[1]), 2))  
        
        if enemy_range > distance_to_home:
            if enemies[i].get_cooldown() < actual_time:
                home_health = homebase.get_health()
                homebase.set_health(home_health - CONST_ENEMY_DAMAGE[enemies[i].get_type()])
                if enemies[i].get_inrange() == False:
                    homebase.set_alert()
                    enemies[i].set_inrange(True)
                
        

        
        
    
    #show snapgrid
    if chosen_tower != -1:
        grid(x,y)
        snapgrid(chosen_tower,x,y)
  
    else:
        coords =findpos()
        show_range(findpos(),fields[coords[0]*11+coords[1]].get_towertype())
    techtree(techtree_font) 
        
    # show towers + deal damage to enemies
    for row in range(0,11):
        for column in range(0,11):
            towertype = fields[row*11+column].get_towertype()
            if towertype != -1:
                gameDisplay.blit(tower_img[towertype],(x+row*40+10,y+column*40+10))
                

                if True:
                    #deal damage to monsters
                    position_tower = cog(row, column)
                    for i in range(0,len(enemies)):                      
                        position_enemy = enemies[i].get_location()
                        distance_to_enemy = sqrt( pow( (position_enemy[0] - position_tower[0]), 2) + pow( (position_enemy[1] - position_tower[1]), 2))   
                        
                        if distance_to_enemy < fields[row*11+column].get_range():
                            enemy_health = enemies[i].get_health()
                            if fields[row*11+column].get_cooldown() < actual_time:
                                new_health = enemy_health - fields[row*11+column].get_damage() 
                                fields[row*11+column].reset_cooldown(actual_time)                                         
                                if new_health < 0:
                                    enemies[i].set_health(0)
                                    balance = balance + enemies[i].get_loot()
                                    delete_enemies.append(i)
                                else:
                                    enemies[i].set_health(new_health)
                                   
                    for i in range(0,len(delete_enemies)):
                        was_in_range = enemies[delete_enemies[i]].get_inrange()    
                        del enemies[delete_enemies[i]]   
                        if was_in_range == True:
                            homebase.reset_alert()
                    delete_enemies = []
                    
                    
                ''' healthbars for towers    
                if health == 100:
                    gameDisplay.blit(pygame.image.load(imgpath + healthbar_img_names[1]), (x+row*40+5,y+column*40+40)) 
                    
                elif health > 50:
                    gameDisplay.blit(pygame.image.load(imgpath + healthbar_img_names[0]), (x+row*40+5,y+column*40+40)) 
                    resolution_x = 30*health/100
                    file = (imgpath+healthbar_img_names[1])
                    image = pygame.image.load(file)                         
                    gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,5) ), (x+row*40+5,y + column*40+40)  )
                elif health > 25:
                    gameDisplay.blit(pygame.image.load(imgpath + healthbar_img_names[0]), (x+row*40+5,y+column*40+40)) 
                    resolution_x = 30*health/100
                    file = (imgpath+healthbar_img_names[2])
                    image = pygame.image.load(file)                         
                    gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,5) ), (x+row*40+5,y + column*40+40)  )
                elif health > 0:
                    gameDisplay.blit(pygame.image.load(imgpath + healthbar_img_names[0]), (x+row*40+5,y+column*40+40)) 
                    resolution_x = 30*health/100
                    file = (imgpath+healthbar_img_names[3])
                    image = pygame.image.load(file)                         
                    gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,5) ), (x+row*40+5,y + column*40+40)  )
                else:
                # kaboom
                    fields[row*11+column].set_towertype(-1)
                '''
                        

                       
    if homebase.get_health() <= 0:
        game_over(game_level)              
    pygame.display.update()     
    clock.tick(60)
    


pygame.quit()
quit()



  
