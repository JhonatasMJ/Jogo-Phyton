import sys
import pygame
from settings import Settings
from nave import Nave
 
class InvasaoAlienigena:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.largura_tela, self.settings.altura_tela))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.largura_tela = self.screen.get_rect().width
        self.settings.altura_tela = self.screen.get_rect().height
        pygame.display.set_caption("Invasão Alienígena")
        self.nave = Nave(self)
        self.bg_color= (230,230,230)
   
    def jogo_on(self):
        while True:
            self._checar_eventos()
            self.nave.update()
            self._atualiza_tela()
 
    def _checar_eventos(self):
                for event in pygame.event.get():
                    if event.type== pygame.QUIT:
                     sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        self._checar_teclaspress_eventos(event)
                    elif event.type == pygame.KEYUP:
                        self._checar_soltarteclas_eventos(event)
 
    def _checar_teclaspress_eventos(self, event):
        if event.key == pygame.K_RIGHT:
            self.nave.mover_direita = True
        elif event.key == pygame.K_LEFT:
            self.nave.mover_esquerda = True
        elif event.key == pygame.K_q:
            sys.exit()
   
    def _checar_soltarteclas_eventos(self, event):
        if event.key == pygame.K_RIGHT:
            self.nave.mover_direita = False
        elif event.key == pygame.K_LEFT:
            self.nave.mover_esquerda = False
   
    def _atualiza_tela(self):    
                #preence tela cor de fundo
                self.screen.fill(self.settings.bg_color)
                self.nave.blitme()
                #atualiza tela
                pygame.display.flip()
                #taxa frame
                self.clock.tick(60)
   
 
 
 
       
if __name__ == '__main__':
    ia = InvasaoAlienigena()
    ia.jogo_on()