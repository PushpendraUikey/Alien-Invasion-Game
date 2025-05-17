import pygame
# Sprite is used to group related elements in a game and manage them as a single entity.
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """ Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # create a bullet rect at (0, 0) and set correct position.
        # pygame.Rect() creates a rect object, given x, y, width and height.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y) # store the bullet's position as a decimal value.