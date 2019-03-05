import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
def draw_cloud() :
    arcade.draw_circle_filled(590, 400, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(540, 450, 53, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(540, 385, 35, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(485,400, 40, arcade.color.WHITE_SMOKE)

def draw_hill ():
    arcade.draw_circle_filled(25, 100, 200, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(125, 100, 150, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(300, 50, 100, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(410, 00, 100, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(800, 100, 200, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(700, 100, 150, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(550, 50, 100, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(450, 00, 100, arcade.color.DARK_SPRING_GREEN)

def draw_tree ():
    # draw trunk
    arcade.draw_rectangle_filled(427, 100, 20, 80, arcade.color.DARK_BROWN)
    # draw hole in trunk
    arcade.draw_circle_filled(427.5, 95, 6, arcade.color.BLACK_BEAN)
    # draw leaves
    arcade.draw_circle_filled(447, 140, 30, arcade.color.APPLE_GREEN)
    arcade.draw_circle_filled(407, 140, 30, arcade.color.APPLE_GREEN)
    arcade.draw_circle_filled(427, 170, 40, arcade.color.APPLE_GREEN)
    # draw apples :
    arcade.draw_circle_filled(410, 150, 5, arcade.color.BRICK_RED)
    arcade.draw_circle_filled(440, 150, 5, arcade.color.BRICK_RED)
    arcade.draw_circle_filled(450, 175, 5, arcade.color.BRICK_RED)
    arcade.draw_circle_filled(400, 180, 5, arcade.color.BRICK_RED)
    arcade.draw_circle_filled(405, 120, 5, arcade.color.BRICK_RED)
    arcade.draw_circle_filled(455, 125, 5, arcade.color.BRICK_RED)
    arcade.draw_circle_filled(427, 190, 5, arcade.color.BRICK_RED)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions

    draw_cloud()
    draw_hill()
    draw_tree()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()