import pygame

amarelo = (255, 255, 0)
verde = (0, 255, 0)
preto = (0, 0, 0)
pygame.init()

tela = pygame.display.set_mode((640, 480), 0)

raio = 30
velocidade = 0.1
x = 10
vel_x = velocidade
y = 10
vel_y = velocidade

while True:
    # Calcula as regras
    x += vel_x
    y += vel_y
    if x + raio > 640:
        vel_x = -velocidade
    if x - raio < 0:
        vel_x = velocidade
    if y + raio > 480:
        vel_y = -velocidade
    if y - raio < 0:
        vel_y = velocidade

    # Pintar a tela
    tela.fill(preto)
    pygame.draw.circle(tela, verde, (int(x), int(y)), raio, 0)
    pygame.display.update()

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
