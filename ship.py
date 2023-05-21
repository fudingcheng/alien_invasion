import pygame
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


"""飞船类"""
class Ship:
    def __init__(self, ai_game):
        # 初始化游戏窗口对象
        self.screen = ai_game.screen
        # 获得游戏窗口的矩形
        self.screen_rect = self.screen.get_rect()

        # 加载飞船图像
        self.image = pygame.image.load("./images/ship.bmp")
        # 获得飞船图片的矩形
        self.rect = self.image.get_rect()

        # 对于每艘飞船，都将其放置在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 设置左移动和右移动的标志
        self.move_left = False
        self.move_rigth = False

        # 导入设置类
        self.settings = ai_game.settings

        # 存储飞船的位置
        self.x = float(self.rect.x)
        

    """在指定位置绘制飞船"""

    def blime(self):
        # 在屏幕上绘制飞船图片
        self.screen.blit(self.image, self.rect)

    """根据移动标志，控制飞船的左移和右移"""

    def update_position(self):
        # 更新飞船的位置
        if self.move_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed
        if self.move_rigth and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # 移动飞船的位置
        self.rect.x = self.x

        # logging.info(f"飞船当前的位置是:{self.x}")
