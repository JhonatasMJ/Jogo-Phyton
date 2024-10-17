import pygame
 
from pygame.sprite import Sprite
 
class Alien(Sprite):
 
    def __init__(self, ia_game):
        super().__init__()
        self.screen = ia_game.screen
        self.screen_rect = ia_game.screen.get_rect()
        self.settings = ia_game.settings
        self.image = pygame.image.load("img/et.png")
        self.rect = self.image.get_rect()
 
        self.rect.top = self.screen_rect.top
 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.direction = 1
 
    def update(self):
        self.x += self.settings.velocidade_alien * self.direction
        self.rect.x = self.x  
        if self.rect.right >= self.screen.get_rect().right or self.rect.left <= 0:
            self.direction *= -1
 
    def top_alien(self):
        self.rect.top = self.screen_rect.top
        self.y = float(self.rect.y)
   
    def blitme(self):
        """
        Coloca a nave na localização atual
        """
        self.screen.blit(self.imagem, self.rect)