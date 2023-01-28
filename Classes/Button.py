import pygame
from Data.settings import *

class Button():
  def __init__(self, pos, title):   
    # font 
    self.title = title
    self.text = pygame.font.SysFont(None, 48).render(self.title, True, "red", "white" )
    self.textrect = self.text.get_rect(center = pos)

  def click(self):
    mx, my = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()
    if self.textrect.collidepoint(mx, my) and clicked == (True, False, False):
      return self.title