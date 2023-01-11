import pygame
from Assets.platforms import platforms
from Assets.settings import tile_size
from Assets.player import player

class World:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.platforms = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    platform = platforms((x, y), tile_size)
                    self.platforms.add(platform)
                if cell == 'P':
                    player_sprite = player((x,y))
                    self.player.add(player_sprite)
                    
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
