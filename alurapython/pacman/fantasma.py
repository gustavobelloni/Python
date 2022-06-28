from elementojogo import ElementoJogo
import random
import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

fonte = pygame.font.SysFont("arial", 20, True, False)

amarelo = (255, 255, 0)
verde = (0, 255, 0)
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
branco = (255, 255, 255)
laranja = (255, 140, 0)
rosa = (255, 15, 192)
ciano = (0, 255, 255)

velocidade = 1

acima = 1
abaixo = 2
direita = 3
esquerda = 4


class Fantasma(ElementoJogo):
    def __init__(self, cor, tamanho):
        self.coluna = 13.0
        self.linha = 15.0
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.velocidade = 1
        self.direcao = abaixo
        self.cor = cor
        self.tamanho = tamanho

    def pintar(self, tela):
        fatia = self.tamanho // 8

        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)

        contorno = [(px, py + self.tamanho),
                    (px + fatia, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py + self.tamanho)
                    ]
        pygame.draw.polygon(tela, self.cor, contorno, 0)

        olho_raio_ext = fatia
        olho_raio_int = fatia // 2

        olho_esquerdo_x = int(px + fatia * 2.5)
        olho_esquerdo_y = int(py + fatia * 2.5)

        olho_direito_x = int(px + fatia * 5.5)
        olho_direito_y = int(py + fatia * 2.5)

        pygame.draw.circle(tela, branco, (olho_esquerdo_x, olho_esquerdo_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, preto, (olho_esquerdo_x, olho_esquerdo_y), olho_raio_int, 0)
        pygame.draw.circle(tela, branco, (olho_direito_x, olho_direito_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, preto, (olho_direito_x, olho_direito_y), olho_raio_int, 0)

    def calcular_regras(self):
        if self.direcao == acima:
            self.linha_intencao -= self.velocidade
        elif self.direcao == abaixo:
            self.linha_intencao += self.velocidade
        elif self.direcao == esquerda:
            self.coluna_intencao -= self.velocidade
        elif self.direcao == direita:
            self.coluna_intencao += self.velocidade

    def mudar_direcao(self, direcoes):
        self.direcao = random.choice(direcoes)

    def esquina(self, direcoes):
        self.mudar_direcao(direcoes)

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudar_direcao(direcoes)

    def processar_eventos(self, evts):
        pass
