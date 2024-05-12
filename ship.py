import pygame


class Ship:
    """管理飞船类"""
    def __init__(self, ai_game):
        """初始化飞船设置起始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 加载飞船图像获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 加载到窗口底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        print(self.rect.x)
        # 移动标记
        self.move_right = False
        self.move_left = False
        # 浮点型rect用于中间变量
        self.x = float(self.rect.x)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    def update(self):
        """根据标记调整位置"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # 更新实际rect
        self.rect.x = self.x

    def blitme(self):
        """指定位置画飞船"""
        self.screen.blit(self.image, self.rect)
