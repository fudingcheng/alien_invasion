import sys
import pygame
from settings import Settings
from ship import Ship
import logging
from bullet import Bullet
from alien import Alien


"""管理游戏资源和行为的类"""


class AlienInvasion:

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


    """初始化方法"""

    def __init__(self):

        # 初始化pygame
        pygame.init()

        # 创建设置类对象
        self.settings = Settings()

        # 设置游戏窗口的宽和高
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.screen_rect = self.screen.get_rect()

        # 设置游戏窗口为全屏显示
        #self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)  
        # 更新setting的宽和高
        #self.settings.screen_width = self.screen.get_width()
        #self.settings.screen_height = self.screen.get_height()


        # 创建飞船类
        self.ship = Ship(self)

        # 定义存储多个子弹的编组
        self.bullets = pygame.sprite.Group()

        # 定义存储多个外星人的编组
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


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
            self.ship.move_position()

            # 更新屏幕的子弹
            self._update_bullets()

            # 更新外星人的坐标
            self._update_aliens()
            
            # 绘制屏幕
            self._update_screen() 

    """移除子弹"""
    def _update_bullets(self):
        # 通过子弹编组调用子弹的位置更新方法
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)  # 调用实例方法中，python会隐示的传递self对象，不需要显示传递
        # print(len(self.bullets))
        # 检测当子弹和外星人碰撞时，删除子弹和外星人
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
    
        # 如果外星人被消灭完毕，则重新创建一批外星人
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

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
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    """创建一颗子弹,并将其加入编组bullets中"""
    def _fire_bullet(self):
        if(len(self.bullets) < self.settings.bullet_allow):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
       
        

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

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 绘制外星人
        self.aliens.draw(self.screen)

        # 刷新窗口
        pygame.display.flip()

    # 创建外星人群
    def _create_fleet(self):
        alien = Alien(self)
        # 一个外星人的宽度
        alien_width = alien.rect.width
        # 计算屏幕一行可用的距离
        avaliable_space_x = self.settings.screen_width-(2 * alien_width)
        # 计算一行可以容纳多少个外星人
        number_aliens_x = avaliable_space_x // (2*alien_width)

        # 计算可以容纳多少行
        avaliable_space_y = self.settings.screen_height - 3 * alien.rect.height - self.ship.rect.height

        number_rows = avaliable_space_y // (2 * alien.rect.height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)

    """在屏幕上添加外星人"""
    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y  = alien_height + 2 * alien_height * row_number
        # 设置外星人的x\y坐标
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        # 将外星人添加到编组中
        self.aliens.add(alien)

    """更新外星人"""
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # 判断外星人是否碰撞上飞船
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("Ship hit!!!")

    """检测外星人是否碰到屏幕边缘，如果碰到边缘的话就改变方向"""
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    """改变外星人移动方向"""
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y +=self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



# 把当前类作为主程序来启动
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
