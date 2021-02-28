from game import Game

def main():
    a = Game(max_steps = 100,
    n_paths    = 10,
    n_steps    = 10,
    snake_size = 10,
    time_sleep = .0) 
    a.simulate()

if __name__ == "__main__":
    main()
