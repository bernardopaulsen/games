"""
Title      : Snake - Game
Description: Game module for snake game.
Author     : Bernardo Paulsen
Version    : 2.0.0
"""
from multiprocessing import Pool
import random
from table import Table
import time

class Game():

    def __init__(self,
        jobs       = 4,
        max_steps  = 50,
        n_paths    = 10,
        n_steps    = 10,
        snake_size = 10,
        x_size     = 60,
        y_size     = 45,
        time_sleep = .2):

        self.table      = Table(snake_size,x_size,y_size)
        self.jobs       = jobs
        self.max_steps  = max_steps
        self.n_paths    = n_paths
        self.n_steps    = n_steps
        self.snake_size = snake_size
        self.time_sleep = time_sleep
        self.start      = time.time()

    def get_directions(self):
        loops = 1
        while loops <= 50000:
            loops     += 1
            directions = [random.randint(0,3) for _ in range(self.n_steps)]
            if not self.table.snake.check_crash(directions,self.table.x_size,self.table.y_size):
                break
        assert loops <= 50000, 'Infinite loop.'
        return directions

    def get_distances(self, directions):
        new_pos = self.table.snake.new_positions(directions)
        distance = 100000.
        for p in new_pos:
            dis = self.table.check_distance(p)
            if dis < distance:
                distance = dis
        return distance

    def get_paths(self,n_path):
        return [self.get_directions() for _ in range(n_path)]

    def simulate(self):
        snake_size = len(self.table.snake.positions)
        n_path = int(snake_size/self.jobs)
        trials = [n_path] * self.jobs
        pool   = Pool(processes=self.jobs)
        self.table.print(time.time()-self.start)
        for _ in range(self.max_steps):
            #directions = self.get_paths(self.n_paths)
            results    = pool.map(self.get_paths,trials)
            directions = []
            for res in results:
                directions.extend(res)
            l          = [self.get_distances(d) for d in directions]
            index      = l.index(min(l))
            final      = directions[index]
            time.sleep(self.time_sleep)
            self.table.snake.move(final[0])
            self.table.print(time.time()-self.start)
            if self.table.check_eaten():
                self.table.change_food()
                self.table.snake.grow()
