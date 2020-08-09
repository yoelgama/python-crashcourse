class Game_stats():
    """Game_stats: Armazena as estatísticas do jogo"""

    def __init__(self, ai_settings):
        """Inicia a Game_stats"""
        self.ai_settings = ai_settings
        self.game_active = False

        self.level = 1
        self.score = 0
        self.high_score = 0

        self.reset_stats()

    def reset_stats(self):
        """Inicializa os dados do jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0
