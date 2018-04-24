"""
作者：刘琪
时间：18-4-18
题目：myplane
"""
import pygame
# 创建一个我方飞机类
class HeroPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("./images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("./images/me2.png").convert_alpha()
        #self.image1 = plane_image
        self.rect = self.image1.get_rect()
        self.rect.left,self.rect.top = ((bg_size.width-self.rect.width)/2+100, \
                                        bg_size.height-self.rect.height-50)
        self.destroy_images=[]
        self.destroy_images.extend([ \
            pygame.image.load("./images/me_destroy_1.png").convert_alpha(),\
            pygame.image.load("./images/me_destroy_2.png").convert_alpha(),\
            pygame.image.load("./images/me_destroy_3.png").convert_alpha(), \
            pygame.image.load("./images/me_destroy_4.png").convert_alpha()])
        # 状态
        self.alive = True

        # 速度
        self.speed = 4

        # 背景大小
        self.bg_size = bg_size

        # 获取非透明区域
        self.mask = pygame.mask.from_surface(self.image1)

    # 上下活动范围
    def move_up(self):
        if self.rect.top < 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def move_down(self):
        if self.rect.bottom > self.bg_size.height-50:
            self.rect.bottom = self.bg_size.height - 50
        else:
            self.rect.bottom += self.speed

    # 左右活动范围
    def move_left(self):
        if self.rect.left <0:
            self.rect.left = 0

        else:
            self.rect.left -= self.speed

    def move_right(self):
        if self.rect.right > self.bg_size.width:
            self.rect.right = self.bg_size.width
        else:
            self.rect.right += self.speed

    def reset(self,bg_size):
        self.alive = True
        self.rect.left, self.rect.top = ((bg_size[0]- self.rect.width) / 2+100, \
                                         bg_size[1] - self.rect.height - 50)