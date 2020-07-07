import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Invader"
SCALING = 2.0

class Invader(arcade.Window):
  """Space Shooter side scroller game
  Player starts on the left, enemies appear on the right
  Player can move anywhere, but not off screen
  Enemies fly to the left at variable speed
  Collisions end the game
  """

  def __init__(self, width: int, height: int, title: int):
    """Initialize the game
    """
    super().__init__(width, height, title)

    # Set up empty sprite lists
    self.enemies_list = arcade.SpriteList()
    self.clouds_list = arcade.SpriteList()
    self.all_sprites = arcade.SpriteList()
  
  def setup(self):
    """Get the game ready to play
    """

    # Set the background color
    arcade.set_background_color(arcade.color.WHITE)

    # Set up the player
    self.player = arcade.Sprite("images/jet.png", SCALING)
    self.player.center_y = self.height / 2
    self.player.left = 10
    self.all_sprites.append(self.player)

    # Spawn new enemey every .25 seconds
    arcade.schedule(self.add_enemy, 0.25)
    
    # Spawn new cloud every second
    #arcade.schedule(self.add_cloud, 1.0)
  
  def add_enemy(self, delta_time: float):
    """Adds a new enemy to the screen

    Arguments:
      delta_time {float} -- How much time has passed since last call
    """

    # Create enemy sprite
    enemy = arcade.Sprite("images/missile.png", SCALING)

    # Set random position and off screen right
    enemy.left = random.randint(self.width, self.width + 80)
    enemy.top = random.randint(10, self.height - 10)

  def on_draw(self):
    """Draw all game objects
    """

    arcade.start_render()
    self.all_sprites.draw()
  
if __name__ == "__main__":
  invader_game = Invader(
    int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
  )

  invader_game.setup()

  arcade.run()