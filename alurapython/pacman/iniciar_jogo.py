from cenario import Cenario
from pacman import Pacman
from fantasma import Fantasma
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

verde = (0, 255, 0)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
laranja = (255, 140, 0)
rosa = (255, 15, 192)
ciano = (0, 255, 255)



if __name__ == "__main__":
    size = 600 // 30

    pacman = Pacman(size)

    blinky = Fantasma(vermelho, size)
    inky = Fantasma(ciano, size)
    clyde = Fantasma(laranja, size)
    pinky = Fantasma(rosa, size)
    greenky = Fantasma(verde, size)

    cenario = Cenario(size, pacman)

    cenario.adicionar_movivel(pacman)
    cenario.adicionar_movivel(blinky)
    cenario.adicionar_movivel(inky)
    cenario.adicionar_movivel(clyde)
    cenario.adicionar_movivel(pinky)
    cenario.adicionar_movivel(greenky)

    while True:
        # Calcular as regras
        pacman.calcular_regras()
        blinky.calcular_regras()
        inky.calcular_regras()
        clyde.calcular_regras()
        pinky.calcular_regras()
        greenky.calcular_regras()
        cenario.calcular_regras()

        # Pintar a tela
        screen.fill(preto)

        cenario.pintar(screen)
        pacman.pintar(screen)
        blinky.pintar(screen)
        inky.pintar(screen)
        clyde.pintar(screen)
        pinky.pintar(screen)
        greenky.pintar(screen)

        pygame.display.update()
        pygame.time.delay(75)

        # Captura de eventos
        eventos = pygame.event.get()

        cenario.processar_eventos(eventos)
        pacman.processar_eventos(eventos)
