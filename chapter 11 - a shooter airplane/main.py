import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import Game_stats
from settings import Settings
from ship import Ship
from scoreboard import ScoreBoard

def run_game():
    # inicializa o jogo e cria um objeto para a tela
    pygame.init()

    ai_settings = Settings()

    # tela do jogo
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.title)

    # Botão play
    play_button = Button(ai_settings, screen, "Play!")

    # estatísticas iniciais
    stats = Game_stats(ai_settings)

    sb = ScoreBoard(ai_settings, screen, stats)

    # espaçonave
    ship = Ship(ai_settings, screen)

    # grupo de projéteis
    bullets = Group()

    # grupo de aliens
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship.rect.height, aliens)

    # Inicia o laço principal do jogo
    while True:
        # Observa eventos de teclado e mouse
        gf.check_events(ai_settings, screen, stats, play_button,
                        ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, ai_settings, screen, stats, sb, ship, aliens)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(play_button, ai_settings, stats, sb, screen, ship, aliens, bullets)


run_game()
