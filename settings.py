
"""存储游戏的设置类"""
class Settings:

    """初始化游戏设置"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1

        # 子弹设置
        self.bullet_speed  = 1.0
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allow = 3

        # 外星人移动的速度
        self.alien_speed = 1.0
        # 外星人向下的速度
        self.fleet_drop_speed = 10
        # 外星人方向 1:右； -1:左边
        self.fleet_direction = 1