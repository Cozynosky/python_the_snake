import pickle

unsaved = [1, 2, 3, 4, 5, 6, 7, 7]

pickle.dump(unsaved, open("testfile", "wb"))

loaded = pickle.load(open("testfile", "rb"))

print(loaded)
