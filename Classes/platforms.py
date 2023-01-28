import pygame
from Data.settings import HEIGHT
ground = pygame.image.load("Assets/ground.png")

class platforms(pygame.sprite.Sprite):
    def __init__(self, pos, width):
        super().__init__()
        self.image = pygame.transform.scale(ground, (width, 10)).convert()
        self.rect = self.image.get_rect(center = pos) 
        
        
    def update(self, scroll):
        self.rect.y += scroll
        if self.rect.top > HEIGHT:
            self.kill()