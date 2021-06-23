"""
Title       : frog game
Description : frog game
Author      : Bernardo Paulsen
Version     : 0.1.0
"""
import logging
import numpy as np
import os
import time

logging.basicConfig()

class Line:
    def __init__(self,
        size    : int,
        p_block : float):
        self.size    = size
        self.p_block = p_block
        self.blocks  = self.initiate_blocks()

    def get_character(self):
        return "X" if np.random.uniform() <= self.p_block else " "

    def initiate_blocks(self):
        return [self.get_character() for _ in range(self.size)]

    def flow_right(self):
        self.blocks = self.blocks[:-1]
        self.blocks.insert(0,self.get_character())

    def flow_left(self):
        self.blocks = self.blocks[1:]
        self.blocks.append(self.get_character())

class River:
    def __init__(self,
        n_rivers : int,
        size     : int,
        n_blocks : int):
        self.lines = self.initiate_lines(n_rivers, size, n_blocks)

    def flow(self,
        indexes : list):
        for i in indexes:
            self.lines[i].flow_right() if i%2 else self.lines[i].flow_left()

    @staticmethod
    def initiate_lines(
        n_rivers : int,
        size     : int,
        n_blocks : int):
        if size < 2:
            logging.warning("Line too short, probility of block greater than unity.")
        return [Line(size,p) for p in np.linspace(n_blocks/size,1.0,n_rivers)]

class Frog:
    def __init__(self,
        y : int,
        x : int):
        self.y = y
        self.x = x

    def move_up(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

class Table:
    def __init__(self,
        height   : int,
        width    : int,
        n_blocks : int):
        self.height = height
        self.width  = width
        self.river  = River(height-4, width-8, n_blocks)
        self.frog   = Frog(height-2, int(width/2))

    def print(self):
        

r = River(10,20,4)
for _ in range(20):
    os.system("clear")
    for line in r.lines:
        print(line.blocks)
    r.flow(range(10))
    time.sleep(.5)
