import json
import re
from pathlib import Path


class GameStats:
    """统计游戏信息"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.score = 0
        # 任何时间都不重置最高分
        self.path = "./config/stats.json"
        self.high_score = 0
        self._load_in_stats()  # 载入的最高分

    def reset_stats(self):
        """初始化运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0

    def _load_in_stats(self):
        path = Path(self.path)
        if path.exists():
            contents = path.read_text()
            stats = json.loads(contents)
            # 正则表达式提取最高分
            match = re.search(r'=\s*(\d+)', stats)
            self.high_score = int(match.group(1))
            print(f'loaded in high score {self.high_score}')
        else:
            stats = 'high_score = 0'
            contents = json.dumps(stats)
            path.write_text(contents)

    def _cover_old_high_score(self, new_high_score):
        stats = f'high_score = {new_high_score}'
        contents = json.dumps(stats)
        path = Path(self.path)
        path.write_text(contents)
