import pygame
# internal imports
from Data.settings import * 
from Classes.level import level
from Classes.main_menu import main_menu
# init settup for pygames
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# general background for the screens
bg = pygame.image.load("./Assets/background.png")
bg = pygame.transform.scale(bg, (700, 800)).convert()

# screens to draw on 
level = level(screen, bg)
main_menu = main_menu(screen, bg)

def main_screen():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return False
      
    if main_menu.is_clicked() == "play button":
      run()

    main_menu.run()

    pygame.display.update()
    clock.tick(60)

def run():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        level.reset()
        return False
    
    level.run()
    
    pygame.display.update()
    clock.tick(60)
  
if __name__ == "__main__":
  main_screen()
 
