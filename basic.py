# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to Arcade"
RADIUS = 150


class Kumusta(arcade.Window):
    """Main welcome window
    """
    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background window
        arcade.set_background_color(arcade.color.BLACK)
    
    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawi9ng
        arcade.start_render()

        # Draw some rectangles
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 200, 100, arcade.color.WHITE)
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.75, 150, 75, arcade.color.GRAY)

# Main code entry point
if __name__ == "__main__":
    app = Kumusta()
    arcade.run()