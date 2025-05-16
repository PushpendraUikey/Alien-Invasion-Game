import pygame
""" Pygame treats each element of the game as a surface. It is easy to work with their 
    coordinates then
    """
class Ship:
    """ A class to manage the ship. """
    
    def __init__(self, ai_game):
        """ Initialize the ship and set its initial position. """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
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

        # store a decimal value for the ship's horizontal postion.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's position based on the movement flag."""
        # update the ship's x value, not the rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x  # done after typecasting to int

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)