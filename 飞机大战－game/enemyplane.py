"""
作者：刘琪
时间：18-4-18
题目：
"""
import pygame
from random import *
# 创建一个我方飞机类
class SmallPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("./images/enemy1.png").convert_alpha()
        #　创建飞机动态图的列表
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("./images/enemy1_down1.png"),\
            pygame.image.load("./images/enemy1_down2.png"),\
            pygame.image.load("./images/enemy1_down3.png"),\
            pygame.image.load("./images/enemy1_down4.png"),\
        ])
        self.rect = self.image1.get_rect()

        # 背景的宽度, 高度
        self.width,self.height = bg_size.width,bg_size.height

        # 速度
        self.speed = 3

        # 设置敌机坐标
        self.rect.left,self.rect.top = randint(0, self.width-self.rect.width),\
                                        randint(-3*self.height, 0)

        # 状态
        self.alive = True
        # 获取非透明区域
        self.mask = pygame.mask.from_surface(self.image1)

        # 背景大小
        #self.bg_size = bg_size

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.alive = True
        self.rect.left,self.rect.top = randint(0,self.width - self.rect.width),\
                                        randint(-3*self.height,0)


class MidPlane(pygame.sprite.Sprite):
    energy = 10
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("./images/enemy2.png").convert_alpha()
        #　创建飞机子弹动态图的列表
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("./images/enemy2_down1.png"),\
            pygame.image.load("./images/enemy2_down2.png"),\
            pygame.image.load("./images/enemy2_down3.png"),\
            pygame.image.load("./images/enemy2_down4.png"),\
        ])
        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size.width,bg_size.height
        self.speed = 2

        # 设置敌机坐标
        self.rect.left,self.rect.top = randint(0, self.width-self.rect.width),\
                                        randint(-10*self.height, 0)
        # 实例能量
        self.energy = MidPlane.energy

        # 状态
        self.alive = True
        # 获取非透明区域
        self.mask = pygame.mask.from_surface(self.image1)

        # 背景大小
        #self.bg_size = bg_size

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.alive = True
        self.rect.left,self.rect.top = randint(0,self.width - self.rect.width),\
                                        randint(-10*self.height,0)
        self.energy = MidPlane.energy

class BigPlane(pygame.sprite.Sprite):
    energy = 20
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("./images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("./images/enemy3_n2.png").convert_alpha()
        #　创建飞机动态图的列表
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("./images/enemy3_down1.png"),\
            pygame.image.load("./images/enemy3_down2.png"),\
            pygame.image.load("./images/enemy3_down3.png"),\
            pygame.image.load("./images/enemy3_down4.png"),\
            pygame.image.load("./images/enemy3_down5.png"),\
            pygame.image.load("./images/enemy3_down6.png"),\
            ])
        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size.width,bg_size.height
        self.speed = 1

        # 设置敌机坐标
        self.rect.left,self.rect.top = randint(0, self.width-self.rect.width),\
                                        randint(-15*self.height, 0)
        # 实例能量
        self.energy = BigPlane.energy
        # 状态
        self.alive = True
        # 获取非透明区域
        self.mask = pygame.mask.from_surface(self.image1)

        # 背景大小
        #self.bg_size = bg_size

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.alive = True
        self.rect.left,self.rect.top = randint(0,self.width - self.rect.width),\
                                        randint(-15*self.height,0)
        self.energy = BigPlane.energy
