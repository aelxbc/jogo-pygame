import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint


pg.init()

pg.mixer.music.set_volume(0.1)
musica_de_fundo = pg.mixer.music.load('music/BoxCat Games - CPU Talk.mp3')
pg.mixer.music.play(-1)

barulho_colisao = pg.mixer.Sound('music/smw_coin.wav')
largura = 640
altura = 480
x_cobra = largura / 2
y_cobra = altura / 2 

x_maca = randint(40, 600) 
y_maca = randint(50, 430)

pontos = 0

fonte = pg.font.SysFont('lucidaconsole', 30, True, True)

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Jogo')
relogio = pg.time.Clock()
lista_cobra = []

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y
        pg.draw.rect(tela, (0, 255, 0,0), (XeY[0], XeY[1], 20, 20))

    pass

while True:
    relogio.tick(60)
    tela.fill((255,255,255))

    mensagem = f'Pontos: {pontos}'
    tex_cobrato_formatado = fonte.render(mensagem, False, (0, 0, 0))

    for event in pg.event.get():
        if event.type == QUIT:
            pg.exit()
            exit()
        '''
        if event.ty_cobrape == keyDOWN:
            if event.key == K_a:
                x_cobra -= 20
            if event.key == K_d:
                x_cobra += 20
            if event.key == K_w:
                y_cobra -= 20
            if event.key == K_s:
                y_cobra += 20
        '''
    if pg.key.get_pressed()[K_a]:
        x_cobra -= 20
    if pg.key.get_pressed()[K_d]:
        x_cobra += 20
    if pg.key.get_pressed()[K_w]:
        y_cobra -= 20
    if pg.key.get_pressed()[K_s]:
        y_cobra += 20

    # desenhando na tela
    cobra = pg.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pg.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600) 
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()

    
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    aumenta_cobra(lista_cobra)


    tela.blit(tex_cobrato_formatado, (400, 40))



    pg.display.update()

