from game import Game
import pickle





class Manager:
    def __init__(self):
        self.games = self.load_games()
        self.run()

    def load_games(self):
        with open("jogo_da_velha/games.pickle",'rb') as file:
            return pickle.load(file)

    def run(self):
        while True:
            message = """Enter:
1 - new game
2 - quit"""
            option  = int(input(message))
            if option == 1:
                game = Game()
                self.games.append(game)
            else:
                with open("games.pickle","wb") as file:
                    pickle.dump(self.games, file)
                    return None

    




