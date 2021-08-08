from datasets.contents import recipes


def my_deepcopy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the 'list' or 'dict' values.

    The function will crash with AttributeError if the values aren't lists
    or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of 'd', with the values being copies of the original values.
    """

    new_d = {}

    for key, value in d.items():
        new_d[key] = value.copy()

    return new_d

recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])