import pygame
from Assets.Button import Button

class main_menu():
  def __init__(self, surface):
    self.display_surface = surface
    self.buttons = []
    self.all_button_sprites = pygame.sprite.Group()
    
  def create_buttons(self):
    play_button = Button((50, 50), "play_button")
    options_button = Button((150, 50), "options_button")
    self.all_button_sprites.add(play_button)
    self.all_button_sprites.add(options_button)
    self.buttons.append(play_button)
    self.buttons.append(options_button)
  
  def is_clicked(self):
    for button in self.buttons:
      return button.click()
     
      
  def run(self):
    self.display_surface.fill( "white")
    self.create_buttons()
    self.all_button_sprites.draw(self.display_surface)