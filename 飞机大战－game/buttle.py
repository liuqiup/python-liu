"""
作者：刘琪
时间：18-4-18
题目：buttle
"""
# 定义一个子弹类
import pygame
class Bulletmyplane(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 10
        self.alive = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < 0:
            self.alive = False
        else:
            self.rect.top -= self.speed
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.alive = True
