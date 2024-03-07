import sys
import pygame
import random

pygame.init()

# Configuração da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CORES = [BRANCO, VERMELHO, AZUL]

tamanho_bolinha = 150
bolinha = pygame.Rect(largura / 2 - tamanho_bolinha / 2, altura / 2 - tamanho_bolinha / 2, tamanho_bolinha, tamanho_bolinha)

clock = pygame.time.Clock()

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)

while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)

COR_ALEATORIA = random.randint(0, len(CORES) - 1)  # Inicializa COR_ALEATORIA fora do loop principal

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bolinha.x += velocidade_x
    bolinha.y += velocidade_y

    if bolinha.right >= largura or bolinha.left <= 0:
        velocidade_x = -velocidade_x
        COR_ALEATORIA = random.randint(0, len(CORES) - 1)

    if bolinha.bottom >= altura or bolinha.top <= 0:
        velocidade_y = -velocidade_y
        COR_ALEATORIA = random.randint(0, len(CORES) - 1)

    clock.tick(320)
    tela.fill(PRETO)
    pygame.draw.ellipse(tela, CORES[COR_ALEATORIA], bolinha)
    pygame.display.flip()
