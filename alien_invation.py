import sys
import pygame
from settings import Settings
from ship import Ship

"""管理游戏资源和行为的类"""


class AlienInvasion:

    """初始化方法"""

    def __init__(self):

        # 初始化pygame
        pygame.init()

        # 创建设置类对象
        self.settings = Settings()

        # 设置游戏窗口的宽和高
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height),pygame.RESIZABLE)

        # 设置游戏窗口为全屏显示
        #self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)  
        # 更新setting的宽和高
        #self.settings.screen_width = self.screen.get_width()
        #self.settings.screen_height = self.screen.get_height()


        # 创建飞船类
        self.ship = Ship(self)

        # 游戏窗口的标题
        pygame.display.set_caption("Alien Invasion")

        # 设置游戏的背景色
        self.bg_color = self.settings.bg_color

    """开始游戏的主循环"""

    def run_game(self):

        while True:

            # 监视键盘和鼠标事件
            self._check_events()    # 调用实例方法中，python会隐示的传递self对象，不需要显示传递

            # 控制飞船的移动
            self.ship.update_position()

            # 绘制屏幕
            self._update_screen()   # 调用实例方法中，python会隐示的传递self对象，不需要显示传递

    """检测用户键盘或鼠标事件"""
    """
         1. 定义实例方法时，以单下划线命名的目的是，该方法是内部方法， 不提供外部的调用
         2. 定义实例方法时，需要显示的指定self形参，不论内部是否使用，在定义实例方法时都要给self形参数
    """

    def _check_events(self):
        for event in pygame.event.get():
            #  如果用户点击关闭按钮，则退出程序
            if event.type == pygame.QUIT:
                sys.exit()
            # 监听键盘按下的方向键，控制飞船的左右移动
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 监听键盘弹起的方向键
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # 监听窗口大小变化
            elif event.type == pygame.VIDEORESIZE:
                self.settings.screen_width = self.screen.get_width()
                self.settings.screen_height = self.screen.get_height()

                # 更新飞船的位置
                self.ship.rect.midbottom = self.screen.get_rect().midbottom



    """响应键盘松开事件"""
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_rigth = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False

    """响应键盘按下事件"""
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:  # 检测到右键
            self.ship.move_rigth = True
                    
        elif event.key == pygame.K_LEFT:  # 检测到左键
            self.ship.move_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        

    """更新屏幕绘制"""
    """
         1. 定义实例方法时，以单下划线命名的目的是，该方法是内部方法， 不提供外部的调用
         2. 定义实例方法时，需要显示的指定self形参，不论内部是否使用，在定义实例方法时都要给self形参数
    """

    def _update_screen(self):   # 以单下划线命名的目的是，该方法是内部方法， 不提供外部的调用
        # 设置屏幕背景色
        self.screen.fill(self.bg_color)
        # 绘制飞船
        self.ship.blime()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


# 把当前类作为主程序来启动
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
