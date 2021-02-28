from game import Game

def main():
    a = Game(
        jobs = 4,
        max_steps = 1000,
        n_paths    = 20,
        n_steps    = 5,
        snake_size = 20,
        time_sleep = .0
        ) 
    a.simulate()

if __name__ == "__main__":
    main()
