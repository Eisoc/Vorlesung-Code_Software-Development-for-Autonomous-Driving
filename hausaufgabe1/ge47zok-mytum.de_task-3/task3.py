"""
Goal of Task 3:
    Implement a function that returns the lowest missing number of the list, starting from 0.
"""


def lowest_missing_number(list_in):
    """
    input:
        list_in (type: list): list of integers

    output:
        lowest_number (type: int or None)
    """

    # Task:
    # ToDo: Calculate the lowest missing number of the list, starting from 0. Return "None" if there is no lowest
    #       missing number. The usage of python packages is not allowed for this task.
    # Hint: e.g. L = [3, 6, 1, 0, 9, 7, 2] the function should return 4
    ########################
    #  Start of your code  #
    ########################

    ########################
    #   End of your code   #
    ########################
    missed = []
    lowest_number = None
    for zahl in range(0, len(list_in)):
        x = 0
        for element in list_in:
            if element == zahl:
                x += 1
        if x == 0:
            missed.append(zahl)
    if missed == []:
        lowest_number = None
    else:
        lowest_number = min(missed)
    return lowest_number


if __name__ == "__main__":
    assert lowest_missing_number([3, 6, 1, 0, 9, 7]) == 2
    assert lowest_missing_number([0, 1, 2, 3, 4, 5]) is None
