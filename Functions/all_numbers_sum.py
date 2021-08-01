from typing import Union
def sum_numbers(*args: float) -> float:
    """
    Returns sum of all given numbers.
    :param args (float): Numbers to sum.
    :return (float): Sum of all given numbers.
    """
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))