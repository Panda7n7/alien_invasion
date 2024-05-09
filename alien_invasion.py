import sys
from settings import Settings
from ship import Ship
import pygame


class AlienInvasion:
    def __init__(self):
        """ 初始化和创建资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ 开始主循环"""
        while True:
            # 监听用户键鼠操作
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """相应按下"""
        print(event.key)
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _update_screen(self):
        """更新屏幕操作"""
        # 屏幕填充颜色
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # 最近绘制可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例运行
    ai = AlienInvasion()
    ai.run_game()
