# Thingy Moving around the screen game 
# Made by Carlie
# Carlie is awesome

# To Do
# have a "play again" text make it clickable
# also exit isn't working in the end loop


import random, pygame, sys, math, pygame.freetype, time, json
from pygame.locals import *

pygame.init()

FPS = 30 
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((600,500),0, 32)
pygame.display.set_caption('Catch the Cat')


white = (255,255,255)


DISPLAYSURF.fill(white)
catImg = pygame.image.load('cat.png')
catLifeImgURL = pygame.image.load('catlife.png')


def blit_alpha(target, source, location, opacity):  # this will hopefully change opacity
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)


GAME_FONT = pygame.freetype.SysFont("Impact", 24)
GAMEOVER_FONT = pygame.freetype.SysFont("Impact", 50)
score = 0
highscore = 0
with open('dict.json', 'r') as f:
    highscore = json.load(f)



catx = 10
caty = 10
direction = 'rightdown'
movediagonal = (catx + caty)
randomdirection = ["leftdown", "leftup", "rightdown", "rightup"]
shake_start_time = int(time.time())
cat_life_counter = 0



while True: # the main game loop
    DISPLAYSURF.fill(white)
    DISPLAYSURF.blit(catImg, (catx, caty))
    blit_alpha(DISPLAYSURF, catLifeImgURL, (10, 10), 250)
    blit_alpha(DISPLAYSURF, catLifeImgURL, (60, 10), 250)
    blit_alpha(DISPLAYSURF, catLifeImgURL, (110, 10), 250)
    blit_alpha(DISPLAYSURF, catLifeImgURL, (160, 10), 250)
    blit_alpha(DISPLAYSURF, catLifeImgURL, (210, 10), 250)
    blit_alpha(DISPLAYSURF, catLifeImgURL, (260, 10), 250)
    blit_alpha(DISPLAYSURF, catLifeImgURL, (310, 10), 250)
    blit_alpha(DISPLAYSURF, catLifeImgURL, (360, 10), 250)
    blit_alpha(DISPLAYSURF, catLifeImgURL, (410, 10), 250)
    
     
    GAME_FONT.render_to(DISPLAYSURF, (25, 470), "Cat Hit Counter: " +str(score), (0, 0, 0))
    
    fpsClock.tick(FPS)
       
    
    if direction == 'leftup':
        caty -= random.randint(5,10)
        catx -= random.randint(5,10)
        movediagonal
        if caty <= 10:
            direction = 'leftdown'
        if catx <= 10:
            direction = 'rightup'
    elif direction == 'leftdown':
        catx -= random.randint(5,10)
        caty += random.randint(5,10)
        movediagonal
        if catx <= 10:
            direction = 'rightdown'
        if caty >= 420:
            direction = 'leftup'
    elif direction == 'rightdown':
        catx += random.randint(5,10)
        caty += random.randint(5,10)
        movediagonal
        if catx >= 480:
            direction = "leftdown"
        if caty >= 420:
            direction = "rightup"
    elif direction == 'rightup':
        caty -= random.randint(5,10)
        catx += random.randint(5,10)
        movediagonal
        if catx >= 480:
            direction = 'leftup'
        if caty <= 10:
            direction = 'rightdown'
    elif direction == "shake":
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        wave_height = 5.0
        wave_length = 10.0
        shake_x = wave_height*math.sin(time.time()*wave_length)
        catx = catx + shake_x
        shake_time = int(time.time() - shake_start_time)
        if shake_time >= 1:
            direction = random.choice(randomdirection)  
            FPS += 10
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    elif direction == "shake_game_over":
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        #DISPLAYSURF.blit(replaytext,replayRect)
        #replayRect = pygame.draw.rect(DISPLAYSURF, blue, (50,50,230,90))
        GAMEOVER_FONT.render_to(DISPLAYSURF, (50, 50), "Game Over", (0, 0, 0))
        wave_height = 5.0
        wave_length = 10.0
        shake_x = wave_height*math.sin(time.time()*wave_length)
        catx = catx + shake_x
        if score >= highscore:
            highscore = score
            jsonwrite = json.dumps(highscore)
            p = open("dict.json", "w")
            p.write(str(highscore))
        replay_text = GAME_FONT.render_to(DISPLAYSURF, (60, 100), "High score: " +str(highscore), (0, 0, 0))
        

    if cat_life_counter >= 9:
            pygame.draw.rect(DISPLAYSURF, white, (10,10,50, 30))
            blit_alpha(DISPLAYSURF, catLifeImgURL, (10, 10), 128)
    if cat_life_counter >= 8:
            pygame.draw.rect(DISPLAYSURF, white, (60,10,50, 30))
            blit_alpha(DISPLAYSURF, catLifeImgURL, (60, 10), 128)
    if cat_life_counter >= 7:
            pygame.draw.rect(DISPLAYSURF, white, (110,10,50, 30))
            blit_alpha(DISPLAYSURF, catLifeImgURL, (110, 10), 128)
    if cat_life_counter >= 6:
            pygame.draw.rect(DISPLAYSURF, white, (160,10,50, 30))
            blit_alpha(DISPLAYSURF, catLifeImgURL, (160, 10), 128)
    if cat_life_counter >= 5:
            pygame.draw.rect(DISPLAYSURF, white, (210,10,50, 30))
            blit_alpha(DISPLAYSURF, catLifeImgURL, (210, 10), 128)
    if cat_life_counter >= 4:
            pygame.draw.rect(DISPLAYSURF, white, (260,10,50, 30))
            blit_alpha(DISPLAYSURF, catLifeImgURL, (260, 10), 128)
    if cat_life_counter >= 3:
            pygame.draw.rect(DISPLAYSURF, white, (310,10,50, 30))
            blit_alpha(DISPLAYSURF, catLifeImgURL, (310, 10), 128)
    if cat_life_counter >= 2:
            pygame.draw.rect(DISPLAYSURF, white, (360,10,50, 30))
            blit_alpha(DISPLAYSURF, catLifeImgURL, (360, 10), 128)
    if cat_life_counter >= 1:
            pygame.draw.rect(DISPLAYSURF, white, (410,10,50, 30))
            blit_alpha(DISPLAYSURF, catLifeImgURL, (410, 10), 128)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            catxsize = catx + 125
            catysize = caty + 80
            mx, my = pygame.mouse.get_pos()
            if catx <= mx <= catxsize and caty <= my <= catysize:
                score += 1
                shake_start_time = int(time.time())
                direction = "shake"
            else:
                cat_life_counter += 1
                if cat_life_counter >= 9:
                        direction = "shake_game_over"
                        #if event.type == pygame.MOUSEBUTTONDOWN:
                        #        if replayRect.collidepoint(event.pos):
                         #           print("restart the game mofo")
                                    #restart the game 
                
  
    pygame.display.update()
    

                 
                        
                        
                    
                
                    
             
