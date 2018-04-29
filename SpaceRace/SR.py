import pygame, sys, random
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Space Race')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,800))
score = 0
pygame.mouse.set_visible(0)
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 36)
ship = pygame.image.load('Spaceships\player1.png')
enemy = pygame.image.load('Spaceships\Enemy1.png')
bomb = pygame.image.load('Spaceships\Bomb1.png')
shot = pygame.image.load('Spaceships\Bullet1.png')
a = 0
alien_x = []
alien_y = []
shoot_y=0
shoot_x=0
enemy_left = 0
enemy_top = 0
bomb_x1 = 0
bomb_x2 = 0
bomb_x3 = 0
bomb_y1 = 0
bomb_y2 = 0
bomb_y3 = 0
enemies = 0

r = 1
while r != 0:
    clock.tick(60)
    screen.fill((0,0,0))
    x,y = pygame.mouse.get_pos()
    screen.blit(ship,(x-42,y))
    while enemies < 8:
        
        enemy_left = 200
        if enemies == 0:
            enemy_left = 200
            
            xposition = 250
            yposition = 24
            alien_x.append(xposition)
            alien_y.append(yposition)
            enemies += 1
        else:
            enemy_left +=  enemies*100
            xposition = enemy_left + 50
            yposition = 24
            alien_x.append(xposition)
            alien_y.append(yposition)
            
            enemies +=1
            
    for i in range(len(alien_x)):
        screen.blit(enemy,(alien_x[i]-50,-1))
   
    
 
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==MOUSEBUTTONDOWN:
            shoot_y = y
            shoot_x = x
            i = random.randint(0,7)
            j = random.randint(0,7)
            k = random.randint(0,7)
            bomb_x1 = alien_x[i] 
            bomb_y1 = alien_y[i]
            bomb_x2 = alien_x[j] 
            bomb_y2 = alien_y[j]
            bomb_x3 = alien_x[k] 
            bomb_y3 = alien_y[k]
            
    if 0<bomb_y1 < 800:
        screen.blit(bomb,(bomb_x1,bomb_y1)) 
        bomb_y1 += 10
    
        
    if 0<bomb_y2 < 800:
        screen.blit(bomb,(bomb_x2,bomb_y2))
        bomb_y2 += 10
        
    if 0<bomb_y3 < 800:
        screen.blit(bomb,(bomb_x3,bomb_y3))
        bomb_y3 += 10
        
    if shoot_y >37:
        screen.blit(shot,(shoot_x,shoot_y))
        shoot_y -= 10
    
    
    if 200<x<1000:
       if -1<y<49:
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        r = 0
        
    if x+40 > bomb_x1 and x-40 < bomb_x1 and y+10 > bomb_y1 and y-10<bomb_y1:
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        r = 0
    if x+40 > bomb_x2 and x-40 < bomb_x2 and y+10 > bomb_y2 and y-10<bomb_y2:
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        r = 0
    if x+40 > bomb_x3 and x-40 < bomb_x3 and y+10 > bomb_y3 and y-10<bomb_y3:
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        r = 0
    if 200<shoot_x<1000:
       if 38<shoot_y<49:
           score +=1
    if score == 10:
        enemy = pygame.image.load('Spaceships\Enemy2.png')
        text = font.render("You Have Won the Space Race!", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        
        
    
    pygame.display.update()
pygame.quit()   
    

        