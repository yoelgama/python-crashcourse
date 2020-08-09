import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Inicializa a espaçonave e define a posição inicial"""
        super(Ship, self).__init__()

        self.screen = screen

        self.speed_factor = ai_settings.ship_speed_factor

        # carrega a imagem da espaçonave e obtém seu retangulo de medidas
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # flags de movimento
        self.moveright = False
        self.moveleft = False

        # armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Desenha a espaçonave na tela"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        # atualiza o valor do centro da espaçonave e não do retangulo
        if self.moveright and self.rect.right < self.screen_rect.right:
            self.center += self.speed_factor
        if self.moveleft and self.rect.left > 0:
            self.center -= self.speed_factor

        self.center_ship()

    def center_ship(self):
        self.rect.centerx = self.center
