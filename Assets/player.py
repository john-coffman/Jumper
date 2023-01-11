import pygame

sprite = pygame.image.load('Assets/sprite.png')

class player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(sprite, (32, 32)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        #movement of player
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.jump_speed = -4
        self.gravity = .08
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1 
        else:
            self.direction.x = 0 
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_speed
            
    def update(self):
        self.player_input()
