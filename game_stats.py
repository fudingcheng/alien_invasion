"""跟踪游戏的统计信息"""


class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings

        self.reset_stats()

        self.game_active = False


    """初始化在游戏运行期间可能变化的信息"""

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
