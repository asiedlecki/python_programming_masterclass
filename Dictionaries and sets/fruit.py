fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "lovely",
       "spinach": "can I have some fruit, please"}

print(veg)

veg.update(fruit)

print(veg)


# safer method (doesn't change object in place)
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)