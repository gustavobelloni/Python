import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
pontos = 10
texto = f'Score: {pontos}'

fonte = pygame.font.SysFont('arial', 48, True, False)
imagem_texto = fonte.render(texto, True, (0, 255, 0))

while True:
    screen.blit(imagem_texto, (100,100))
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()