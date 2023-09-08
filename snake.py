# É necessário fazer a instalação da biblioteca pygame
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#Limites da tela
largura = 640
altura = 480
x_cobra = int((largura/2)) - 20
y_cobra = int((altura/2)) - 25

#Velocidade do jogo
velocidade = 3
x_control = 3
y_control = 0

#Variáveis de áudio
barulho_moeda = pygame.mixer.Sound('./assets/smw_yoshi_tongue.wav')
barulho_final = pygame.mixer.Sound('./assets/smw_castle_clear.wav')
barulho_lula = pygame.mixer.Sound('./assets/lulinha_o.wav')
barulho_bolso = pygame.mixer.Sound('./assets/bozinho_o.wav')
barulho_over = pygame.mixer.Sound('./assets/smw_game_over.wav')
barulho_mariana_50 = pygame.mixer.Sound('./assets/mariana_50.wav')
barulho_mariana_70 = pygame.mixer.Sound('./assets/mariana_70.wav')
barulho_danilo_5 = pygame.mixer.Sound('./assets/danilo_5.wav')
barulho_danilo_30 = pygame.mixer.Sound('./assets/danilo_30.wav')

barulho_over.set_volume(1)
barulho_lula.set_volume(0.3)
barulho_bolso.set_volume(0.3)


pontos = 0
fonte = pygame.font.SysFont('txt', 20, True, False)

x_maca = randint(40, 520)
y_maca = randint(20, 320)

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('COBRINEA')

limite = 10
corpo = []

morre = False 

def cobra_cresce(corpo):
    for AeB in corpo:
        # AeB = [x, y]
        # AeB[0] = x
        # AeB[1] = y
        pygame.draw.rect(tela, (240,248,255), (AeB[0], AeB[1], 30,30))


def restart_jogo(): #função que reinicia o jogo quando a cobrinha morre ou você ganha
    global pontos, limite, x_cobra, y_cobra, corpo, cabeca, x_maca, y_maca, morre, ganhou
    pontos = 0
    limite = 10
    x_cobra = int((largura/2)) - 20
    y_cobra = int((altura/2)) - 25
    corpo = []
    cabeca = []
    x_maca = randint(40, 520)
    y_maca = randint(20, 320)
    morre = False
    ganhou = False



    


while True: #loop geral obrigatóro (que faz as coisas rodarem)
    relogio.tick(120)
    tela.fill((72,61,139))
    texto_pontos = f'Pontos: {pontos}'
    texto_format = fonte.render(texto_pontos, False, (245,245,245), None)
    texto_devs = 'Developed by Danzz0 :)'
    texto_devs_format = fonte.render(texto_devs, True, (245,245,245))
    for event in pygame.event.get(): #loop que controloa os eventos do jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
        #Comandos para a cobra andar de acordo com o teclado
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_control == -velocidade:
                    pass
                elif x_control == velocidade:
                    pass
                else:
                    x_control -= velocidade
                    y_control = 0 
            if event.key == K_RIGHT:
                if x_control == velocidade:
                    pass
                elif x_control == -velocidade:
                    pass
                else:
                    x_control += velocidade
                    y_control = 0
            if event.key == K_DOWN:
                if y_control == velocidade:
                    pass
                elif y_control == -velocidade:
                    pass
                else:
                    y_control += velocidade
                    x_control = 0
            if event.key == K_UP:
                if y_control == -velocidade:
                    pass
                elif y_control == velocidade:
                    pass
                else:
                    y_control -= velocidade
                    x_control = 0
    
    x_cobra = x_cobra + x_control 
    y_cobra = y_cobra + y_control
   
    #Criação da cobrinha e maçã
    cobrinha = pygame.draw.rect(tela, (240,248,255), (x_cobra,y_cobra,30,30))
    maca = pygame.draw.circle(tela, (255,99,71), (x_maca,y_maca), 12)

    #Faz com que a maçã respawne aleatoriamente quando a cobrinha a come
    if cobrinha.colliderect(maca):
        x_maca = randint(40, 520)
        y_maca = randint(50, 320)
        pontos += 1
        if pontos == 5:
            barulho_danilo_5.play()
        if pontos == 13:
            barulho_lula.play()
        if pontos == 22:
            barulho_bolso.play()
        if pontos == 30:
            barulho_danilo_30.play()
        if pontos == 50:
            barulho_mariana_50.play()
        if pontos == 70:
            barulho_mariana_70.play()
        if pontos == 101:
            barulho_final.play()
        barulho_moeda.play()
        limite +=6
        
    cabeca = []
    cabeca.append(x_cobra)
    cabeca.append(y_cobra)
    corpo.append(cabeca)

    contador = corpo.count(cabeca)

    #Tudo o que acontece quando a cobrinha morre
    if contador > 1 or x_cobra > largura or x_cobra < 0 or y_cobra > altura or y_cobra < 0:

        global mensagem_format2 , fonte3
        morre = True
        barulho_over.play()
        fonte2 = pygame.font.SysFont('txt', 30, True, False)
        fonte3 = pygame.font.SysFont('txt', 25, True, False)
        mensagem1 = 'GAME OVER!'
        mensagem2 = 'Pressione a tecla ESPAÇO para reiniciar'
        
        mensagem_format1 = fonte2.render(mensagem1, False, (244,255,255))
        mensagem_format2 = fonte3.render(mensagem2, True, (244,255,255))
        while morre:
            tela.fill((25,25,112))
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        restart_jogo()

            tela.blit(mensagem_format1, (int((largura/2)-75), int((altura/2)-15)) )
            tela.blit(mensagem_format2, (int((largura/2)-180), int((altura/2)+15)) )         
            pygame.display.update() 

    #Tudo que acontece quando a cobrinha ganha
    if pontos == 101:
        ganhou = True
        mensagem3 = "VOCÊ GANHOU!"
        mensagem4 = 'Pressione a tecla ESPAÇO para reiniciar'
        fonte4 = pygame.font.SysFont('txt', 30, True, False)
        fonte5 = pygame.font.SysFont('txt', 25, True, False)
        mensagem_format3 = fonte4.render(mensagem3, False, (244,255,255))
        mensagem_format4 = fonte5.render(mensagem4, True, (244,255,255))
        while ganhou:
            tela.fill((0,191,255))
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        restart_jogo()
            tela.blit(mensagem_format3, (int((largura/2)-87), int((altura/2)-15)) )
            tela.blit(mensagem_format4, (int((largura/2)-180), int((altura/2)+15)) )
            pygame.display.update()
    #Faz com que a cobra não creça infinitamente
    if len(corpo) > limite:
        del corpo[0]


    cobra_cresce(corpo)
            
    #Cria a tela do jogo
    tela.blit(texto_format, (410,10))
    tela.blit(texto_devs_format, (20, 460))
    pygame.display.update() #Comando importante que faz alterações na tela