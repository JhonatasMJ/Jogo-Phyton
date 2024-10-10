import sys
import pygame
from settings import Settings
from nave import Nave
from missel import Missel
from alien import Alien

class InvasaoAlienigena:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
  
        self.bg_image = pygame.image.load('img/fundo.jpg') 
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.largura_tela, self.settings.altura_tela))
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.largura_tela = self.screen.get_rect().width
        self.settings.altura_tela = self.screen.get_rect().height
        
        pygame.display.set_caption("Invasão Alienígena")
        self.nave = Nave(self)
        self.missel = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()
        self._criar_frota()
   
    def jogo_on(self):
        while True:
            self._checar_eventos()
            self.nave.update()
            self._atualiza_missel()
            self._atualiza_aliens()
            self._atualiza_tela()

    def _checar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        elif event.key == pygame.K_UP:
            self.nave.mover_cima = True   
        elif event.key == pygame.K_DOWN:
            self.nave.mover_baixo = True     
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._disparar_missel()        

    def _checar_soltarteclas_eventos(self, event):
        if event.key == pygame.K_RIGHT:
            self.nave.mover_direita = False
        elif event.key == pygame.K_LEFT:
            self.nave.mover_esquerda = False
        elif event.key == pygame.K_UP:
            self.nave.mover_cima = False  
        elif event.key == pygame.K_DOWN:
            self.nave.mover_baixo = False

    def _disparar_missel(self):
        if len(self.missel) < self.settings.disparos_por_vez:
            novo_missel = Missel(self)
            self.missel.add(novo_missel)    

    def _atualiza_missel(self):
        self.missel.update()
        for missel in self.missel.copy():
            if missel.rect.bottom <= 0:
                self.missel.remove(missel)  
                
    def _atualiza_aliens(self):
        self.alien.update()            

    def _criar_frota(self):
        alien = Alien(self)
        self.alien.add(alien)   
        alien_largura, alien_altura = alien.rect.size

        current_x, current_y = alien_largura, alien_altura
        while current_y < (self.settings.altura_tela - 3 * alien_altura):
            self._criar_alien(current_x,current_y)
            current_x += 2 * alien_altura 

    def _criar_alien(self, x_position, y_position):
            novo_alien = Alien(self)
            novo_alien.x = x_position
            novo_alien.rect.x = x_position
            novo_alien.rect.y = y_position
            self.alien.add(novo_alien)
                  

    def _atualiza_tela(self):    
        # Desenha a imagem de fundo
        self.screen.blit(self.bg_image, (0, 0))
        
        for missel in self.missel.sprites():
            missel.gerar_missel()
        self.nave.blitme()
        self.alien.draw(self.screen)
        # Atualiza a tela
        pygame.display.flip()
        self.clock.tick(60) 

if __name__ == '__main__':
    ia = InvasaoAlienigena()
    ia.jogo_on()
