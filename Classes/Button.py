import pygame
from Assets.settings import *

class Button(pygame.sprite.Sprite):

  def __init__(self, pos, title):
    super().__init__()
    self.image = pygame.Surface((50, 50))
    self.image.fill("red")
    self.rect = self.image.get_rect(center = pos)
    self.title = title

  def click(self):
    mx, my = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()
    if self.rect.collidepoint(mx, my) and clicked == (True, False, False):
      return self.title