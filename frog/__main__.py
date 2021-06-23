import numpy as np
import os
import time

class Frog:
    MOVEMENTS = {
        "w": (-1,0),
        "a": (0,-1),
        "s": (1,0),
        "d": (0,1)
        }
    def __init__(self,
        position : list = [11,25]):
        self.position = position

    def move(self, direction):
        p = self.position
        y = p[0]
        x = p[1]
        m = self.MOVEMENTS[direction]
        a = m[0]
        b = m[1]
        self.position = [y+a,x+b]



class Game:
    def __init__(self):
        self.run()


    def run(self):
        f = Frog()
        t = Table()
        while True:
            t.print(f)
            direction = self.input_direction()
            f.move(direction)

    @staticmethod
    def input_direction():
        valid_inputs = {"w","a","s","d"}
        while True:
            actual_input = input("Enter direction (w,a,s,d): ")
            if actual_input in valid_inputs:
                return actual_input
            else:
                pass 

class Line:
    def __init__(self,
        width : int   = 50,
        prob  : float = .5,
        index : int   = 0):
        self.width     = width
        self.prob      = prob
        self.direction = self.get_direction(index)
        self.symbols   = self.initiate_symbols()

    @staticmethod
    def get_direction(index):
        return not index%2

    def initiate_symbols(self):
        symbols = []
        for _ in range(self.width):
            p = np.random.uniform()
            if p < self.prob:
                symbols.append("X")
            else:
                symbols.append(" ")
        return symbols

    def update(self):
        p              = np.random.uniform()
        if self.direction:
            actual_symbols = self.symbols[:-1]
            if p < self.prob:
                actual_symbols.insert(0,"X")
            else:
                actual_symbols.insert(0," ")
        else:
            actual_symbols = self.symbols[1:]
            if p < self.prob:
                actual_symbols.append("X")
            else:
                actual_symbols.append(" ")
        self.symbols = actual_symbols

class River:
    def __init__(self,
        height   : int   = 9,
        width    : int   = 46,
        min_prob : float = .2,
        max_prob : float = .4):
        self.height = height
        self.width  = width
        self.prob   = np.linspace(min_prob,max_prob,self.height)
        self.lines = self.initiate_lines()
    
    def initiate_lines(self):
        return [Line(self.width,p,i) for p, i in zip(self.prob,range(self.height))]

    def print(self):
        string = ""
        for line in self.lines:
            for symbol in line.symbols:
                string += symbol
            string += "\n"
        os.system("clear")
        print(string)

    def flow(self,i):
        for h in range(self.height):
            if not i%(h+1):
                self.lines[h].update()

class Table:
    def __init__(self,
        height : int = 20, 
        width  : int = 50):
        self.height = height
        self.width  = width
        self.frog   = Frog([self.height - 2, int(self.width/2)])
        self.river  = River(self.height - 2, self.width - 2, .2,.4)

    def print(self,
        frog :  Frog,
        river : River):
        table = ""
        for y in range(self.height):
            for x in range(self.width):
                if frog.position == [y,x]:
                    table += "o"
                else:
                    y_low = y > 1
                    y_upp = y < self.height - 2
                    x_low = x > 1
                    x_upp = x < self.width - 2
                    if y_low and y_upp and x_low and x_upp:
                            table += river.lines[y-2].symbols[x-2]
                    else:
                        table += " "
            table += "\n"
        os.system('clear')
        print(table)

    def run(self):
        s = 3/self.height
        i = 0
        start = time.time()
        while True:
            i += 1
            self.print(self.frog,self.river)
            print(f"{time.time()-start:.2f} seconds")
            if not self.check_finish():
                self.frog_move()
                self.river.flow(i)
                self.frog_flow(i)
                time.sleep(s)
            else:
                print("FINISHED!")
                break

    def frog_flow(self, i : int):
        y = self.frog.position[0]
        if y > 1 and not i%(y-1):
            frog_pos = self.frog.position
            x        = frog_pos[1]
            y_lo     = y > 1
            y_up     = y < self.height - 2
            x_lo     = x > 1
            x_up     = x < self.width - 2
            if y_lo and y_up and x_lo and x_up:
                if self.river.lines[y-2].direction:
                    self.frog.move("d")
                else:
                    self.frog.move("a")

    def frog_move(self):
        frog_pos = self.frog.position
        y        = frog_pos[0]
        x        = frog_pos[1]
        y_lo     = y > 1
        y_up     = y < self.height - 1
        x_lo     = x > 1
        x_up     = x < self.width - 2
        if y_lo and y_up and x_lo and x_up:
            next_line = self.river.lines[y-3]
            character = next_line.symbols[x-2]
            if character == "X":
                self.frog.move("w")

    def check_finish(self):
        return self.frog.position[0] == 1

t = Table(20,50)
t.run()

