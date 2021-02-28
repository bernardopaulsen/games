import random
from table import Table
import time

class Game():

    def __init__(self,
        max_steps  = 50,
        n_paths    = 10,
        n_steps    = 10,
        snake_size = 10,
        time_sleep = .2):

        self.table      = Table(snake_size)
        self.max_steps  = max_steps
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
        for _ in range(self.max_steps):
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