import shelve

# Python built-in functions
print(dir())
print()
for obj in dir(shelve.Shelf):
    if obj in dir(shelve.Shelf):
        if obj[0] != '_':
            print(obj)

# help(shelve)