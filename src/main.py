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


if __name__ == '__main__':
    pass


import pygame

pygame.init()
pygame.font.init()


CONST_DISPLAY_WIDTH = 1024
CONST_DISPLAY_HEIGHT = 768

# be careful, change also in building.py! not global!
CONST_TOWER_DAMAGE = [1,2,4,6,12]
CONST_TOWER_RANGE = [80,120,200,300,300]
CONST_TOWER_PRICE = [20,35,80,300,650]
CONST_TOWER_COOLDOWN = [300,200,50,400,100]

# be careful, change also in enemy.py! not global!
CONST_ENEMY_DAMAGE = [0.5, 1, 2.5, 4, 5]
CONST_ENEMY_RANGE = [10, 20, 30, 40, 50]
CONST_ENEMY_SPEED = [1, 1.5, 1.5, 2, 0.5]
CONST_ENEMY_LOOT = [1, 2, 3, 4, 5]
CONST_ENEMY_HEALTH = [100, 110, 120, 130, 140]


techtree_font = pygame.font.SysFont("Arial", 15)  
wavecounter_font = pygame.font.SysFont("Arial", 50)  





gamepath = 'E:\_Work\LD38\\'
imgpath = gamepath + 'sprites\\'

gameDisplay = pygame.display.set_mode((CONST_DISPLAY_WIDTH,CONST_DISPLAY_HEIGHT))
pygame.display.set_caption('LD38 - A small world - by Flex')
clock = pygame.time.Clock()

   

info_font = pygame.font.SysFont("Arial", 10)




techtree_x_offset = [50, 140, 230, 310, 390]
tower_img =[ pygame.image.load(imgpath + 'Tower1.png') , pygame.image.load(imgpath + 'Tower2.png') , pygame.image.load(imgpath + 'Tower3.png') , pygame.image.load(imgpath + 'Tower4.png') , pygame.image.load(imgpath + 'Tower5.png')]
enemy_img = [ pygame.image.load(imgpath + 'enemy_1.png') , pygame.image.load(imgpath + 'enemy_2.png') , pygame.image.load(imgpath + 'enemy_3.png'), pygame.image.load(imgpath + 'enemy_4.png'), pygame.image.load(imgpath + 'enemy_5.png')]

healthbar_img_names = ['Healthbar_schwarz.png','Healthbar_gruen.png','Healthbar_gelb.png','Healthbar_rot.png']

#starting coins
balance = 1000


white = (255,255,255)
black = (0,0,0)



globeimg = pygame.image.load(imgpath + 'world.png').convert_alpha()
gridimg = pygame.image.load(imgpath + 'world_grid.png').convert_alpha() 

offs_x= CONST_DISPLAY_WIDTH*0.5-(globeimg.get_width()/2)
offs_y= CONST_DISPLAY_HEIGHT*0.5-(globeimg.get_height()/2)

def globe(x,y):
    gameDisplay.blit(globeimg, (x,y))

def grid(x,y):      
    gameDisplay.blit(gridimg,(x,y))

def coins(x,y):
    label = techtree_font.render("Coins: %d" % balance, True, black)
    gameDisplay.blit(label, (x, y))   
    
    
def snapgrid(img,x,y):
    
    (row, column) = findpos()
    
    valid = True    
        
    if (row == 0 or row == 10) and (column == 0 or column == 1 or column ==  2 or column ==  3 or column == 7 or column == 8 or column ==  9 or column ==  10):
        valid = False
    
    if (row == 1 or row == 9 ) and (column == 0 or column == 1 or column ==  9 or column ==  10):
        valid = False
        
    if (row == 2 or row == 8 ) and (column == 0 or column ==  10):
        valid = False
        
    if (row == 3 or row == 7 ) and (column == 0 or column ==  10):
        valid = False
        
    if (row == 4 or row == 5 or row == 6 ) and (column ==  4 or column ==  5 or column ==  6):
        valid = False
          
    if valid == True:
        if chosen_tower != -1:
            gameDisplay.blit(img,(x+row*40+10,y+column*40+10))
        
def techtree(techtree_font):
    # show the techtree

    label = techtree_font.render("Techtree", True, black)
    gameDisplay.blit(label, (50, CONST_DISPLAY_HEIGHT - 110))

    for i in range(0, len(CONST_TOWER_DAMAGE)):
        label = techtree_font.render("Tower%d" %(i+1) , True, black)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 90))    
        gameDisplay.blit(tower_img[i],(techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 70))     
        label = info_font.render("Cost: %d " % CONST_TOWER_PRICE[i], True, black)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 50))           
        label = info_font.render("Range: %d" % CONST_TOWER_RANGE[i], True, black)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 40))              
        label = info_font.render("Damage: %d" % CONST_TOWER_DAMAGE[i], True, black)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 30)) 
        label = info_font.render("Cooldown: %.1fs" % (CONST_TOWER_COOLDOWN[i]/1000), True, black)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT -20))         
      

def findpos():
    p = pygame.mouse.get_pos()
    row = int((p[0]-x)/40)
    if row <0:
        row =0
    if row > 10:
        row = 10
    column = int((p[1]-y)/40)
    if column < 0:
        column = 0
    if column > 10:
        column = 10
    return(row,column)

def findtower(chosen_tower):
    p = pygame.mouse.get_pos()

   
    if  p[1] > CONST_DISPLAY_HEIGHT - 80 :
        if p[0] <= techtree_x_offset[0]+70:    
            return 0
        elif p[0] > techtree_x_offset[0]+70 and p[0] <= techtree_x_offset[1]+60:
            return 1
        elif p[0] > techtree_x_offset[1]+60 and p[0] <= techtree_x_offset[2]+60:
            return 2  
        elif p[0] > techtree_x_offset[2]+60 and p[0] <= techtree_x_offset[3]+60:
            return 3
        elif p[0] > techtree_x_offset[3]+60 and p[0] <= techtree_x_offset[4]+60:
            return 4               
        else:
            return -1
    else:
        return chosen_tower
    
def check_if_valid():
    valid = True
    if (row == 0 or row == 10) and (column == 0 or column == 1 or column ==  2 or column ==  3 or column == 7 or column == 8 or column ==  9 or column ==  10):
        valid = False
    
    if (row == 1 or row == 9 ) and (column == 0 or column == 1 or column ==  9 or column ==  10):
        valid = False
        
    if (row == 2 or row == 8 ) and (column == 0 or column ==  10):
        valid = False
        
    if (row == 3 or row == 7 ) and (column == 0 or column ==  10):
        valid = False
        
    if (row == 4 or row == 5 or row == 6 ) and (column ==  4 or column ==  5 or column ==  6):
        valid = False
    
    
    
    return valid

 

def cog(r,c):
    cog_x = offs_x+r*40+20
    cog_y = offs_y+c*40+20
    return (cog_x, cog_y)

#create paths
walking_path = []
path_offset_x = CONST_DISPLAY_WIDTH*0.5-(globeimg.get_width()/2)
path_offset_y = CONST_DISPLAY_HEIGHT*0.5-(globeimg.get_height()/2)
walking_path.append([(path_offset_x + 55, path_offset_y+ 45),(path_offset_x + 200, path_offset_y + 80),(path_offset_x + 275, path_offset_y + 130),(path_offset_x + 300, path_offset_y + 190),(path_offset_x + 290, path_offset_y + 240),(path_offset_x + 250, path_offset_y + 265),(path_offset_x + 230, path_offset_y + 215)])
walking_path.append([(path_offset_x + 395, path_offset_y + 385),(path_offset_x+240,path_offset_y+360),(path_offset_x+ 210, path_offset_y + 330),(path_offset_x+220, path_offset_y+290),(path_offset_x+230, path_offset_y + 280),(path_offset_x+250, path_offset_y + 265),(path_offset_x+230,path_offset_y+215)])



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
buymode = False
chosen_tower = -1



while not crashed:
  
    for event in pygame.event.get():
           
        
        if event.type == pygame.QUIT:
            crashed = True          
          
        if buymode == True:    
            #buymode active  
            
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
                                fields[index].health = 100
                                balance = balance - CONST_TOWER_PRICE[chosen_tower]     
                                buymode = False
                                chosen_tower = -1
                        else:
                            print('incufficient funds!')
                    
        else:
            
            # buymode not active
            if event.type == pygame.MOUSEBUTTONUP:       
                print("please press B!") 


        if event.type == pygame.KEYDOWN:
            #check for key-input
            if event.key == pygame.K_b:
                buymode = True
            elif event.key == pygame.K_x:
                buymode = False

                chosen_tower = -1

        
    #clean view    
    gameDisplay.fill(white)   

    #show world
    #show coin balance and globe
    x= CONST_DISPLAY_WIDTH*0.5-(globeimg.get_width()/2)
    y= CONST_DISPLAY_HEIGHT*0.5-(globeimg.get_height()/2)
    globe(x,y)
    coins(50,10)
    
    #generate enemies
    actual_time = pygame.time.get_ticks()
    if game_level == 0:    
        time_to_next_wave = (5000 - actual_time) /1000
        label = wavecounter_font.render("Next wave in: %d seconds" % int(time_to_next_wave) , True, black)
        gameDisplay.blit(label, (230, 100))       
        
    if actual_time > 5000:
        game_level = 1
        
    if game_level == 1:       
        if event_counter <1:
            enemies.append(enemy("Arsch1", 0, 0))
            enemies.append(enemy("Arsch1.1", 0, 1))
            enemies.append(enemy("Arsch1.2", 0, 0))
            enemies.append(enemy("Arsch2", 1, 1))
            
            event_counter = 1
    
        if actual_time > 16000 and event_counter <2:
            enemies.append(enemy("Arsch3", 1, 0))   
            enemies.append(enemy("Arsch3.1", 0, 0))
            event_counter = 2
    
        if actual_time > 17000 and event_counter <3:
            enemies.append(enemy("Arsch4", 1, 1))   
            enemies.append(enemy("Arsch5", 0, 1))  
            event_counter = 3            
                        
   
    
    
    
    
    
    # enemy movement + show enemies
    for i in range(0,len(enemies)):
        
        if enemies[i].get_health() > 0:
            activepath = walking_path[enemies[i].get_type()]
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
                    gameDisplay.blit(enemy_img[enemies[i].get_type()],enemies[i].get_location()) 
                    health = 100* enemies[i].get_health() / CONST_ENEMY_HEALTH[enemies[i].get_type()]
                    if health == 100:
                        resolution_x = 21
                        file = (imgpath+healthbar_img_names[1])
                        image = pygame.image.load(file)                          
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  )                        
                    
                    elif health > 50:
                        resolution_x = 21
                        file = (imgpath+healthbar_img_names[0])
                        image = pygame.image.load(file)                          
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  )    
                        resolution_x = 21*health/CONST_ENEMY_HEALTH[enemies[i].get_type()]
                        file = (imgpath+healthbar_img_names[1])
                        image = pygame.image.load(file)                         
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  )
                    elif health > 25:
                        resolution_x = 21
                        file = (imgpath+healthbar_img_names[0])
                        image = pygame.image.load(file)                          
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  ) 
                        resolution_x = 21*health/CONST_ENEMY_HEALTH[enemies[i].get_type()]
                        file = (imgpath+healthbar_img_names[2])
                        image = pygame.image.load(file)                         
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  )
                    elif health > 0:
                        resolution_x = 21
                        file = (imgpath+healthbar_img_names[0])
                        image = pygame.image.load(file)                          
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  ) 
                        resolution_x = 21*health/CONST_ENEMY_HEALTH[enemies[i].get_type()]
                        file = (imgpath+healthbar_img_names[3])
                        image = pygame.image.load(file)                         
                        gameDisplay.blit(pygame.transform.scale( image , (int(resolution_x) ,3) ), (new_position[0]-3, new_position[1]+20)  )

        
    
    #show snapgrid
    if buymode == True:
        grid(x,y)
        snapgrid(tower_img[chosen_tower],x,y)
        techtree(techtree_font)    

        
    # show towers + deal damage to enemies
    for row in range(0,11):
        for column in range(0,11):
            towertype = fields[row*11+column].get_towertype()
            if towertype != -1:
                gameDisplay.blit(tower_img[towertype],(x+row*40+10,y+column*40+10))
                health = fields[row*11+column].get_health()

                if health > 0:
                    #deal damage to monsters
                    position_tower = cog(row, column)
                    for i in range(0,len(enemies)):                      
                        position_enemy = enemies[i].get_location()
                        distance_to_enemy = sqrt( pow( (position_enemy[0] - position_tower[0]), 2) + pow( (position_enemy[1] - position_tower[1]), 2))   
                        
                        if distance_to_enemy < fields[row*11+column].get_range():
                            enemy_health = enemies[i].get_health()
                            if fields[row*11+column].get_cooldown() < actual_time:
                                new_health = enemy_health - fields[row*11+column].get_damage()          
                                if new_health < 0:
                                    enemies[i].set_health(0)
                                    balance = balance + enemies[i].get_loot()
                                    fields[row*11+column].reset_cooldown(actual_time)
                                    delete_enemies.append(i)
                                else:
                                    enemies[i].set_health(new_health)
                                   
                    for i in range(0,len(delete_enemies)):     
                        del enemies[delete_enemies[i]]   
                    delete_enemies = []
                    
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
                        
        
                   
                        
    pygame.display.update()     
    clock.tick(60)
    

    
    
    

pygame.quit()
quit()
