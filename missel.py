import pygame
from pygame.sprite import Sprite

class Missel(Sprite):
    def __init__(self, ia_game):
        super().__init__()
        self.screen = ia_game.screen
        self.settings = ia_game.settings
        self.color = self.settings.color_missel

        self.rect = pygame.Rect(0, 0, self.settings.largura_missel, self.settings.altura_missel)

        self.rect.midtop = ia_game.nave.rect.midtop
 
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.velocidade_missel
        self.rect.y = self.y

    def gerar_missel(self):
        pygame.draw.rect(self.screen, self.color, self.rect)