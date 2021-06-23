import os

class Table:
    POSITIONS = {1: (0,0),
        2: (0,1),
        3: (0,2),
        4: (1,0),
        5: (1,1),
        6: (1,2),
        7: (2,0),
        8: (2,1),
        9: (2,2)}
    def print(self, players):
        symbols = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
            ]
        for player in players:
            initial = player.initial
            for point in player.points:
                xy = self.POSITIONS[point]
                x  = xy[1]
                y  = xy[0]
                symbols[y][x] = initial
        os.system('clear')
        print(f""" {symbols[0][0]} | {symbols[0][1]} | {symbols[0][2]}
---+---+---
 {symbols[1][0]} | {symbols[1][1]} | {symbols[1][2]}
---+---+---
 {symbols[2][0]} | {symbols[2][1]} | {symbols[2][2]}
""")