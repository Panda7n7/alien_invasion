class Settings:
    """存储外星人游戏中的设置"""

    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3  # 最多3台飞船
        # 子弹设置
        self.bullet_speed = 2.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 30
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        # 移动方向 1 右方向， -1左方向
        self.fleet_direction = 1
