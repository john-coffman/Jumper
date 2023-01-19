import pygame
sprite = pygame.image.load('Assets/sprite.png')

class player(pygame.sprite.Sprite):
    def __init__(self, pos, platforms_sprites):
        super().__init__()
        self.image = pygame.transform.scale(sprite, (32, 32)).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.platform_sprites = platforms_sprites
        #movement of player
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.jump_speed = -10
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
        
    def collision_y(self):
        self.apply_gravity()
        for sprite in self.platform_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.jump()
                elif self.direction.y < 0:
                    self.rect.y = sprite.rect.bottom
                    self.direction.y = -self.direction.y
                    
    def collision_x(self):
        self.rect.x += self.direction.x * self.speed
        for sprite in self.platform_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                elif self.direction.x > 0:
                    self.rect.right = sprite.rect.left
    
    def update(self):
        self.player_input()
        self.collision_y()
        self.collision_x()
        
