import pygame
from pygame.locals import *
from random import *

class myPlan(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self, moveSpeed):
        '''
        if self.rect.left <= 0 or self.rect.right >= self.width:
            moveSpeed = (0,0)
        if self.rect.top <= 0 or self.rect.bottom >= self.height:
            moveSpeed = (0,0)
        '''
        self.rect = self.rect.move(moveSpeed)
        return self.rect

class myBullet(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self, moveSpeed):
        '''
        if self.rect.left <= 0 or self.rect.right >= self.width:
            moveSpeed = (0,0)
        if self.rect.top <= 0 or self.rect.bottom >= self.height:
            moveSpeed = (0,0)
        '''
        self.rect = self.rect.move(moveSpeed)
        return self.rect

