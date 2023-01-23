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

        
    def create_platforms(self):
        if len(self.all_platforms) < 10:
            p_w = randint(40, 60)
            p_x = randint(0, WIDTH - p_w)
            p_y = self.init_platform.rect.y - randint(80, 120)
            self.init_platform = platforms((p_x, p_y), p_w)
            self.all_platforms.add(self.init_platform)
           
    def collision_x(self):
        player = self.player_sprite.sprite
        player.rect.x += player.direction.x * player.speed
                    
    def collision_y(self):
        player = self.player_sprite.sprite
        player.apply_gravity()
        for sprite in self.all_platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.jump() 
                                    
    def run(self):
        self.display_surface.fill('white')
        # level
        self.create_platforms()
        self.all_platforms.draw(self.display_surface)
        # player
        self.player_sprite.update()
        self.collision_y()
        self.collision_x()
        self.player_sprite.draw(self.display_surface)