class GameStats:
    """统计游戏信息"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit

