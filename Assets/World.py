import pygame, math
import numpy as np
from Assets.platforms import platforms
from Assets.settings import tile_size, level_map
from Assets.player import player

class World:
    def __init__(self, surface):
        self.display_surface = surface

    def collision_x(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0 :
                    player.rect.right = sprite.rect.left
                    
    def collision_y(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.jump() 
                elif player.direction.y < 0 :
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = -player.direction.y
                                    
    def run(self):
        # level
        self.platforms.draw(self.display_surface)
        # player
        self.player.update()
        self.collision_x()
        self.collision_y()
        self.player.draw(self.display_surface)
