small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

# Deleting individual item
small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

# What happens if one try to discard non-existing item?
small_ints.discard(99)
print(f"Discarded:\n{small_ints}")

small_ints.remove(99)
print(f"Removed:\n{small_ints}")