import pygame, math
from Assets.platforms import platforms
from Assets.settings import *
from Assets.player import player

class World:
    def __init__(self, surface):
        self.display_surface = surface
        self.player = player((WIDTH/2, HEIGHT-150))
        self.init_platform = platforms((WIDTH/2, HEIGHT-100), 50)
        self.setup(self.player, self.init_platform)
        
    def setup(self, player, platform):
        self.all_platforms = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player_sprite.add(player)
        self.all_platforms.add(platform)

    def create_platforms(self):
        if len(self.all_platforms) < 10:
           p_x = randint(0, WIDTH)
           p_y = randint(0, HEIGHT - 200)
           new_platform = platforms((p_x, p_y), 50)
           self.all_platforms.add(new_platform)
           
    def collision_x(self):
        player = self.player_sprite.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.all_platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0 :
                    player.rect.right = sprite.rect.left
                    
    def collision_y(self):
        player = self.player_sprite.sprite
        player.apply_gravity()
        for sprite in self.all_platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.jump() 
                elif player.direction.y < 0 :
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = -player.direction.y
                                    
    def run(self):
        self.display_surface.fill('white')
        # level
        self.all_platforms.draw(self.display_surface)
        self.create_platforms()
        # player
        self.player_sprite.update()
        self.collision_x()
        self.collision_y()
        self.player_sprite.draw(self.display_surface)
