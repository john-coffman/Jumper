import pygame

from Assets.settings import * 
from Assets.player import player
from Assets.platforms import platforms

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

platform = platforms((WIDTH/2,HEIGHT-100), 50)
all_platforms = pygame.sprite.Group()
all_platforms.add(platform)

player = player((WIDTH/2,HEIGHT - 150), all_platforms)
player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(player)

def run():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return False 
                    
    screen.fill('white')
    if len(all_platforms) < 10:
      p_x = randint(0, WIDTH)
      p_y = randint(0, HEIGHT - 200, )
      platform = platforms((p_x, p_y), 50)
      all_platforms.add(platform)
    
    player_sprite.update()
    player_sprite.draw(screen)
    all_platforms.update()
    all_platforms.draw(screen)
    
    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__":
  run()
