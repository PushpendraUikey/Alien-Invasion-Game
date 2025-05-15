import pygame
""" Pygame treats each element of the game as a surface. It is easy to work with their 
    coordinates then
    """
class Ship:
    """ A class to manage the ship. """
    
    def __init__(self, ai_game):
        """ Initialize the ship and set its initial position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() # get_rect() returns a rect object representing the screen.

        # load the ship image and get its rect.
        # self.image = pygame.image.load('images/ship.bmp') #returns the surface representing the image
        original_image = pygame.image.load('images/ship.bmp')
        width, height = original_image.get_size()
        scaled_size = (int(width * 0.17), int(height * 0.17))
        self.image = pygame.transform.scale(original_image, scaled_size) # scale the img to 17% of original to work with

        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)