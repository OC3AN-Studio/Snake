from engine import *
import random


class SnakeGame(object):

    def __init__(self):
        # snake body
        self.snake = None
        # create dictionary
        self.obj_list = {}
        self.window = WindowManager("Snake", 800, 800)
        self.window.window.bind_all('<Key>', self.get_user_input)

        # Constant fields
        self.WIDTH = 800
        self.HEIGHT = 800
        self.SPEED = 25
        self.OBJECT_WIDTH = 25

    # snake movement

    def move_snake(self, code):
        if code == 37:
            if self.snake.velocity[0] == 0:
                self.snake.velocity = [-self.SPEED, 0]
        elif code == 39:
            if self.snake.velocity[0] == 0:
                self.snake.velocity = [self.SPEED, 0]
        elif code == 38:
            if self.snake.velocity[1] == 0:
                self.snake.velocity = [0, self.SPEED]
        elif code == 40:
            if self.snake.velocity[1] == 0:
                self.snake.velocity = [0, -self.SPEED]

    def get_user_input(self, event):
        code = event.keycode
        self.move_snake(code)

    def reset(self):
        self.obj_list.clear()
        self.snake = Snake()
        self.generate_food()
        location_third = (self.WIDTH / 2 + 2 * self.OBJECT_WIDTH, self.HEIGHT / 2)
        location_second = (self.WIDTH / 2 + self.OBJECT_WIDTH, self.HEIGHT / 2)
        location_first = (self.WIDTH / 2, self.HEIGHT / 2)
        third_body = GameObj(location=location_third, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="snake")
        second_body = GameObj(location=location_second, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="snake")
        first_body = GameObj(location=location_first, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="snake")
        self.snake.insert(third_body)
        self.snake.insert(second_body)
        self.snake.insert(first_body)
        self.obj_list[location_third] = third_body
        self.obj_list[location_second] = second_body
        self.obj_list[location_first] = first_body

    def movement(self):
        # add new body to the head
        head_location = self.snake.head.location

        # compute location
        location = (head_location[0] + self.snake.velocity[0], head_location[1] + self.snake.velocity[1])
        temp_obj = self.obj_list[location]
        if isinstance(temp_obj, GameObj):
            if temp_obj.tag == "snake":
                self.reset()
        else:
            # remove snake tail
            remove_location = (self.snake.tail.game_obj.location[0], self.snake.tail.game_obj.location[1])
            self.obj_list.pop(remove_location)
            self.snake.remove()

        # create snake body for head
        snake_body = GameObj(location=location, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="snake")
        self.snake.insert(snake_body)
        self.obj_list[location] = snake_body

    # Generate food

    def generate_food(self):
        random_x = random.randint(0, self.WIDTH)
        random_y = random.randint(0, self.HEIGHT)
        food = GameObj(location=[random_x, random_y], width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="food")
        self.obj_list[(random_x, random_y)] = food

    # Main game
    def main(self):
        self.reset()
        game_over = False
        has_food = True
        while True:
            if game_over:
                self.reset()
                game_over = False

            # Check for user input

            self.movement()

            # Check if there is food, if not, then create one
            if not has_food:
                self.generate_food()
                has_food = True