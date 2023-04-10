"""
Goal of Task 4:
    Implement a function that returns the n-th number of the Fibonacci Sequence.
"""


def fibonacci(n):
    """
    input:
        n (type: int)

    output:
        fibonacci_number (type: int)
    """

    # Task:
    # ToDo: Calculate the n-th number of the Fibonacci Sequence.
    #       The usage of python packages is not allowed for this task.
    # Hint: F_n = F_n-1 + F_n-2
    ########################
    #  Start of your code  #
    ########################

    ########################
    #   End of your code   #
    ########################
    fibonacci_number = int(1 / (5 ** 0.5) * (((1 + 5 ** 0.5) / 2)**n - ((1 - 5 ** 0.5) / 2)**n))
    return fibonacci_number


if __name__ == "__main__":
    assert fibonacci(9) == 34
