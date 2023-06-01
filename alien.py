import pygame
from pygame.sprite import Sprite

"""外星人类"""
class Alien(Sprite):

    def __init__(self,ai_game):

        super().__init__()
        self.screen = ai_game.screen

        self.settings = ai_game.settings


        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都定位到屏幕的左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    """更新setting的位置"""
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    """检测外星人是否碰到边缘"""
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right or self.rect.left <=0:
            return True
