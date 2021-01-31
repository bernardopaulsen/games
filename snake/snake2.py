import os
import random
import time
 

class Snake():

    DIRECTIONS = {0: {'x':0, 'y': 1},
        1: {'x': -1, 'y':  0},
        2: {'x':  0, 'y': -1},
        3: {'x':  1, 'y':  0}}

    def __init__(self,
        size = 3):

        self.positions = [[i,0] for i in range(size)]

    def check_crash(self, directions: list, x_size: int, y_size: int) -> bool:
        crash     = False
        new_pos   = self.new_positions(directions)
        len_snake = len(self.positions)
        for i in range(len(new_pos)):
            snake = self.positions[i+1:]
            snake.extend(new_pos[i-len_snake:i+1])
            crash = self.check_repeated(snake)
            if not crash:
                crash = self.check_outside(snake,x_size,y_size)
            if crash:
                break
        return crash

    def check_food(self, directions: list, food: list) -> bool:
        new_pos   = self.new_positions(directions)
        if food in new_pos:
            return True
        else:
            return False

    def get_directions(self, direction: int) -> int:
        return self.DIRECTIONS[direction]['x'], self.DIRECTIONS[direction]['y']
    
    def grow(self):
        snake = [self.positions[0]]
        snake.extend(self.positions)
        self.positions = snake

    def move(self, direction: int):
        size = len(self.positions)
        x, y = self.get_directions(direction)
        for i in range(size):
            if i < size - 1:
                self.positions[i] = self.positions[i+1]
            else:
                pos = self.positions[i]
                self.positions[i] = [pos[0] + x, pos[1] + y]

    def new_positions(self, directions: list) -> list:
        pos = [self.positions[-1]]
        for d in directions:
            x, y = self.get_directions(d)
            pos.append([pos[-1][0]+x,pos[-1][1]+y])
        return pos[1:]

    @staticmethod
    def check_outside(snake,x_size,y_size):
        outside = False
        for part in snake:
            x, y = part[0], part[1]
            if x < 0 or y < 0 or x >= x_size or y >= y_size:
                outside = True
            if outside:
                break
        return outside

    @staticmethod
    def check_repeated(snake):
        repeated = False
        for e in range(len(snake)):
            if snake[e] in snake[e+1:] or snake[e] in snake[:e]:
                repeated = True
            if repeated:
                break
        return repeated


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

class Game():

    def __init__(self,
        n_paths    = 10,
        n_steps    = 10,
        snake_size = 10,
        time_sleep = .2):

        self.table      = Table(snake_size)
        self.n_paths    = n_paths
        self.n_steps    = n_steps
        self.snake_size = snake_size
        self.time_sleep = time_sleep
        self.start      = time.time()

    def get_directions(self):
        loops = 1
        while loops <= 500:
            loops     += 1
            directions = [random.randint(0,3) for _ in range(self.n_steps)]
            if not self.table.snake.check_crash(directions,self.table.x_size,self.table.y_size):
                break
        assert loops < 500, 'Infinite loop.'
        return directions

    def get_distances(self, directions):
        new_pos = self.table.snake.new_positions(directions)
        distance = 100000.
        for p in new_pos:
            dis = self.table.check_distance(p)
            if dis < distance:
                distance = dis
        return distance

    def simulate(self):
        self.table.print(time.time()-self.start)
        while True:
            directions = [self.get_directions() for _ in range(self.n_paths)]
            l          = [self.get_distances(d) for d in directions]
            index      = l.index(min(l))
            final      = directions[index]
            time.sleep(self.time_sleep)
            self.table.snake.move(final[0])
            self.table.print(time.time()-self.start)
            if self.table.check_eaten():
                self.table.change_food()
                self.table.snake.grow()






a = Game(n_paths    = 10,
    n_steps    = 10,
    snake_size = 10,
    time_sleep = .0)
    
a.simulate()
