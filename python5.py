def add_numbers(*args):
    """
    Adds variable-length integer arguments.

    Parameters:
    *args: Variable-length integer arguments to be added.

    Returns:
    int: The sum of all the arguments.
    """
    return sum(args)

result = add_numbers(1, 2, 3, 4, 5)
print("The sum is:", result)
