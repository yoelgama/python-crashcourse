import pygame.font

class Button():
    """Button: um botão para o jogo"""

    def __init__(self, ai_settings, screen, msg):
        """Inicia a Button"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Propriedades do botão
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 100)
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont("tlwgtypewriter", 38, True, True)
        self.rect  = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """draw_button: """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

