import pickle

l = []
with open("games.pickle","wb") as file:
    pickle.dump(l,file)