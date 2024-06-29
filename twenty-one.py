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

    somaCartasJogador = 0
    cartaAtual = 0

    xCartaAnimada = 600
    yCartaAnimada = 150
    posicaoRelativaAnimacao = 50

    lista_posicaoRelativaCartas = []
    posicaoRelativaCartas = 10
    cartasExibidas = []

    # flags base
    flag_exibirCartas = False
    flag_animacaoCarta = False
    suaVez = True
    musica_MenuPrincipal.play(-1)
    musica_MenuPrincipal.set_volume(0.15)
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

        tela_jogo.blit(fundo_jogo, (0, 0))
        tela_jogo.blit(redimensionarImagem(iconPlayer, 0.06), (580, 350))
        tela_jogo.blit(redimensionarImagem(iconBot, 0.06), (25, 25))
        fps.tick(30)

        # volta para o menu pelo botao esc
        if pygame.key.get_pressed()[K_ESCAPE]:
            musica_MenuPrincipal.stop()
            menuPrincipal()


        # verifica se o usuario puxou uma carta
        if botao_packBaralho.botao_na_tela(tela_jogo) and suaVez:
            # som de puxar a carta
            somPuxarCarta = random.choice([som1, som2, som3, som4, som5])
            somPuxarCarta.play()

            # aleatoriza um valor aleatório do vetor baralho
            cartaAtual = random.choice(baralho)

            #adiciona a mão do jogador a carta aleatorizada
            cartasDoJogador.append(cartaAtual)
            somaCartasJogador = sum(cartasDoJogador)
            print(somaCartasJogador)

            # convertendo o valor na imagem da carta
            cartaNova = selecionaNipe(cartaAtual)

            #ativando a animação de puxar carta
            flag_animacaoCarta = True


        # animação da carta puxando
        if flag_animacaoCarta:
            tela_jogo.blit(cartaNova, (xCartaAnimada, yCartaAnimada))
            xCartaAnimada -= 100
            yCartaAnimada += 30
            if xCartaAnimada <= posicaoRelativaAnimacao:
                # adiciona a nova carta ao deck exibido e a posicao relativa
                cartasExibidas.append(cartaNova)
                lista_posicaoRelativaCartas.append(posicaoRelativaCartas)
                posicaoRelativaCartas += 50

                # reseta e atualiza as configurações da animação
                xCartaAnimada = 600
                yCartaAnimada = 150
                posicaoRelativaAnimacao += 50

                flag_exibirCartas = True
                flag_animacaoCarta = False

        # exibir a carta na tela
        if flag_exibirCartas:
            for i, c, in enumerate(cartasExibidas):
                tela_jogo.blit(c, (lista_posicaoRelativaCartas[i], 306))

        # textos
        if somaCartasJogador == 21:
            point_playerFormatado = fonte.render(str(somaCartasJogador), True, (218, 165, 32))
        elif somaCartasJogador > 21:
            point_playerFormatado = fonte.render(str(somaCartasJogador), True, (255, 000, 000))
        else:
            point_playerFormatado = fonte.render(str(somaCartasJogador), True, (255, 255, 255))

        tela_jogo.blit(point_playerFormatado, (10, altura_tela//2))

        pygame.display.flip()

def opcoes():
    ...

menuPrincipal()