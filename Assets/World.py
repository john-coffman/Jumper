import pygame
from Assets.platforms import platforms
from Assets.settings import *
from Assets.player import player

class World:
    def __init__(self, surface):
        #screen
        self.display_surface = surface
        #player
        self.player = player((WIDTH/2, HEIGHT-150))
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player_sprite.add(self.player)
        #platforms
        self.init_platform = platforms((WIDTH/2, HEIGHT-100), 50)
        self.all_platforms = pygame.sprite.Group()
        self.all_platforms.add(self.init_platform)
        self.create_platforms(self.init_platform)

    def create_platforms(self, platform):
        if len(self.all_platforms) < 10:
           print(platform.rect.y)
           p_w = randint(40, 60)
           p_x = randint(0, WIDTH - p_w)
           p_y = platform.rect.y - randint(80, 120)
           platform = platforms((p_x, p_y), 50)
           self.all_platforms.add(platform)
           
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
        # player
        self.player_sprite.update()
        self.collision_x()
        self.collision_y()
        self.player_sprite.draw(self.display_surface)
