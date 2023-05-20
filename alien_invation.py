import sys
import pygame
from setting import Settings

"""管理游戏资源和行为的类"""


class AlienInvasion:

    """初始化方法"""

    def __init__(self):

        pygame.init()

        # 创建设置类对象
        self.settings = Settings()

        # 设置游戏窗口的宽和高
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 游戏窗口的标题
        pygame.display.set_caption("Alien Invasion")
        # 设置游戏的背景色
        self.bg_color = self.settings.bg_color

    """开始游戏的主循环"""

    def run_game(self):

        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                #  如果用户点击关闭按钮，则退出程序
                if event.type == pygame.QUIT:
                    sys.exit()

            # 重绘屏幕
            self.screen.fill(self.bg_color)

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
