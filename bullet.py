import pygame
from pygame.sprite import Sprite

"""管理飞船发射的子弹类"""
class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color


        # 在(0,0)处创建一个表示子弹的矩形,再设置正确的位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
        
    """定义更新子弹位置的方法"""
    def update(self):

        self.y -= self.settings.bullet_speed

        self.rect.y = self.y 

    """在屏幕上绘制子弹"""
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)