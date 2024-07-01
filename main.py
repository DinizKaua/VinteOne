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
botao_comeca = Botao(230, 20, comeca, comecaPress, 0.08)
botao_parar = Botao(560, 300, parar, pararPress, 0.05)
botao_jogarNovamente  = Botao(60, 210, jogarNovamente, jogarNovamentePress, 0.08)
jogandoNovamente = False

# telas
pygame.display.set_icon(icone)
musica_Menu.play(-1)
def menuPrincipal():
    global jogandoNovamente
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

        tela_jogo.blit(fundo_menu, (0, 0))
        fps.tick(30)

        # verifica se o usuario clicou em jogo
        if botao_jogar.botao_na_tela(tela_jogo):
            musica_Menu.stop()
            jogandoNovamente = False
            Jogo()

        # verificou se o usuario clicou em opcoes
        if botao_opcoes.botao_na_tela(tela_jogo):
            opcoes()

        # verificou se o usuario clicou em sair
        if botao_sair.botao_na_tela(tela_jogo):
            pygame.quit()
            exit()

        pygame.display.flip()

def Jogo():
    # variaveis do jogo
    cartaAtual = 0
    contador_deParada = 0
    contador_deDistribuicao = 0

    #variaveis fo jogador
    cartasDoJogador = []
    somaCartasJogador = 0

    # variaveis do bot
    cartasDoBot = []
    somaCartasBot = 0

    # variaveis auxiliares de animação
    xCartaAnimadaPlayer = 600
    yCartaAnimadaPlayer = 150
    posicaoRelativaAnimacaoPlayer = 50

    xCartaAnimadaBot = 600
    yCartaAnimadaBot = 150
    posicaoRelativaAnimacaoBot = 50

    # variaveis auxiliares para mostrar as cartas na tela
    lista_posicaoRelativaCartasPlayer = []
    posicaoRelativaCartasPlayer = 10
    cartasExibidasPlayer = []

    lista_posicaoRelativaCartasBot = []
    posicaoRelativaCartasBot = 10
    cartasExibidasBot = []

    # flags

    flag_playerParou = False
    flag_botParou = False
    flag_exibirCartasPlayer = False
    flag_animacaoCartaPlayer = False

    flag_exibirCartasBot = False
    flag_virarCartasBot = False
    flag_somVirarCarta = True
    flag_animacaoCartaBot = False
    global jogandoNovamente

    inicioDojogo = True
    vezDoBot = False
    suaVez = False

    if not jogandoNovamente:
        musica_Jogo.play(-1)
        musica_Jogo.set_volume(0.15)
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()

        # imagens e icons
        tela_jogo.blit(fundo_jogo, (0, 0))
        tela_jogo.blit(redimensionarImagem(iconPlayer, 0.06), (580, 350))
        tela_jogo.blit(redimensionarImagem(iconBot, 0.06), (580, 25))
        fps.tick(30)

        # volta para o menu pelo botao esc
        if pygame.key.get_pressed()[K_ESCAPE]:
            musica_Jogo.stop()
            musica_Menu.play()
            menuPrincipal()


        # começo do jogo
        if inicioDojogo:
            if botao_comeca.botao_na_tela(tela_jogo):
                inicioDojogo = False
                # bot começa jogando
                vezDoBot = True

        # a seguinte o algoritimo é direcionado ao jogador
        # verifica se o usuario parou
        if botao_parar.botao_na_tela(tela_jogo):
            suaVez = False
            flag_playerParou = True

        # permite que o bot continue jogando depois que o jogador parar
        if not flag_botParou and flag_playerParou:
            vezDoBot = True

        # verifica se o usuario puxou uma carta
        if botao_packBaralho.botao_na_tela(tela_jogo) and suaVez:
            # som de puxar a carta
            somPuxarCarta = random.choice([som1, som2, som3, som4, som5])
            somPuxarCarta.play()

            # aleatoriza um valor aleatório do vetor baralho
            cartaAtual = random.choice(baralho)

            # a mão do jogador a carta aleatorizada
            cartasDoJogador.append(cartaAtual)
            somaCartasJogador = sum(cartasDoJogador)

            # convertendo o valor na imagem da carta
            imagem_cartaNovaPlayer = selecionaNipe(cartaAtual)

            #ativando a animação de puxar carta
            flag_animacaoCartaPlayer = True


        # animação da carta puxando (do player)
        if flag_animacaoCartaPlayer:
            tela_jogo.blit(imagem_cartaNovaPlayer, (xCartaAnimadaPlayer, yCartaAnimadaPlayer))
            xCartaAnimadaPlayer -= 100
            yCartaAnimadaPlayer += 30
            if xCartaAnimadaPlayer <= posicaoRelativaAnimacaoPlayer:
                # adiciona a nova carta ao deck exibido e a posicao relativa
                cartasExibidasPlayer.append(imagem_cartaNovaPlayer)
                lista_posicaoRelativaCartasPlayer.append(posicaoRelativaCartasPlayer)
                posicaoRelativaCartasPlayer += 50

                # reseta e atualiza as configurações da animação
                xCartaAnimadaPlayer = 600
                yCartaAnimadaPlayer = 150
                posicaoRelativaAnimacaoPlayer += 50

                flag_exibirCartasPlayer = True
                flag_animacaoCartaPlayer = False
                if not flag_botParou:
                    vezDoBot = True

        # exibir minhas carta na tela
        if flag_exibirCartasPlayer:
            for i, c, in enumerate(cartasExibidasPlayer):
                tela_jogo.blit(c, (lista_posicaoRelativaCartasPlayer[i], 306))

        # a seguinte o algoritimo é direcionado ao bot
        # é bem semelhante ao do jogador, mas resolvi fazer separado para facilidar a manipulação de ambos
        if vezDoBot:
            if probabilidado_botPuxarCarta(somaCartasBot):
                # som de puxar a carta
                somPuxarCarta = random.choice([som1, som2, som3, som4, som5])
                somPuxarCarta.play()

                # aletoriza uma carta do baralho
                cartaAtual = random.choice(baralho)

                # adiciona a mão do bot a carta aleatorizada
                cartasDoBot.append(cartaAtual)
                somaCartasBot = sum(cartasDoBot)

                # convertendo o valor na imagem da carta
                imagem_cartaNovaBot = selecionaNipe(cartaAtual)

                # ativando a animação de puxar carta
                flag_animacaoCartaBot = True
                vezDoBot = False

            else:
                vezDoBot = False
                flag_botParou = True

        if flag_animacaoCartaBot:
            tela_jogo.blit(redimensionarImagem(verso_daCarta, 0.2), (xCartaAnimadaBot, yCartaAnimadaBot))
            xCartaAnimadaBot -= 100
            yCartaAnimadaBot -= 27

            if xCartaAnimadaBot <= posicaoRelativaAnimacaoBot:
                # adiciona a nova carta ao deck do bot exibido e a posicao relativa
                cartasExibidasBot.append(imagem_cartaNovaBot)
                lista_posicaoRelativaCartasBot.append(posicaoRelativaCartasBot)
                posicaoRelativaCartasBot += 50

                # reseta e atualiza as configurações da animação
                xCartaAnimadaBot = 600
                yCartaAnimadaBot = 150
                posicaoRelativaAnimacaoBot += 50

                flag_exibirCartasBot = True
                flag_animacaoCartaBot = False
                if not flag_playerParou:
                    suaVez = True

        # exibe as cartas viradas na tela
        if flag_exibirCartasBot == True:
            for i in lista_posicaoRelativaCartasBot:
                tela_jogo.blit(redimensionarImagem(verso_daCarta, 0.2), (i, 10))

        # vira as cartas
        if flag_virarCartasBot:
            if flag_somVirarCarta:
                som6.play()
                flag_somVirarCarta = False
            for i, c, in enumerate(cartasExibidasBot):
                tela_jogo.blit(c, (lista_posicaoRelativaCartasBot[i], 10 ))

        # verifica se os dois ja pararm e procede com o resultado
        if flag_playerParou and flag_botParou:
            flag_virarCartasBot = True

            # total do bot
            if somaCartasBot == 21:
                point_botFormatado = fonte.render(str(somaCartasBot), True, (218, 165, 32))
            elif somaCartasBot > 21:
                point_botFormatado = fonte.render(str(somaCartasBot), True, (255, 000, 000))
            else:
                point_botFormatado = fonte.render(str(somaCartasBot), True, (255, 255, 255))
            tela_jogo.blit(point_botFormatado, (20, 175))

            # resultado geral do jogo
            resultado_naTela = fonte.render(verificaVencedor(somaCartasJogador, somaCartasBot), True, (255, 255, 255))
            tela_jogo.blit(resultado_naTela, (80, 160))
            if botao_jogarNovamente.botao_na_tela(tela_jogo):
                jogandoNovamente = True
                Jogo()

        # total do jogador
        if somaCartasJogador == 21:
            point_playerFormatado = fonte.render(str(somaCartasJogador), True, (218, 165, 32))
        elif somaCartasJogador > 21:
            point_playerFormatado = fonte.render(str(somaCartasJogador), True, (255, 000, 000))
        else:
            point_playerFormatado = fonte.render(str(somaCartasJogador), True, (255, 255, 255))


        tela_jogo.blit(point_playerFormatado, (20, 260))

        pygame.display.flip()

def opcoes():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
        tela_jogo.blit(fundo_jogo, (0, 0))
        fps.tick(30)
        # volta para o menu pelo botao esc
        if pygame.key.get_pressed()[K_ESCAPE]:
            menuPrincipal()

        tela_jogo.blit(redimensionarImagem(barrio, 0.5), (100, 150))
        tela_jogo.blit(redimensionarImagem(hellokitty, 0.2), (380, 150))
        agradecimentos = fonte.render('Obrigado Monitores S2!!', True, (255, 255, 255))
        tela_jogo.blit(agradecimentos, (90, 90))
        pygame.display.flip()
menuPrincipal()