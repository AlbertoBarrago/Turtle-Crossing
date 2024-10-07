""" Class: CarManager """
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, player, scoreboard):
        self.all_cars = []
        self.speed = 1
        self.player = player
        self.scoreboard = scoreboard
        self.game_over = False

    def generate_new_car(self):
        """
        Generate new car and append to all_cars
        :return:
        """
        if not self.game_over:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-200, 200)
            new_car.goto(-300, random_y)
            self.all_cars.append(new_car)


    def move_car(self):
        """
        Move car forward
        :return:
        """
        if not self.game_over:
            for car in self.all_cars:
                car.setx(car.xcor()+ MOVE_INCREMENT)

    def handle_movements(self):
        """
        Handle movements: if player distance is < 20
        from a car the game is over
        :return:
        """
        for car in self.all_cars:
            if self.player.distance(car) < 20:
                self.game_over = True
                self.scoreboard.game_over()

    def handle_next_level(self):
        """
        Handle next level if player hits the edge of the screen
        :return:
        """
        if self.player.ycor() >= 270:
            for car in self.all_cars:
                self.speed += 1
                car.speed(self.speed)
            self.scoreboard.update_score()
            self.player.level_up()
