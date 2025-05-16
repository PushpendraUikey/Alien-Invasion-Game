import sys
## to exit the game when the player quits
import pygame
## Pygame module contains the functionality we need to make a game.
from settings import Settings
## Importing the Settings class from settings.py to use the settings defined there.
from ship import Ship



class AlienInvasion:
    """ Overall class to manage game assets and behavior """
    def __init__(self):
        """ Initialize the game and create game resources. """
        pygame.init()
        self.settings = Settings() # Create an instance of the Settings class

        self.screen = pygame.display.set_mode( (self.settings.screen_width, self.settings.screen_height) ) # this method creates a display window of given size
        # and returns a surface object representing the screen: drawable area
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)


    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            # allow th continuous movement of the ship
            self.ship.update()
            # Redraw the screen during each pass through the code
            self._update_screen()
    
    def _check_events(self):
        """ Respond to keypresses and mouse events."""
        for event in pygame.event.get(): # returns a list of events that have occured since the last time this method was called
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """ Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color) # since every new frame overwrites the old one.
        self.ship.blitme()  # Draw the ship in the current surface.
        # Make the most recently drawn screen visible (Doesn't remember previous frames).
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
