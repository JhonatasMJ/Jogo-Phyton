import pygame
 
class Nave:
    def __init__(self, ia_game):
        """Inicializa a nava e define sua posição inicial"""
        self.screen = ia_game.screen
        self.screen_rect = ia_game.screen.get_rect()
        self.settings = ia_game.settings #pega as configurações
 
        self.imagem = pygame.image.load('img/nave.png')
        self.rect = self.imagem.get_rect()
 
        self.rect.midbottom = self.screen_rect.midbottom
 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
 
        self.mover_direita = False
        self.mover_esquerda = False
        self.mover_cima = False
        self.mover_baixo = False
 
 
    def update(self):
        if self.mover_direita and self.rect.right < self.screen_rect.right:
            self.x += self.settings.velocidade_nave
 
        if self.mover_esquerda and self.rect.left > 0:
            self.x -= self.settings.velocidade_nave
            
        if self.mover_cima and self.rect.top > 0:
            self.y -= self.settings.velocidade_nave
 
        if self.mover_baixo and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.velocidade_nave
 
        self.rect.y = self.y
        self.rect.x = self.x
 
    def center_nave(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
 
    def blitme(self):
        """
        Coloca a nave na localização atual
        """
        self.screen.blit(self.imagem, self.rect)