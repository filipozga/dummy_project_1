def add_one(number: int) -> int:
    """
    Adds one to the given integer.

    Args:
        a (int): The integer to which one will be added.

    Returns:
        int: The result of adding one to the input integer.
    """
    return number + 1


def add_two(number: int) -> int:
    """
    Adds two to the given integer.

    Args:
        number (int): The integer to which two will be added.

    Returns:
        int: The result of adding two to the input integer.
    """
    return number + 2


if __name__ == "__main__":
    # Example usage
    result = add_one(5) + add_two(3)
    print(f"Result: {result}")
