import pygame

from game.utils.constants import COLITION


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.player_bullets = []

    def update (self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                game.death_count += 1
                game.lives += 1
                game.substract_lives()
                pygame.time.delay(1000)
                self.enemy_bullets.remove(bullet)
                if game.lives < 1:
                    game.playing = False
                break

            if len (game.enemy_manager.enemies) > 0:
                if bullet.rect.colliderect(game.enemy_manager.enemies[0].rect) and bullet.owner == 'player':
                    EXPLOSION_SONIDO.play()
                    game.score += 100
                    game.score_total += 100
                    self.explosion(game,game.enemy_manager.enemies[0])
                    game.enemy_manager.enemies = []

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

    def colition(self, game, rival):
        x = rival.rect.x + (rival.rect.width - COLITION.get_width()) // 2
        y = rival.rect.y + (rival.rect.height - COLITION.get_height()) // 2

        image_colition = COLITION

        pygame.display.flip()

    def draw (self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len (self.enemy_bullets)<1:
            self.enemy_bullets.append(bullet)
        if bullet.owner == 'player' and len (self.player_bullets)<1:
            self.enemy_bullets.append(bullet)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []