import pygame

from Assets.settings import * 
from Assets.World import World
from Assets.main_menu import main_menu
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

level = World(screen)
main_menu = main_menu(screen)

def main_screen():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return False 
    if main_menu.is_clicked() == "play_button":
      run()
    main_menu.run()

    pygame.display.update()
    clock.tick(60)

def run():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return False 
                    
    level.run()
    
    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__":
  main_screen()
  #run()
 
 