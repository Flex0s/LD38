'''
Created on 22.04.2017

@author: Flex

beware: i mixed up the names for row and columns, 
'''
from optparse import check_builtin
from building import building


if __name__ == '__main__':
    pass


import pygame

pygame.init()
pygame.font.init()

display_width = 1024
display_height = 768
gamepath = 'E:\_Work\LD38\\'
imgpath = gamepath + 'sprites\\'

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('LD38 - A small world - by Flex')
clock = pygame.time.Clock()

techtree_font = pygame.font.SysFont("Arial", 15)
info_font = pygame.font.SysFont("Arial", 10)


#Tower1
range_t1 = 5
damage_t1 = 5
cost_t1 = 5 

#Tower2
range_t2 = 10
damage_t2 = 10
cost_t2 = 10

#Tower3
range_t3 = 15
damage_t3 = 15
cost_t3 = 15

#Tower4
range_t4 = 20
damage_t4 = 20 
cost_t4 = 20

#Tower5
range_t5 = 25 
damage_t5 = 25 
cost_t5 = 25

#starting coins
balance = 10000


white = (255,255,255)
black = (0,0,0)



globeimg = pygame.image.load(imgpath + 'world.png').convert_alpha()
gridimg = pygame.image.load(imgpath + 'world_grid.png').convert_alpha() 
t1img = pygame.image.load(imgpath + 'Tower1.png')
t2img = pygame.image.load(imgpath + 'Tower2.png')
t3img = pygame.image.load(imgpath + 'Tower3.png')
t4img = pygame.image.load(imgpath + 'Tower4.png')
t5img = pygame.image.load(imgpath + 'Tower5.png')


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
        
    if (row == 3 or row == 7 ) and (column == 0 or column ==  4 or column ==  5 or column ==  6 or column ==  10):
        valid = False
        
    if (row == 4 or row == 5 or row == 6 ) and (column == 3 or column ==  4 or column ==  5 or column ==  6 or column ==  7):
        valid = False
          
    if valid == True:
        gameDisplay.blit(img,(x+row*40+10,y+column*40+10))
        
def techtree():
    # show the techtree
    label = techtree_font.render("Techtree", True, black)
    gameDisplay.blit(label, (50, display_height - 100))
    
    #Tower1
    x_offs = 50
    label = techtree_font.render("Tower1", True, black)
    gameDisplay.blit(label, (x_offs, display_height - 80))    
    gameDisplay.blit(t1img,(x_offs, display_height - 60))     
    label = info_font.render("Cost: %d " % cost_t1, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 40))           
    label = info_font.render("Range: %d" % cost_t1, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 30))              
    label = info_font.render("Damage: %d" % cost_t1, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 20)) 
    
    #Tower2    
    x_offs=130
    label = techtree_font.render("Tower2", True, black)
    gameDisplay.blit(label, (x_offs, display_height - 80))    
    gameDisplay.blit(t2img,(x_offs, display_height - 60)) 
    label = info_font.render("Cost: %d " % cost_t2, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 40))           
    label = info_font.render("Range: %d" % cost_t2, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 30))              
    label = info_font.render("Damage: %d" % cost_t2, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 20)) 
        
    #Tower3    
    x_offs=210  
    label = techtree_font.render("Tower3", True, black)
    gameDisplay.blit(label, (x_offs, display_height - 80))    
    gameDisplay.blit(t3img,(x_offs, display_height - 60)) 
    label = info_font.render("Cost: %d " % cost_t3, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 40))           
    label = info_font.render("Range: %d" % cost_t3, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 30))              
    label = info_font.render("Damage: %d" % cost_t3, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 20)) 

    #Tower4  
    x_offs=280
    label = techtree_font.render("Tower4", True, black)
    gameDisplay.blit(label, (x_offs, display_height - 80))    
    gameDisplay.blit(t4img,(x_offs, display_height - 60)) 
    label = info_font.render("Cost: %d " % cost_t4, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 40))           
    label = info_font.render("Range: %d" % cost_t4, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 30))              
    label = info_font.render("Damage: %d" % cost_t4, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 20)) 

    #Tower5   
    x_offs =350
    label = techtree_font.render("Tower5", True, black)
    gameDisplay.blit(label, (x_offs, display_height - 80))    
    gameDisplay.blit(t5img,(x_offs, display_height - 60))  
    label = info_font.render("Cost: %d " % cost_t5, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 40))           
    label = info_font.render("Range: %d" % cost_t5, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 30))              
    label = info_font.render("Damage: %d" % cost_t5, True, black)
    gameDisplay.blit(label, (x_offs, display_height - 20))    
    
    

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

def cog(r,c):
    offs_x= display_width*0.5-(globeimg.get_width()/2)
    offs_y= display_height*0.5-(globeimg.get_height()/2)
    cog_x = offs_x+r*40+20
    cog_y = offs_y+c*40+20
    return (cog_x, cog_y)

#initialize Buildings with 'none'
fields = []

for row in range(0,11):
    for column in range(0,11):
        fields.append(building(row,column,'none',0))




crashed = False
buymode = False
chosen_tower = 'none'

while not crashed:
    
    for event in pygame.event.get():
        gameDisplay.fill(white)     
        
        if event.type == pygame.QUIT:
            crashed = True          
      
        x= display_width*0.5-(globeimg.get_width()/2)
        y= display_height*0.5-(globeimg.get_height()/2)
        globe(x,y)
        coins(50,10)
        
        if buymode == True:      
            grid(x,y)
            if(chosen_tower != 'none'):
                snapgrid(t1img,x,y)
            techtree()
            
            if event.type == pygame.MOUSEBUTTONUP:              
                
                
                
                
                  
                (row,column) = findpos()                      
                index = row*11 + column
                fields[index].set_towertype(chosen_tower)          
                buymode = False
                chosen_tower = 'none'
                
                
                
        else:        
            for row in range(0,11):
                for column in range(0,11):
                    tower = fields[row*11+column].get_towertype()
                    if ( tower == 't1'):
                        gameDisplay.blit(t1img,(x+row*40+10,y+column*40+10))
                    elif ( tower == 't2'):
                        gameDisplay.blit(t2img,(x+row*40+10,y+column*40+10))
                    elif ( tower == 't3'):
                        gameDisplay.blit(t3img,(x+row*40+10,y+column*40+10))                       
                    elif ( tower == 't4'):
                        gameDisplay.blit(t4img,(x+row*40+10,y+column*40+10))
                    elif ( tower == 't5'):
                        gameDisplay.blit(t5img,(x+row*40+10,y+column*40+10))             
        
      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                buymode = True
            elif event.key == pygame.K_x:
                buymode = False




    pygame.display.update()     
    clock.tick(60)

pygame.quit()
quit()
