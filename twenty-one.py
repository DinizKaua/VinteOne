import time
import pygame
from pygame.locals import *
from sys import exit
from botao import Botao
import random
from biblioteca import*

pygame.init()

# instancias
botao_jogar = Botao(280, 220, jogar, jogarPress, 0.05)
botao_opcoes = Botao(280, 300, opcoes, opcoesPress, 0.05)
botao_sair = Botao(280, 380, sair, sairPress, 0.05)
botao_packBaralho = Botao(580, 150, pack, packPress, 0.2)

# telas
pygame.display.set_icon(icone)
def menuPrincipal():
    musicaDoidona()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

        tela_jogo.blit(fundo_menu, (0, 0))
        fps.tick(40)

        # verifica se o usuario clicou em jogo
        if botao_jogar.botao_na_tela(tela_jogo):
            Jogo()

        # verificou se o usuario clicou em opcoes
        if botao_opcoes.botao_na_tela(tela_jogo):
            print('opcoes')

        # verificou se o usuario clicou em sair
        if botao_sair.botao_na_tela(tela_jogo):
            pygame.quit()
            exit()

        pygame.display.flip()


def Jogo():

    # variaveis do jogo
    flag_mostrarCarta = False
    xCartaAnimada = 600
    yCartaAnimada = 150
    flag = True
    pos = [50, 160]
    cartasExibidas = [redimensionarImagem(copas_3, 0.2), redimensionarImagem(espada_8, 0.2)]
    musicaClassica()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

        tela_jogo.blit(fundo_jogo, (0, 0))
        fps.tick(40)

        # volta para o menu pelo botao esc
        if pygame.key.get_pressed()[K_ESCAPE]:
            menuPrincipal()

        # verifica se o usuario puxou uma carta
        if botao_packBaralho.botao_na_tela(tela_jogo):
             flag_mostrarCarta = True

        for i, c, in enumerate(cartasExibidas):
            tela_jogo.blit(c, (pos[i], 306))

        # exibir a carta na tela
        '''
        if flag_mostrarCarta:
            tela_jogo.blit(redimensionarImagem(paus_3, 0.2), (xCartaAnimada, yCartaAnimada))
            if flag:
                xCartaAnimada -= 50
                yCartaAnimada += 13
            if xCartaAnimada == 50:
                flag = False
                '''

        pygame.display.flip()

def opcoes():
    ...

menuPrincipal()