"""
Title      : Snake - Main
Description: Initiates the game and runs a simulation.
Author     : Bernardo Paulsen
Version    : 2.0.0
"""
from game import Game

def main():
    a = Game(
        jobs = 4,
        max_steps = 5000,
        n_paths    = 40,
        n_steps    = 10,
        snake_size = 10,
        time_sleep = .0
        ) 
    a.simulate()

if __name__ == "__main__":
    main()
