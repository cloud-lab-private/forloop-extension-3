def factorial(n):
    """
    Calculate the factorial of a non-negative integer using a for loop.

    The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.
    For example:
        5! = 5 * 4 * 3 * 2 * 1 = 120

    We'll use a for loop to multiply each number from 1 to n together to calculate the factorial.

    @param n: The number for which to calculate the factorial.
    @return: The factorial of the given number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Initialize the result variable to store the factorial value
    result = 1
    
    # Iterate through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        result *= i  # Multiply each number to the result
    
    # Return the calculated factorial value
    return result
