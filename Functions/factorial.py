def factorial(number: int) -> int:
    """
    Returns factorial of a number.
    :param number: Integer.
    :return: Integer.
    """
    sum = 1
    if number == 0:
        return sum
    else:
        for i in range(1, number+1):
            sum*=i
        return sum

print(factorial(4))