'''
Created on 22.04.2017

@author: Flex

beware: i mixed up the names for row and columns, 
'''
from optparse import check_builtin
from building import building
from enemy import enemy
from math import sqrt


if __name__ == '__main__':
    pass


import pygame

pygame.init()
pygame.font.init()


CONST_DISPLAY_WIDTH = 1024
CONST_DISPLAY_HEIGHT = 768

CONST_TOWER_DAMAGE = [5,10,15,20,25]
CONST_TOWER_RANGE = [5,10,15,20,25]
CONST_TOWER_PRICE = [5,10,15,20,25]





gamepath = 'E:\_Work\LD38\\'
imgpath = gamepath + 'sprites\\'

gameDisplay = pygame.display.set_mode((CONST_DISPLAY_WIDTH,CONST_DISPLAY_HEIGHT))
pygame.display.set_caption('LD38 - A small world - by Flex')
clock = pygame.time.Clock()

   
techtree_font = pygame.font.SysFont("Arial", 15)
info_font = pygame.font.SysFont("Arial", 10)




techtree_x_offset = [50, 130, 210, 280, 350]
tower_img =[ pygame.image.load(imgpath + 'Tower1.png') , pygame.image.load(imgpath + 'Tower2.png') , pygame.image.load(imgpath + 'Tower3.png') , pygame.image.load(imgpath + 'Tower4.png') , pygame.image.load(imgpath + 'Tower5.png')]


healthbar_img_names = ['Healthbar_schwarz.png','Healthbar_gruen.png','Healthbar_gelb.png','Healthbar_rot.png']

#starting coins
balance = 10000


white = (255,255,255)
black = (0,0,0)



globeimg = pygame.image.load(imgpath + 'world.png').convert_alpha()
gridimg = pygame.image.load(imgpath + 'world_grid.png').convert_alpha() 



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
        
def techtree():
    # show the techtree
    label = techtree_font.render("Techtree", True, black)
    gameDisplay.blit(label, (50, CONST_DISPLAY_HEIGHT - 100))

    for i in range(0, len(CONST_TOWER_DAMAGE)):
        label = techtree_font.render("Tower%d" %(i+1) , True, black)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 80))    
        gameDisplay.blit(tower_img[i],(techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 60))     
        label = info_font.render("Cost: %d " % CONST_TOWER_PRICE[i], True, black)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 40))           
        label = info_font.render("Range: %d" % CONST_TOWER_RANGE[i], True, black)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 30))              
        label = info_font.render("Damage: %d" % CONST_TOWER_DAMAGE[i], True, black)
        gameDisplay.blit(label, ( techtree_x_offset[i], CONST_DISPLAY_HEIGHT - 20)) 
      

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
    offs_x= CONST_DISPLAY_WIDTH*0.5-(globeimg.get_width()/2)
    offs_y= CONST_DISPLAY_HEIGHT*0.5-(globeimg.get_height()/2)
    cog_x = offs_x+r*40+20
    cog_y = offs_y+c*40+20
    return (cog_x, cog_y)

#create paths
walking_path = []
path_offset_x = CONST_DISPLAY_WIDTH*0.5-(globeimg.get_width()/2)
path_offset_y = CONST_DISPLAY_HEIGHT*0.5-(globeimg.get_height()/2)
walking_path.append([(path_offset_x + 55, path_offset_y+ 45),(path_offset_x + 200, path_offset_y + 80),(path_offset_x + 275, path_offset_y + 130),(path_offset_x + 300, path_offset_y + 190),(path_offset_x + 290, path_offset_y + 240),(path_offset_x + 250, path_offset_y + 265),(path_offset_x + 230, path_offset_y + 215)])
walking_path.append([(path_offset_x + 395, path_offset_y + 385),(path_offset_x+240,path_offset_y+360),(path_offset_x+ 210, path_offset_y + 330),(path_offset_x+220, path_offset_y>+290),(path_offset_x+230, path_offset_y + 280),(path_offset_x+250, path_offset_y + 265),(path_offset_x+230,path_offset_y+215)])





#initialize Buildings with 'none'
fields = []

for row in range(0,11):
    for column in range(0,11):
        fields.append(building(row,column,-1,0))




crashed = False
buymode = False
chosen_tower = -1

while not crashed:
    arsch1 = enemy("Arsch1", 20, 100, 3, 1, 0)
    
    
    
    
    
    
    for event in pygame.event.get():
        gameDisplay.fill(white)     
        
        if event.type == pygame.QUIT:
            crashed = True          
      
        #show coin balance and globe
        x= CONST_DISPLAY_WIDTH*0.5-(globeimg.get_width()/2)
        y= CONST_DISPLAY_HEIGHT*0.5-(globeimg.get_height()/2)
        globe(x,y)
        coins(50,10)
        
        
        if buymode == True:    
            #buymode active  
            grid(x,y)
            techtree()

            
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
                    
                        
                                  
      
            snapgrid(tower_img[chosen_tower],x,y)
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

        

                        
        # enemy movement
        activepath = walking_path[arsch1.get_path()]
        actual_location = arsch1.get_location()
        sector = arsch1.get_sector()
        if sector == 0:
             #new enemy
            arsch1.set_location(activepath[0])
            arsch1.set_sector(1)
            
        else:
            target_location= activepath[sector]
            
            
            

            distance_to_next_waypoint = sqrt( pow( (target_location[0] - actual_location[0]), 2) + pow( (target_location[1] - actual_location[1]), 2))
      
            

        
        # damage dealing                
        # towers
        
        
        # enemy     
        
        
        #show enemies
        
        
        
        
        
        
        # show towers
        for row in range(0,11):
            for column in range(0,11):
                towertype = fields[row*11+column].get_towertype()
                if towertype != -1:
                    gameDisplay.blit(tower_img[towertype],(x+row*40+10,y+column*40+10))
                    health = fields[row*11+column].get_health()
                    
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
