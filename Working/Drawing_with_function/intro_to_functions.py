import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
def draw_cloud(x, y) :
    arcade.draw_circle_filled(x + 50, y, 40, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x, y + 50, 53, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x, y - 15, 35, arcade.color.WHITE_SMOKE)
    arcade.draw_circle_filled(x - 55, y, 40, arcade.color.WHITE_SMOKE)

def draw_hill():
    arcade.draw_circle_filled(25, 100, 200, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(125, 100, 150, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(300, 50, 100, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(410, 00, 100, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(800, 100, 200, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(700, 100, 150, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(550, 50, 100, arcade.color.DARK_SPRING_GREEN)
    arcade.draw_circle_filled(450, 00, 100, arcade.color.DARK_SPRING_GREEN)

def draw_tree(x, y) :
    # draw trunk
    arcade.draw_rectangle_filled(x + 27, y - 50, 20, 80, arcade.color.DARK_BROWN)
    # draw hole in trunk
    arcade.draw_circle_filled(x + 27.5, y - 55, 6, arcade.color.BLACK_BEAN)
    # draw leaves
    arcade.draw_circle_filled(x + 47, y - 10, 30, arcade.color.APPLE_GREEN)
    arcade.draw_circle_filled(x + 7, y - 10, 30, arcade.color.APPLE_GREEN)
    arcade.draw_circle_filled(x + 27, y + 20, 40, arcade.color.APPLE_GREEN)
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

    draw_cloud(500, 300)
    draw_cloud(300, 350)
    draw_cloud(650, 450)
    draw_cloud(200, 500)
    draw_hill()
    draw_tree(400, 150)

    # Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()