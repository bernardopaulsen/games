import os
from treelib import Node, Tree


class Snake:
    DIRECTIONS = {
        0: {'x':0, 'y': 1},
        1: {'x': -1, 'y':  0},
        2: {'x':  0, 'y': -1},
        3: {'x':  1, 'y':  0}
        }

    def __init__(self,
        size):
        self.positions = [(0,i) for i in range(size)]

    def get_changes(self, direction : int) -> tuple:
        return self.DIRECTIONS[direction]['x'], self.DIRECTIONS[direction]['y']

    def move(self, snake : list, direction : int) -> list:
        x, y = self.get_changes(direction)
        snake.append((snake[-1][0] + x, snake[-1][1] + y))
        snake = snake[1:]
        return snake

    @staticmethod
    def check_crash(snake : list) -> bool:
        if snake[-1] in snake:
            return True
        else:
            return False

    @staticmethod
    def check_outside(snake: list, x_size : int, y_size : int) -> bool:
        if snake[-1][0] < 0 or snake[-1][1] < 0 or snake[-1][0] >= x_size or snake[-1][1] >= y_size:
            return True
        else:
            return False 

class Table:
    def __init__(self,
        snake_size : int = 10,
        x_size     : int = 20,
        y_size     : int = 20):

        self.snake  = Snake(snake_size)
        self.x_size = x_size
        self.y_size = y_size
        self.food   = (int(self.x_size/2),int(self.y_size/2))


    def create_environment(self):
        envir = [[' ' for _ in range(self.x_size)] for _ in range(self.y_size)]
        envir[self.food[1]][self.food[0]] = 'X'
        for part in self.snake.positions:
            envir[part[1]][part[0]] = 'o'
        return envir

    def print(self):
        envir = self.create_environment()
        string = """"""
        for y in envir:
            for x in y:
                string += x
            string += '\n'
        os.system('clear')
        print(string)

class Game:
    def __init__(self,
        snake_size : int = 10,
        x_size     : int = 20,
        y_size     : int = 20):

        self.table = Table(snake_size, x_size, y_size)

    def get_paths(self):
        tree = Tree()
        tree.create_node("Root","root")
        e = 0
        for i in range(3):
            tree.create_node(i,str(e) + str(i),parent="root",data=self.table.snake)
        for name, node in tree.nodes.items():
            print(name)
            snake = self.table.snake.move(self.table.snake,node.tag)
            print(snake)




a = Game()
a.get_paths()