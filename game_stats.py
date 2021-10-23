class GameStats():
    """Armazena os dados estatísticos da Invasção Alienígena"""
    
    def __init__(self, ai_settings):
        """Inicializa dos dados estatístivos."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Inicializa a Invasão Alienígena como ativa
        self.game_active = False

        # A pontuação máxima jamais devera ser reiniciada
        self.high_score = 0

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0

