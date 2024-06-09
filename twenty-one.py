import pygame
from pygame.locals import *
from sys import exit
from botao import Botao

pygame.init()
# carregando arquivos

# imagem das cartas
backface_cards = pygame.image.load('cards/BackFace/CardBackFaceBlueSmallPattern.png')
backface_cards = pygame.transform.scale(backface_cards, (80, 113))

#imagem dos botoes
jogar = pygame.image.load('images/jogar.png')
jogarPress = pygame.image.load('images/jogarPress.png')
opcoes = pygame.image.load('images/opcoes.png')
opcoesPress = pygame.image.load('images/opcoesPress.png')
sair = pygame.image.load('images/sair.png')
sairPress = pygame.image.load('images/sairPress.png')

#imagem gerais
fundo_menu = pygame.image.load('images/menu.png')
icone = pygame.image.load('images/icon.png')
pygame.display.set_icon(icone)

fundo_jogo = pygame.image.load('images/tela_jogo.png')

# musicas
def musicaClassica():
    pygame.mixer.music.load('sounds/music_classic.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

def musicaDoidona():
    pygame.mixer.music.load('sounds/musica_doidona.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

# variáveis e interface geral
altura_tela = 480
largura_tela = 720

tela_jogo = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Vinte One')
fps = pygame.time.Clock()

# instancias
botao_jogar = Botao(280, 220, jogar, jogarPress, 0.05)
botao_opcoes = Botao(280, 300, opcoes, opcoesPress, 0.05)
botao_sair = Botao(280, 380, sair, sairPress, 0.045)

# variáveis do jogo


# telas
def menuPrincipal():
    musicaDoidona()
    while True:
        fps.tick(60)
        tela_jogo.blit(fundo_menu, (0, 0))

        if botao_jogar.botao_na_tela(tela_jogo):
            Jogo()
        botao_opcoes.botao_na_tela(tela_jogo)
        if botao_sair.botao_na_tela(tela_jogo):
            pygame.quit()
            exit()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()

def Jogo():
    musicaClassica()
    while True:
        tela_jogo.blit(fundo_jogo, (0, 0))
        tela_jogo.blit(backface_cards, (600, 20))
        tela_jogo.blit(backface_cards, (610, 20))
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

        if pygame.key.get_pressed()[K_ESCAPE]:
            menuPrincipal()

        pygame.display.flip()

def opcoes():
    ...

menuPrincipal()