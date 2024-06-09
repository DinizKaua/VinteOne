import pygame
class Botao():
    def __init__(self, x, y, imagem, imagemPress, escala):
        altura_botao = imagem.get_height()
        largura_botao = imagem.get_width()
        self.imagem = imagem
        self.imagemPress = imagemPress
        self.imagem = pygame.transform.scale(imagem, (int(largura_botao * escala), int(altura_botao * escala)))
        self.imagemPress = pygame.transform.scale(imagemPress, (int(largura_botao * escala), int(altura_botao * escala)))
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.clique_botao_esquerdo = False

    def botao_na_tela(self, interface):
        # interacao com o mouse
        acao = False
        posicao_mouse = pygame.mouse.get_pos()

        # imprimir o botao
        interface.blit(self.imagem, (self.rect.x, self.rect.y))

        if self.rect.collidepoint(posicao_mouse):
            interface.blit(self.imagemPress, (self.rect.x, self.rect.y))
            if pygame.mouse.get_pressed()[0] == 1 and self.clique_botao_esquerdo == False:
                self.clique_botao_esquerdo = True
                acao = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clique_botao = False

        return acao