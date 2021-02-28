import os
import random
from snake import Snake

class Table():

    def __init__(self,
        snake_size =  3,
        x_size     = 60,
        y_size     = 45):

        self.snake_size = snake_size
        self.x_size     = x_size
        self.y_size     = y_size
        self.food       = [int(self.x_size/2),int(self.y_size/2)]
        self.snake      = Snake(snake_size)

    def change_food(self):
        while True:
            x = random.randint(0,self.x_size-1)
            y = random.randint(0,self.y_size-2)
            self.food = [x,y]
            if self.food not in self.snake.positions:
                break

    def check_distance(self,pos):
        return ((pos[0]-self.food[0])**2+(pos[1]-self.food[1])**2)**(1/2)

    def check_eaten(self):
        if self.food in self.snake.positions:
            return True
        else:
            return False

    def environment(self):
        envir = [[' ' for i in range(self.x_size)] for i in range(self.y_size)]
        envir[-(self.food[1]+1)][self.food[0]] = 'X'
        for part in self.snake.positions:
            envir[-(part[1]+1)][part[0]] = 'o'
        return envir

    def print(self, time : float):
        os.system('clear')
        envir = self.environment()
        for y in envir:
            for x in  y:
                print(x,end='')
            print()
        print(f'{time/60:.0f}:{time%60:.0f}')
