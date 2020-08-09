class Settings:
    """Uma classe para armazenar as configurações do jogo"""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela do jogo
        self.title = "Invasão de Aliens!"
        self.screen_width = 840
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.initialize()

    def initialize(self):
        # Configurações da espaçonave
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Configurações dos projéteis
        self.bullet_speed_factor = 3
        self.bullet_width = 8
        self.bullet_height = 20
        self.bullet_color = 255, 200, 60
        self.bullets_allowed = 3

        # Configurações do Alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 = right | -1 = left
        self.aliens_points = 50

        # velocidade inicial escalonável do jogo
        self.speedup_scale = 1.1
        self.score_scale  = 1.5

    def increase_speed(self):
        """increase_speed: """
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.aliens_points = int(self.aliens_points * self.score_scale)
