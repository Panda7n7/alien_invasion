import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船发的子弹类"""

    def __init__(self, ai_game):
        """在飞船位置创建子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # (0,0)创建子弹矩形，设置位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width
                                , self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储位置浮点数
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新准确位置
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """屏幕显示图形"""
        pygame.draw.rect(self.screen, self.color, self.rect)



