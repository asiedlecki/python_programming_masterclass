import shelve

# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "a sweet, orange, citrus, fruit"
#     fruit['apple'] = "goof for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# print(fruit)

fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus, fruit"
fruit['apple'] = "goof for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)

fruit.close()