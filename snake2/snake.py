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