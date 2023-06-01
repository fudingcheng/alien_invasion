"""跟踪游戏的统计信息"""
class GameStats:

    def __init__(self,ai_game):
        self.settings = ai_game.settings

        self.reset_stats()

    