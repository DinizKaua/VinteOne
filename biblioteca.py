import pygame
import random

pygame.init()
# imagem das cartas
verso_daCarta = pygame.image.load('images/cards/backface_card.png')
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
comeca = pygame.image.load('images/comecar.png')
comecaPress = pygame.image.load('images/comecarPress.png')
parar = pygame.image.load('images/parar.png')
pararPress = pygame.image.load('images/pararPress.png')
jogarNovamente = pygame.image.load('images/jogarNovamente.png')
jogarNovamentePress = pygame.image.load('images/jogarNovamentePress.png')

#imagem gerais
fundo_menu = pygame.image.load('images/menu.png')
icone = pygame.image.load('images/icon.png')
pygame.display.set_icon(icone)
barrio = pygame.image.load('images/barrio.png')
hellokitty = pygame.image.load('images/hellokitty.png')

fundo_jogo = pygame.image.load('images/tela_jogo.png')
iconPlayer = pygame.image.load('images/imagem_heroi.png')
iconBot = pygame.image.load('images/imagem_vilao.png')

# musicas e efeitos sonoros

musica_Jogo = pygame.mixer.Sound('sounds/music_classic.mp3')
musica_Menu = pygame.mixer.Sound('sounds/old_citytheme.ogg')
som1 = pygame.mixer.Sound('sounds/soundEffect/cardSlide1.wav')
som2 = pygame.mixer.Sound('sounds/soundEffect/cardSlide2.wav')
som3 = pygame.mixer.Sound('sounds/soundEffect/cardSlide3.wav')
som4 = pygame.mixer.Sound('sounds/soundEffect/cardSlide4.wav')
som5 = pygame.mixer.Sound('sounds/soundEffect/cardSlide5.wav')
som6 = pygame.mixer.Sound('sounds/soundEffect/cardTakeOutPackage1.wav')

# fonte
fonte = pygame.font.Font('chawp.ttf', 40)

# contantes de interface e geral
altura_tela = 480
largura_tela = 720

tela_jogo = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Vinte One')
fps = pygame.time.Clock()

baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cartas_1 = [paus_1, copas_1, ouro_1, espada_1]
cartas_2 = [paus_2, copas_2, ouro_2, espada_2]
cartas_3 = [paus_3, copas_3, ouro_3, espada_3]
cartas_4 = [paus_4, copas_4, ouro_4, espada_4]
cartas_5 = [paus_5, copas_5, ouro_5, espada_5]
cartas_6 = [paus_6, copas_6, ouro_6, espada_6]
cartas_7 = [paus_7, copas_7, ouro_7, espada_7]
cartas_8 = [paus_8, copas_8, ouro_8, espada_8]
cartas_9 = [paus_9, copas_9, ouro_9, espada_9]
cartas_10 = [paus_10, copas_10, ouro_10, espada_10, paus_j, copas_j, ouro_j, espada_j, paus_q, copas_q, ouro_q, espada_q, paus_k, copas_k, ouro_k, espada_k]

# funções
def redimensionarImagem(imagem, escala):
    altura = imagem.get_height()
    largura = imagem.get_width()
    imagem = pygame.transform.scale(imagem, (int(largura*escala), int(altura*escala)))
    return imagem

# dependendo do valor ela retorna uma carta com o nipe aleatorio daquele valor
def selecionaNipe(cartaAtual):
    if cartaAtual == 1:
        return redimensionarImagem((random.choice(cartas_1)), 0.2)
    elif cartaAtual == 2:
        return redimensionarImagem((random.choice(cartas_2)), 0.2)
    elif cartaAtual == 3:
        return redimensionarImagem((random.choice(cartas_3)), 0.2)
    elif cartaAtual == 4:
        return redimensionarImagem((random.choice(cartas_4)), 0.2)
    elif cartaAtual == 5:
        return redimensionarImagem((random.choice(cartas_5)), 0.2)
    elif cartaAtual == 6:
        return redimensionarImagem((random.choice(cartas_6)), 0.2)
    elif cartaAtual == 7:
        return redimensionarImagem((random.choice(cartas_7)), 0.2)
    elif cartaAtual == 8:
        return redimensionarImagem((random.choice(cartas_8)), 0.2)
    elif cartaAtual == 9:
        return redimensionarImagem((random.choice(cartas_9)), 0.2)
    elif cartaAtual == 10:
        return redimensionarImagem((random.choice(cartas_10)), 0.2)


def probabilidado_botPuxarCarta(somaDasCartas):
    if somaDasCartas <= 11:
        return True
    else:
        probabilidade = random.randint(0, 100)
        if somaDasCartas <= 15:
            return probabilidade <= 60
        elif somaDasCartas <= 18:
            return probabilidade <= 40
        elif somaDasCartas < 21:
            return probabilidade <= 15
        elif somaDasCartas >= 21:
            return False

def verificaVencedor(point_Player, point_Bot):
    if point_Player == point_Bot:
        return ' HOUVE UM EMPATE!'
    elif point_Player > point_Bot and point_Player <= 21:
        return 'VOCÊ VENCEU!'
    elif point_Player < point_Bot and point_Bot > 21:
        return 'VOCÊ VENCEU!'
    else:
        return 'VOCÊ PERDEU...(melhore)'