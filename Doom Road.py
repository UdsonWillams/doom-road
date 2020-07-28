import pygame
from random import randint
from time import sleep
pygame.init()
x = 350  # 350 carro no meio / 510 o maximo para a direita / 170 o maximo para a esquerda
y = 360  # 360 carro no meio /
pos_x = 180
pos_y_carro1 = -500
pos_y_carro2 = -200
pos_y_carro3 = -400
velocidade = 12
velocidade_carro1 = 14    #VARIAVEIS DE COMANDO DOS PERSONAGENS
velocidade_carro2 = 16
velocidade_carro3 = 16
timer = 0
tempo_segundo = 0
vida = 3

fundo = pygame.image.load("tela.png")
carro = pygame.image.load("carro.png")
carro1 = pygame.image.load("carro1.png")  # VARIAVEIS DE CARREGAMENTO DAS SPRITES
carro2 = pygame.image.load("carro2.png")
carro3 = pygame.image.load("carro3.png")


#  ALGORITIMO PARA ESCRITA DE TEXTO NA ESQUERDA DA TELA DO JOGO
font = pygame.font.SysFont('arial black', 20)
texto = font.render("TEMPO: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

# ALGORITIMO PARA ESCRITA DE TEXTO NA ESQUERDA DA TELA DO JOGO
texto2 = font.render("VIDAS : ", True, (255, 0, 0), (0, 0, 0))
pos_texto2 = texto.get_rect()
pos_texto2.center = (65, 80)

texto3 = font.render("CARREGANDO...", True, (255, 0, 0), (0, 0, 0))
pos_texto3 = texto.get_rect()
pos_texto3.center = (350, 350)

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Doom Road")
# tela de inicio
sleep(0.5)
inicio = pygame.image.load("inicio.png")
pygame.mixer.music.load('carroligando.mp3')
pygame.mixer.music.play()
janela.blit(inicio, (0, 0))
pygame.display.update()
sleep(4.5)

janela_aberta = True

pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

while janela_aberta:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    # if comandos[pygame.K_w]:
    #    y -= velocidade
    # if comandos[pygame.K_s]:
    #    y += velocidade
    if comandos[pygame.K_d] and x <= 510:
        x += velocidade
    if comandos[pygame.K_a] and x >= 170:
        x -= velocidade

    # DETECTOR DE COLISÃO

    if x + 75 > (pos_x + 320) and y - 170 < pos_y_carro3: # COLISAO DA DIREITA, CARRO 3
        y = 1000        #l 420 > 500 e 190 < -350
        vida -= 1
        x = 350  # 350 carro no meio / 510 o maximo para a direita / 170 o maximo para a esquerda
        y = 360  # 360 carro no meio /
        pos_x = 180
        pos_y_carro1 = -500
        pos_y_carro2 = -200
        pos_y_carro3 = -400
    if x - 75 < pos_x and y - 170 < pos_y_carro1: # COLISAO DA ESQUERDA, CARRO 1
        y = 1000        #x = 350y = 360posx = 180
        vida -= 1
        x = 350  # 350 carro no meio / 510 o maximo para a direita / 170 o maximo para a esquerda
        y = 360  # 360 carro no meio /
        pos_x = 180
        pos_y_carro1 = -500
        pos_y_carro2 = -200
        pos_y_carro3 = -400

    if x + 75 > (pos_x + 160) and y - 170 < pos_y_carro2 and (x - 75 < (pos_x + 160) and y + 170 > pos_y_carro2):
        y = 1200                # 420 > 340 e 190 < -200  e 280 < 340 e 440 > -200
        vida -= 1                           #     v  e f                    v e v
        x = 350  # 350 carro no meio / 510 o maximo para a direita / 170 o maximo para a esquerda
        y = 360  # 360 carro no meio /
        pos_x = 180
        pos_y_carro1 = -500
        pos_y_carro2 = -200
        pos_y_carro3 = -400
    # ------------------------------------------------------------------------------------------------------------
    # LUGAR AONDE OS CARROS VAO DPS DE PASSAR A TELA
    aleatorio_carro1 = randint(80, 600)
    aleatorio_carro2 = randint(1700, 2200)
    aleatorio_carro3 = randint(800, 1500)

    # ALGORITIMO DE MUDANÇA DO TEMPO, JA QUE A TELA ATUALIZA A CADA 50MILISEGUNDOS, TIMER RECEBERA +1 20 VEZES, OQUE DARA 1 SEGUNDO
    # LOGO SERA MOSTRADO O TEMPO_SEGUNDO COMO 1, + UMA SEQUENCIA E MUDARA PARA 2 E ASSIM POR DIANTE

    if timer < 20:
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("TEMPO: " + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0
    # ------------------------------------------------------------------------------------------


    if pos_y_carro1 > 600:
        pos_y_carro1 = -aleatorio_carro1
    if pos_y_carro2 > 600:
        pos_y_carro2 = -aleatorio_carro2
    if pos_y_carro3 > 600:
        pos_y_carro3 = -aleatorio_carro3

    pos_y_carro1 += velocidade_carro1  # incremento da posicao dos outros carros, oque faz o carro inimigo se mecher
    pos_y_carro2 += velocidade_carro2
    pos_y_carro3 += velocidade_carro3

    janela.blit(fundo, (0, 0))  # adiciona o fundo o 0, 0 representa aonde ele deve começar
    janela.blit(carro, (x, y))  # adciona o carinho nas posições x e y
    janela.blit(carro1, (pos_x, pos_y_carro1))
    janela.blit(carro2, (pos_x + 160, pos_y_carro2))
    janela.blit(carro3, (pos_x + 320, pos_y_carro3))
    janela.blit(texto, pos_texto)  # : Diz oque voce quer que apareça e em que posição
    janela.blit(texto2, pos_texto2)
    texto2 = font.render("VIDAS: " + str(vida), True, (255, 0, 0), (0, 0, 0))
    pygame.display.update()
    if vida <= 0:
        pygame.mixer.music.stop()
        gameover = pygame.image.load("gameover.png")
        del fundo
        janela.blit(gameover, (0, 0))
        pygame.display.update()
        sleep(5)
        break
    if tempo_segundo > 60:
        pygame.mixer_music.stop()
        vencedor = pygame.image.load("vencedor.png")
        del fundo
        pygame.mixer_music.load("apalusos.mp3")
        pygame.mixer_music.play(0)
        janela.blit(vencedor, (0, 0))
        pygame.display.update()
        sleep(5)
        break
pygame.quit()
