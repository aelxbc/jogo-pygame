import pygame as pg
from pg.locals import *
from sys import exit
from random import randint


pg.init()

pg.mixer.music.set_volume(0.1)
musica_de_fundo = pg.mixer.music.load('music/BoxCat Games - CPU Talk.mp3')
pg.mixer.music.play(-1)

barulho_colisao = pg.mixer.Sound('music/smw_coin.wav')
largura = 640
altura = 480
x = largura / 2
y = altura / 2 

x_blue = randint(40, 600) 
y_blue = randint(50, 430)

pontos = 0

fonte = pg.font.SysFont('lucidaconsole', 30, True, True)

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Jogo')
relogio = pg.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0,0,0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))

    for event in pg.event.get():
        if event.type == QUIT:
            pg.exit()
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
    if pg.key.get_pressed()[K_a]:
        x_cobra -= 20
    if pg.key.get_pressed()[K_d]:
        x_cobra += 20
    if pg.key.get_pressed()[K_w]:
        y_cobrea -= 20
    if pg.key.get_pressed()[K_s]:
        y_cobra += 20

    # desenhando na tela
    ret_red = pg.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_blue = pg.draw.rect(tela, (0, 0, 255), (x_blue, y_blue, 40, 50))
    
    if ret_red.colliderect(ret_blue):
        x_blue = randint(40, 600) 
        y_blue = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
    
    tela.blit(texto_formatado, (400, 40))


    pg.display.update()

