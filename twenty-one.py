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
        fps.tick(30)

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
    cartasDoJogador = []
    somaCartasJogador = 0
    cartasDoBot = []

    suaVez = True
    cartaAtual = 0

    # xCartaAnimada = 600
    # yCartaAnimada = 150

    lista_posicaoRelativaCartas = []
    posicaoRelativaCartas = 10
    cartasExibidas = []
    flag_exibirCartas = False

    flag_animacaoCarta = False
    musicaClassica()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

        tela_jogo.blit(fundo_jogo, (0, 0))
        tela_jogo.blit(redimensionarImagem(iconPlayer, 0.12), (570, 330))
        tela_jogo.blit(redimensionarImagem(iconBot, 0.12), (25, 25))
        fps.tick(30)

        # volta para o menu pelo botao esc
        if pygame.key.get_pressed()[K_ESCAPE]:
            menuPrincipal()

        # verifica se o usuario puxou uma carta
        if botao_packBaralho.botao_na_tela(tela_jogo) and suaVez:
            # aleatoriza um valor aleatório do vetor baralho
            cartaAtual = random.choice(baralho)
            #adiciona a mão do jogador a carta aleatorizada
            cartasDoJogador.append(cartaAtual)
            somaCartasJogador = sum(cartasDoJogador)
            print(somaCartasJogador)
            flag_animacaoCarta = True


            # dependendo da carta, adiciona a lista de cartas que serão exibidas na tela
            if cartaAtual == 1:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_1)), 0.2))
            elif cartaAtual == 2:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_2)), 0.2))
            elif cartaAtual == 3:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_3)), 0.2))
            elif cartaAtual == 4:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_4)), 0.2))
            elif cartaAtual == 5:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_5)), 0.2))
            elif cartaAtual == 6:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_6)), 0.2))
            elif cartaAtual == 7:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_7)), 0.2))
            elif cartaAtual == 8:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_8)), 0.2))
            elif cartaAtual == 9:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_9)), 0.2))
            elif cartaAtual == 10:
                cartasExibidas.append(redimensionarImagem((random.choice(cartas_10)), 0.2))

            # adiciona juntamente a posicao relativa da carta
            lista_posicaoRelativaCartas.append(posicaoRelativaCartas)
            posicaoRelativaCartas += 50
            flag_exibirCartas = True


        # exibir a carta na tela
        if flag_exibirCartas:
            for i, c, in enumerate(cartasExibidas):
                tela_jogo.blit(c, (lista_posicaoRelativaCartas[i], 306))


        pygame.display.flip()

def opcoes():
    ...

menuPrincipal()