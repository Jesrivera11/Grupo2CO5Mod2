import pygame
import os

# Global Constants
TITLE = "Batman Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Other/Logo.png"))

MILLENIUM = pygame.image.load(os.path.join(IMG_DIR, 'Spaceship/MilleniumFalcon.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

ALLIANCE_TYPE = pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart.png'))

OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, 'Other/Explosion.png'))

WALLPAPER = pygame.image.load(os.path.join(IMG_DIR, 'Other/Wallpaper.png'))

BULLETS = pygame.image.load(os.path.join(IMG_DIR, 'Other/Bullets.png'))

DEFAULT_TYPE = "default"
MILLENIUM_TYPE = 'millenium falcon'
ALLIANCE_TYPE = 'alliance'
BULLETS_TYPE = 'burst'
YWING_TYPE = 'y wing'
BOMB_TYPE = 'bomb'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/Xwing.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/MilleniumFalcon.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'SW.ttf'
FONT_STYLE1 = 'SW.ttf'

