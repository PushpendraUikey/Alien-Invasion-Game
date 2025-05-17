import sys
## to exit the game when the player quits
import pygame
## Pygame module contains the functionality we need to make a game.
from settings import Settings
## Importing the Settings class from settings.py to use the settings defined there.
from ship import Ship
## Importing the Ship class to create a ship object.
from bullet import Bullet
## Importing the Bullet class to create bullet objects.


class AlienInvasion:
    """ Overall class to manage game assets and behavior """
    def __init__(self):
        """ Initialize the game and create game resources. """
        pygame.init()
        self.settings = Settings() # Create an instance of the Settings class

        # Note: The screen size is set to 0, 0 to make it fullscreen.
        # pygame.FULLSCREEN tells pygame to figure the window size that will fill the screen.
        self.screen = pygame.display.set_mode( (0, 0), pygame.FULLSCREEN ) # this method creates a display window of given size
        # and returns a surface object representing the screen: drawable area
        self.settings.screen_width = self.screen.get_rect().width # get the width of the screen
        self.settings.screen_height = self.screen.get_rect().height # get the height of the screen

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # create a group to hold the bullets


    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            # allow the continuous movement of the ship
            self.ship.update()
            # Update the position of the bullets
            self.bullets.update() # when update on a group is called, it calls update on each sprite in the group
            # Get rid of the bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            # Redraw the screen during each pass through the code
            self._update_screen()
    
    def _check_events(self):
        """ Respond to keypresses and mouse events."""
        for event in pygame.event.get(): # returns a list of events that have occured since the last time this method was called
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    """ Very important Note: make sure to keep exit using 'q' key, don't remove that part. Pygame do not 
    provide a default way to exit the game in fullscreen mode."""
    def _check_keydown_events(self, event):
        """ Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE: # quit the game when 'q' or 'esc' is pressed
            sys.exit()
        elif event.key == pygame.K_SPACE: # fire a bullet when space is pressed
            self._fire_bullet()

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group. """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """ Respond to key releases."""
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
        for bullet in self.bullets.sprites(): # .sprites() returns a list of all the bullets in the group
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
