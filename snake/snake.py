"""
Title      : Snake - Snake
Description: Snake module for snake game.
Author     : Bernardo Paulsen
Version    : 2.0.1
"""
class Snake:
    """
    Class that represents the snake from the snake game.
    """
    DIRECTIONS = {0: {'x':0, 'y': 1},
        1: {'x': -1, 'y':  0},
        2: {'x':  0, 'y': -1},
        3: {'x':  1, 'y':  0}}

    def __init__(self,
        size = 3):
        """
        Parameters
        ----------
        size : int
            Initial size of snake.
        """
        self.positions = [[i,0] for i in range(size)]

    def check_crash(self, directions: list, x_size: int, y_size: int) -> bool:
        """
        Checks if snake eats itself or gets out of the table given the directions
        the snake will follow.

        Parameters
        ----------
        directions : list
            List of directions for the snake to follow.
        x_size : int
            Length of table.
        y_size : int
            Height of table.

        Returns
        -------
        bool
            True if snake crashes.

        """
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
        """
        Checks if food is eaten given the directios the snake will follow.

        Parameters
        ----------
        directions : list
            Directions the snake will follow.
        food : list
            Food's position

        Returns
        -------
        bool
            True if food is eaten.
        """
        new_pos   = self.new_positions(directions)
        if food in new_pos:
            return True
        else:
            return False

    def get_directions(self, direction: int) -> tuple:
        """
        Returns changes in the x and y for each direction.

        Paramenters
        -----------
        direction : int
            Number of direction.

        Returns
        -------
        tuple
            Changes in x and y.
        """
        return self.DIRECTIONS[direction]['x'], self.DIRECTIONS[direction]['y']
    
    def grow(self):
        """
        Grows the snake (one position). The snake will grow from the tail.
        """
        snake = [self.positions[0]]
        snake.extend(self.positions)
        self.positions = snake

    def move(self, direction: int):
        """
        Moves the snake given a new direction.

        Parameters
        ----------
        direction : int
            Number of direction.
        """
        #size = len(self.positions)
        x, y = self.get_directions(direction)
        #for i in range(size):
        #    if i < size - 1:
        #        self.positions[i] = self.positions[i+1]
        #    else:
        #        pos = self.positions[i]
        #        self.positions[i] = [pos[0] + x, pos[1] + y]
        snake = self.positions
        snake.append([snake[-1][0] + x, snake[-1][1] + y])
        self.positions = snake[1:]

    def new_positions(self, directions: list) -> list:
        """
        Returns new positions the snake will take given directions.

        Parameters
        ----------
        directions : list
            Directions for the snake to follow

        Returns
        -------
        list
            New positions the snake will take.

        """
        pos = [self.positions[-1]]
        for d in directions:
            x, y = self.get_directions(d)
            pos.append([pos[-1][0]+x,pos[-1][1]+y])
        return pos[1:]

    @staticmethod
    def check_outside(snake : list, x_size : int, y_size : int) -> bool:
        """
        Checks if snake gets outside the table.

        Parameters
        ----------
        snake : list
            Snake's positions.
        x_size : int
            Length of table.
        y_size : int
            Length of table.

        Returns
        -------
        bool
            True if snake gets outside table.
        """
        outside = False
        for part in snake:
            x, y = part[0], part[1]
            if x < 0 or y < 0 or x >= x_size or y >= y_size:
                outside = True
                break
        return outside

    @staticmethod
    def check_repeated(snake : list) -> bool:
        """
        Checks if snake eats itself.

        Parameters
        ----------
        snake : list
            Snake's positions

        Returns
        -------
        bool
            True if snake eats itself.
        """
        if snake[-1] in snake[:-1]:
            return True
        else:
            return False