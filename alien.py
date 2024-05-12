import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人类"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # 加载图片和设置rec属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 最初位置在屏幕左上角
        self.rect.x = self.image.get_width()
        self.rect.y = self.image.get_height()

        # 存储精确位置
        self.x = float(self.rect.x)

    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """如果边缘就返回True"""
        screen_rect = self.screen.get_rect()
        return ((self.rect.right >= screen_rect.right)
                or (self.rect.left <= screen_rect.left))

