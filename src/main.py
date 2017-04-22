'''
Created on 22.04.2017

@author: Flex
'''
from optparse import check_builtin

if __name__ == '__main__':
    pass


import pygame

pygame.init

display_width = 1024
display_height = 768
gamepath = 'E:\_Work\LD38\\'
imgpath = gamepath + 'sprites\\'

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('LD38 - A small world - by Flex')
clock = pygame.time.Clock()


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
    
def snapgrid(img,x,y):
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
    
    


crashed = False
buymode = False

while not crashed:
    
    for event in pygame.event.get():
        gameDisplay.fill(white)   
        x= display_width*0.5-(globeimg.get_width()/2)
        y= display_height*0.5-(globeimg.get_height()/2)
        
        globe(x,y)
        grid(x,y)        
        
        if event.type == pygame.QUIT:
            crashed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                buymode = True
            elif event.key == pygame.K_x:
                buymode = False
        print (buymode)
        
        for r in range(0,11):
            for c in range(0,11):
                
                
                
            
        
        
        
        if buymode == True:
            if event.type == pygame.MOUSEMOTION:
                snapgrid(t1img,x,y)

        
   
    
  
      
    
    pygame.display.update()       
        
    clock.tick(60)

pygame.quit()
quit()
