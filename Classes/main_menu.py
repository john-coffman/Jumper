import pygame
from Classes.Button import Button
from Data.settings import *
class main_menu():
  def __init__(self, surface):
    self.display_surface = surface
    self.buttons = []

  def create_buttons(self):
    play_button = Button((WIDTH/2, HEIGHT/2), "play button")
    options_button = Button((150, 50), "options button")
    self.buttons.append(play_button)
    self.buttons.append(options_button)
  
  def is_clicked(self):
    for button in self.buttons:
      button.click()
  
  def draw_buttons(self):
    for button in self.buttons:
      self.display_surface.blit(button.text, button.textrect)
  
  def run(self):
    self.display_surface.fill( "white")
    self.create_buttons()
    self.draw_buttons()