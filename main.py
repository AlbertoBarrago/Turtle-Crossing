import random
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player('turtle')
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

def main():
    while game_is_on:
        time.sleep(0.1)
        if random.randint(1, 6) == 1:
            car_manager.generate_new_car()

        car_manager.move_car()

        if player.ycor() >= 270:
            scoreboard.update_score()
            player.level_up()

        screen.update()

if __name__ == '__main__':
    main()