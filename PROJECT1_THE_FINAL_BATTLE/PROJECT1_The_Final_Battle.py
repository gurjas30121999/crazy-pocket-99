#IMPORTING AND INITIALISING PYGAME:
import pygame
from pygame import mixer
pygame.init()
#IMPORTING RANDOM:
import random
#IMPORTING MATH:
import math
#SETTING UP THE SCREEN:
screen=pygame.display.set_mode((800,600))
#BACKGROUND:
back=pygame.image.load('background.png')
#BACKGROUND SOUND:
mixer.music.load('backsound.wav')
mixer.music.play(-1)
#CAPTION AND ICON:
pygame.display.set_caption("THE FINAL BATTLE")
icon=pygame.image.load("tanker.png")
pygame.display.set_icon(icon)
#PLAYER:
playerimg=pygame.image.load('player.png')
playerimgx=370
playerimgy=480
playerxchange=0#FOR CHANGING POSITION OF PLAYER.
#ENEMY:
enemyimg=[]
enemyimgx=[]
enemyimgy=[]
enemyxchange=[]
enemyychange=[]
number=6
for i in range(number):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyimgx.append(random.randint(0,800))
    enemyimgy.append(random.randint(50,150))
    enemyxchange.append(4)#FOR CHANGING POSITION OF ENEMY.
    enemyychange.append(40)#FOR CHANGING POSITION OF ENEMY.
#BULLET:
bulletimg=pygame.image.load('bullet.png')
bulletimgx=0
bulletimgy=480
bulletxchange=0
bulletychange=10
bulletstate='ready'
#SCORES:
s=0
font=pygame.font.Font('freesansbold.ttf',32)
scorex=10
scorey=10
#GAME OVER TEXT:
overfont=pygame.font.Font('freesansbold.ttf',64)
def showscore(x,y):
    score=font.render("SCORE:"+str(s),True,(0,255,0))
    screen.blit(score,(x,y))

def gameover():
    overtext=overfont.render("GAME OVER",True,(0,255,0))
    screen.blit(overtext,(200,300))
    
#POSITION OF PLAYER:
def player(x,y):
    screen.blit(playerimg,(x,y))
#POSITION OF ENEMY:
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
#POSITION OF BULLET:
def bullet(x,y):
    global bulletstate
    bulletstate='fire'
    screen.blit(bulletimg,(x+16,y+10))
#COLLISION:
def iscollision(enemyimgx, enemyimgy, bulletimgx, bulletimgy):
    d=math.sqrt(math.pow(enemyimgx-bulletimgx,2)+ math.pow(enemyimgy-bulletimgy,2))
    if d<27:
        return True
    else:
        return False

         
    

#GAME LOOP:
running=True
while running:
    screen.fill((0, 255, 122))
    screen.blit(back,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #KEY CONTROLS:
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerxchange=-5
            if event.key==pygame.K_RIGHT:
                playerxchange=5
            if event.key==pygame.K_SPACE:
                if bulletstate is 'ready':#FOR ENSURING NO PRESSING OF SPACBAR UNTIL ONE BULLET REACHES THE TOP. 
                    shot=mixer.Sound('target.wav')
                    shot.play()
                    bulletimgx=playerimgx
                    bullet(bulletimgx,bulletimgy)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerxchange=0
    #PLLAYER MOTION STATEMENT:    
    playerimgx+=playerxchange
    #BOUNDING MOVEMENT OF PLAYER:
    if playerimgx<=0:
        playerimgx=0
    elif playerimgx>=736:
        playerimgx=736
    #ENEMY MOTION STATEMENT:
    for i in range(number):
        #GAME OVER:
        if enemyimgy[i]>=440:
            for j in range(number):
                enemyimgx[j]=2000
            gameover()
            break
        
        enemyimgx[i]+=enemyxchange[i]
        if enemyimgx[i]<=0:
            enemyxchange[i]=4
            enemyimgy[i]+=enemyychange[i]
        elif enemyimgx[i]>=736:
            enemyxchange[i]=-4
            enemyimgy[i]+=enemyychange[i]
        #COLLISION AFTERSTEPS:
        collision=iscollision(enemyimgx[i], enemyimgy[i], bulletimgx, bulletimgy)
        if collision:
            exp_sound=mixer.Sound('explode.wav')
            exp_sound.play()
            bulletimgy=480
            bulletstate='ready'
            s+=5
            enemyimgx[i]=random.randint(0,735)
            enemyimgy[i]=random.randint(50,150)
        enemy(enemyimgx[i],enemyimgy[i],i)
    #ENSURING MULTIPLE BULLETS:
    if bulletimgy<=0:
        bulletstate='ready'
        bulletimgy=480
    #BULLET MOVEMENT:
    if bulletstate is'fire':
        bullet(bulletimgx,bulletimgy)
        bulletimgy-=bulletychange
    
        
    player(playerimgx,playerimgy)
    showscore(scorex,scorey)
    pygame.display.update()
    
