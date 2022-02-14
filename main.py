import pygame 
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

largura = 640
altura = 480
x = largura / 2
y = altura / 2 

x_blue = randint(40, 600) 
y_blue = randint(50, 430)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            if event.key == K_d:
                x += 20
            if event.key == K_w:
                y -= 20
            if event.key == K_s:
                y += 20
        '''
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20

    # desenhando na tela
    ret_red = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_blue = pygame.draw.rect(tela, (0, 0, 255), (x_blue, y_blue, 40, 50))
    
    if ret_red.colliderect(ret_blue):
        x_blue = randint(40, 600) 
        y_blue = randint(50, 430)


    pygame.display.update()

