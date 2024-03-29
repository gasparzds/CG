import pygame
import sys
from mecMovimento import MovendoTexto

class Game: 
    def __init__(self):
        pygame.init()
        self.largura = 800
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("BATE-BATE")
        self.clock = pygame.time.Clock()
        self.MovendoTexto = MovendoTexto("PAULO", 50, self.largura, self.altura)

    def run(self):
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            self.MovendoTexto.move()
            self.tela.fill((0,0,0))  
            self.tela.blit(self.MovendoTexto.texto_surf,
                           self.MovendoTexto.rect)
            pygame.display.flip()      
            self.clock.tick(350)

        pygame.quit()
        sys.exit()