import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

with shelve.open("bike2") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engin_size"] = 250

    print(bike["engine_size"])
    print(bike["engin_size"])
    print(bike["colour"])

    del bike['engin_size']

    for key in bike:
        print(key)

    print('=' * 40)

    print(bike["engine_size"])
    print(bike["engin_size"])
    print(bike["colour"])


## shelve is persisted to a file so we have two entries
## one for engine_size and one for erroneous name: enign_size

