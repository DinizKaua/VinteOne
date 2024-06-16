import time

import pygame
from pygame.locals import *
from sys import exit
from botao import Botao
import random

pygame.init()
# carregando arquivos
# imagem das cartas
pack = pygame.image.load('images/cards/pack.png')
packPress = pygame.image.load('images/cards/pack_click.png')

paus_1 = pygame.image.load('images/cards/PNG-cards-1.3/ace_of_clubs.png')
paus_2 = pygame.image.load('images/cards/PNG-cards-1.3/2_of_clubs.png')
paus_3 = pygame.image.load('images/cards/PNG-cards-1.3/3_of_clubs.png')
paus_4 = pygame.image.load('images/cards/PNG-cards-1.3/4_of_clubs.png')
paus_5 = pygame.image.load('images/cards/PNG-cards-1.3/5_of_clubs.png')
paus_6 = pygame.image.load('images/cards/PNG-cards-1.3/6_of_clubs.png')
paus_7 = pygame.image.load('images/cards/PNG-cards-1.3/7_of_clubs.png')
paus_8 = pygame.image.load('images/cards/PNG-cards-1.3/8_of_clubs.png')
paus_9 = pygame.image.load('images/cards/PNG-cards-1.3/9_of_clubs.png')
paus_10 = pygame.image.load('images/cards/PNG-cards-1.3/10_of_clubs.png')
paus_j = pygame.image.load('images/cards/PNG-cards-1.3/jack_of_clubs2.png')
paus_q = pygame.image.load('images/cards/PNG-cards-1.3/queen_of_clubs2.png')
paus_k = pygame.image.load('images/cards/PNG-cards-1.3/king_of_clubs2.png')

ouro_1 = pygame.image.load('images/cards/PNG-cards-1.3/ace_of_diamonds.png')
ouro_2 = pygame.image.load('images/cards/PNG-cards-1.3/2_of_diamonds.png')
ouro_3 = pygame.image.load('images/cards/PNG-cards-1.3/3_of_diamonds.png')
ouro_4 = pygame.image.load('images/cards/PNG-cards-1.3/4_of_diamonds.png')
ouro_5 = pygame.image.load('images/cards/PNG-cards-1.3/5_of_diamonds.png')
ouro_6 = pygame.image.load('images/cards/PNG-cards-1.3/6_of_diamonds.png')
ouro_7 = pygame.image.load('images/cards/PNG-cards-1.3/7_of_diamonds.png')
ouro_8 = pygame.image.load('images/cards/PNG-cards-1.3/8_of_diamonds.png')
ouro_9 = pygame.image.load('images/cards/PNG-cards-1.3/9_of_diamonds.png')
ouro_10 = pygame.image.load('images/cards/PNG-cards-1.3/10_of_diamonds.png')
ouro_j = pygame.image.load('images/cards/PNG-cards-1.3/jack_of_diamonds2.png')
ouro_q = pygame.image.load('images/cards/PNG-cards-1.3/queen_of_diamonds2.png')
ouro_k = pygame.image.load('images/cards/PNG-cards-1.3/king_of_diamonds2.png')

copas_1 = pygame.image.load('images/cards/PNG-cards-1.3/ace_of_hearts.png')
copas_2 = pygame.image.load('images/cards/PNG-cards-1.3/2_of_hearts.png')
copas_3 = pygame.image.load('images/cards/PNG-cards-1.3/3_of_hearts.png')
copas_4 = pygame.image.load('images/cards/PNG-cards-1.3/4_of_hearts.png')
copas_5 = pygame.image.load('images/cards/PNG-cards-1.3/5_of_hearts.png')
copas_6 = pygame.image.load('images/cards/PNG-cards-1.3/6_of_hearts.png')
copas_7 = pygame.image.load('images/cards/PNG-cards-1.3/7_of_hearts.png')
copas_8 = pygame.image.load('images/cards/PNG-cards-1.3/8_of_hearts.png')
copas_9 = pygame.image.load('images/cards/PNG-cards-1.3/9_of_hearts.png')
copas_10 = pygame.image.load('images/cards/PNG-cards-1.3/10_of_hearts.png')
copas_j = pygame.image.load('images/cards/PNG-cards-1.3/jack_of_hearts2.png')
copas_q = pygame.image.load('images/cards/PNG-cards-1.3/queen_of_hearts2.png')
copas_k = pygame.image.load('images/cards/PNG-cards-1.3/king_of_hearts2.png')

espada_1 = pygame.image.load('images/cards/PNG-cards-1.3/ace_of_spades2.png')
espada_2 = pygame.image.load('images/cards/PNG-cards-1.3/2_of_spades.png')
espada_3 = pygame.image.load('images/cards/PNG-cards-1.3/3_of_spades.png')
espada_4 = pygame.image.load('images/cards/PNG-cards-1.3/4_of_spades.png')
espada_5 = pygame.image.load('images/cards/PNG-cards-1.3/5_of_spades.png')
espada_6 = pygame.image.load('images/cards/PNG-cards-1.3/6_of_spades.png')
espada_7 = pygame.image.load('images/cards/PNG-cards-1.3/7_of_spades.png')
espada_8 = pygame.image.load('images/cards/PNG-cards-1.3/8_of_spades.png')
espada_9 = pygame.image.load('images/cards/PNG-cards-1.3/9_of_spades.png')
espada_10 = pygame.image.load('images/cards/PNG-cards-1.3/10_of_spades.png')
espada_j = pygame.image.load('images/cards/PNG-cards-1.3/jack_of_spades2.png')
espada_q = pygame.image.load('images/cards/PNG-cards-1.3/queen_of_spades2.png')
espada_k = pygame.image.load('images/cards/PNG-cards-1.3/king_of_spades2.png')


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
botao_packBaralho = Botao(580, 150, pack, packPress, 0.2)

# funções gerais
def redimensionarImagem(imagem, escala):
    altura = imagem.get_height()
    largura = imagem.get_width()
    return pygame.transform.scale(imagem, (int(largura * escala), int(altura * escala)))

# variáveis do jogo
baralho = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

# telas

paus_2 = redimensionarImagem(paus_2, 0.2)

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
        fps.tick(60)
        tela_jogo.blit(fundo_jogo, (0, 0))

        if botao_packBaralho.botao_na_tela(tela_jogo):
            #time.sleep(2)

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