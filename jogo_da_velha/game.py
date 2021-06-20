from player import Player
from table import Table
import os

class Game:
    VICTORIES = [
        {1,2,3},
        {4,5,6},
        {7,8,9},
        {1,4,7},
        {2,5,8},
        {3,6,9},
        {1,5,9},
        {3,5,7},
        ]
    def __init__(self):
        self.players = self.get_players()
        self.table   = Table()
        self.run()
    def get_players(self):
        players = []
        for i in range(2):
            player_name = input("Enter name of player:")
            players.append(Player(player_name))
        return players
    def run(self):
        os.system('clear')
        self.table.print(self.players)
        while True:
            for player in self.players:
                point = int(input(F"{player.name}: enter a number [1,...,9]"))
                player.add_point(point)
                self.table.print(self.players)
                if_win, player = self.check_win()
                if if_win:
                    print(f"Congratulations {player.name}!")
                    return None

    def check_win(self):
        for player in self.players:
            points = player.points
            for victory in self.VICTORIES:
                if victory.issubset(set(points)):
                    return True, player
        return False, None