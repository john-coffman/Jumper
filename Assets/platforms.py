import pygame

ground = pygame.image.load("Assets/ground.png")

class platforms(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(ground, (size, size)).convert()
        self.rect = self.image.get_rect(center = pos) 
