import sys
## to exit the game when the player quits
import pygame
## Pygame module contains the functionality we need to make a game.




class AlienInvasion:
    """ Overall class to manage game assets and behavior """
    def __init__(self):
        """ Initialize the game and create game resources. """
        pygame.init()

        self.screen = pygame.display.set_mode( (1200, 800) ) # this method creates a display window of given size
        # and returns a surface object representing the screen: drawable area
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230) # pygame uses RGB color model

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color) # since every new frame overwrites the old one.
            # Make the most recently drawn screen visible (Doesn't remember previous frames).
            pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
