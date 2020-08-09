import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


# ########### Stats area ######################
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ship_hit: faz as ações necessárias para quando a espaçoonave é atingida"""
    if stats.ships_left - 1 > 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship.rect.height, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.reset_stats()
        stats.game_active = False


def check_high_score(stats, sb):
    """check_high_score: """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


# ########### Bullet area ####################
def check_bullet_collision(bullets, ai_settings, screen, stats, sb, ship, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.aliens_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship.rect.height, aliens)
        ai_settings.increase_speed()


def update_bullets(bullets, ai_settings, screen, stats, sb, ship, aliens):
    # atualiza a posição dos projéteis
    bullets.update()
    # remove projéteis fora da área do jogo
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_collision(bullets, ai_settings, screen, stats, sb, ship, aliens)


def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# #################### Alien Area #################
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Verifica se algum alienígena alcançou a parte inferior da
    tela."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1


def get_number_aliens_x(ai_settings, alien_width):
    # calcula o espaço para cada alien
    available_space_x = ai_settings.screen_width - (alien_width * 2)
    number_aliens_x = available_space_x // (2 * alien_width)

    return number_aliens_x


def get_number_aliens_y(ai_settings, ship_height, alien_height):
    # calcula o espaço para cada alien
    available_space_y = ai_settings.screen_height - \
                        (3 * alien_height) - ship_height
    number_aliens_y = available_space_y // (2 * alien_height)

    return number_aliens_y


def create_alien(ai_settings, screen, aliens, aliens_number, alien_row):
    alien = Alien(ai_settings, screen)
    alien_width, alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * aliens_number
    alien.y = alien.rect.height + 2 * alien.rect.height * alien_row

    alien.rect.y = alien.y
    alien.rect.x = alien.x

    aliens.add(alien)


def create_fleet(ai_settings, screen, ship_height, aliens):
    """Cria uma frota de alienigenas"""
    alien = Alien(ai_settings, screen)
    alien_width, alien_height = alien.rect.size
    alien_number_x = get_number_aliens_x(ai_settings, alien_width)
    alien_number_y = get_number_aliens_y(ai_settings, ship_height, alien_height)

    for alien_row in range(alien_number_y):
        for alien_number in range(alien_number_x):
            create_alien(ai_settings, screen, aliens, alien_number, alien_row)


# ######### Screen Area #######################################
def update_screen(play_button, ai_settings, stats, sb, screen, ship, aliens, bullets):
    # redesenha a tela com a cor selecionada
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)
    sb.prep_score()
    sb.prep_level()
    sb.prep_ships()
    sb.show_score()

    if not stats.game_active:
        pygame.mouse.set_visible(True)
        play_button.draw_button()

    # Deixa a tela mais recente visível
    pygame.display.flip()


# ############### Key area #################################
def check_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        # para de mover para a direita
        ship.moveright = False
    if event.key == pygame.K_LEFT:
        # para de mover para a esquerda
        ship.moveleft = False


def check_keydown(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # move para a direita
        ship.moveright = True
    elif event.key == pygame.K_LEFT:
        # move para a esquerda
        ship.moveleft = True
    elif event.key == pygame.K_SPACE:
        # atira
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


# ########## Events area #############################
def check_play_button(ai_settings, screen, stats, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y):
    """Inicia um novo jogo quando o jogador clicar em Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        ai_settings.initialize()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship.rect.height, aliens)


def check_events(ai_settings, screen, stats, play_button, ship,
                 aliens, bullets):
    # Observa eventos de teclado e mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y)
