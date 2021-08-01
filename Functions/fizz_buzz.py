def fizz_buzz(number: int):
    """
    Return "fizz" if number is divisible by 3, "buzz" if divisible by 5 or "fizz buzz" if number is divisible
    by both 3 and 5. In other cases return the number itself.
    :param number: Integer.
    :return: String.
    """
    if number % 15 == 0:
            return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return("buzz")
    else:
        return str(number)

for i in range(16):
    print(fizz_buzz(i))

def cos(x):
    """

    :param x:
    :return:
    """