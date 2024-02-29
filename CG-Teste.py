import sys
import pygame
import random

pygame.init()

#Configuração da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Pygame")



PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO =(255,0,0) 
AZUL =(0,0,255)
CORES = [ BRANCO, VERMELHO, AZUL]

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("PAULO", True, BRANCO)
#

texto_rect = texto.get_rect(center=(largura/2, altura/2))
clock = pygame.time.Clock()

velocidade_x = random.randint(-1,1)
velocidade_y = random.randint(-1,1)

while velocidade_x ==0:
    velocidade_x = random.randint(-1,1)

while velocidade_y ==0:
    velocidade_y = random.randint(-1,1)

#Loop printicpal 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    texto_rect.x += velocidade_x 
    texto_rect.y += velocidade_y 



    if texto_rect.right >= largura or texto_rect.left <= 0:
        velocidade_x = random.randint(-1,1)
        velocidade_y = random.randint(-1,1)
        COR_ALEATORIA = random.randint(0, len(CORES) - 1)
        texto = fonte.render("PAULO", True, CORES[COR_ALEATORIA])
        

    if texto_rect.bottom >= altura or texto_rect.top <= 0:
        velocidade_x = random.randint(-1,1)
        velocidade_y = random.randint(-1,1)
        COR_ALEATORIA = random.randint(0, len(CORES) - 1)
        texto = fonte.render("PAULO", True, CORES[COR_ALEATORIA])


    clock.tick(320)
    tela.fill(PRETO)
    tela.blit(texto,texto_rect)
    pygame.display.flip()
                
            
