def divide_two_numbers(a, b):
    """
    Returns the division of two numbers a and b.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


if __name__ == "__main__":
    print("Division of 6 by 3 is:", divide_two_numbers(6, 3))
