import pygame.font
from pygame.sprite import Group

from ship import Ship
class Scoreboard:
    """得分信息板"""
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats

        # 显示得分信息使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始化得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_ship()

    def prep_score(self):
        """文字转成image，rect调整位置"""
        rouded_score = round(self.stats.score, -1)
        score_str = f"{rouded_score:,}"
        self.score_image = self.font.render(score_str, True,
                                    self.text_color, self.settings.bg_color)
        # 调整rect位置
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20

    def prep_high_score(self):
        """文字转成image，rect调整位置"""
        high_rouded_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_rouded_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                                            self.text_color,
                                            self.settings.bg_color)
        # 调整rect位置
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_ship(self):
        """ 显示剩下船加入编组"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship.rect.width * ship_number
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """画图方法"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """检查是否产生最高分"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.stats._cover_old_high_score(self.stats.high_score)
