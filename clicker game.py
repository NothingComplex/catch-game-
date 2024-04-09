import pygame
import sys
import random as rd
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.music.load("331876__furbyguy__idunnometloop.wav")
pygame.mixer.music.play(-1)
width = 850
heigth = 650
screen = pygame.display.set_mode((width,heigth))
pygame.mouse.set_visible(False)
pygame.display.set_caption("Catch!")
logo = pygame.image.load("unnamed.jpg")
pygame.display.set_icon(logo)
filler = pygame.Rect(0,0,1000,1000)
x = rd.randint(0,800)
y = rd.randint(117,600)
catch = pygame.Rect(x,y,50,50)
pos = pygame.mouse.get_pos()
(pox,poy) = pos
mogus = pygame.Rect(pox,poy,5,5)
l = 0
font = pygame.font.Font("freesansbold.ttf",32)
text = font.render(f"score: {l}",True,(0,255,0),(255,255,255))
while True:
    clock.tick(60)
    volume = 100
    font = pygame.font.Font("freesansbold.ttf",32)
    text = font.render(f"score: {l}",True,(0,255,0),None)
    pos = pygame.mouse.get_pos()
    (pox,poy) = pos
    mogus = pygame.Rect(pox,poy,5,5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if catch.colliderect(mogus):
            l += 1
            x = rd.randint(117,800)
            y = rd.randint(0,600)
            catch = pygame.Rect(x,y,50,50)
            r = rd.randint(0,255)
            g = rd.randint(0,255)
            b = rd.randint(0,255)
            pygame.draw.rect(screen,(r,g,b),catch)
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    pygame.draw.rect(screen,(0,255,255),filler)
    pygame.draw.circle(screen,(0,0,200),(425,300),100,100)
    pygame.draw.circle(screen,(0,0,200),(575,300),100,100)
    pygame.draw.circle(screen,(0,0,200),(275,300),100,100)
    pygame.draw.circle(screen,(0,0,200),(125,300),100,100)
    pygame.draw.circle(screen,(0,0,200),(725,300),100,100)
    pygame.draw.circle(screen,(0,0,200),(-25,300),100,100)
    pygame.draw.circle(screen,(0,0,200),(875,300),100,100)
    pygame.draw.circle(screen,(0,0,200),(425,400),100,100)
    pygame.draw.circle(screen,(0,0,200),(425,550),100,100)
    pygame.draw.circle(screen,(0,0,200),(425,675),100,100)
    pygame.draw.circle(screen,(0,0,200),(425,200),100,100)
    pygame.draw.circle(screen,(0,0,200),(425,75),100,100)
    pygame.draw.circle(screen,(0,0,200),(425,-25),100,100)
    pygame.draw.rect(screen,(r,g,b),catch)
    screen.blit(text,(350,35))
    pygame.draw.rect(screen,(255,0,0),mogus)
    pygame.display.flip()