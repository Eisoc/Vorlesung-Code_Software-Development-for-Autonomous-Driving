"""
Goal of Task 2:
    Implement a function that returns the median of a list.
"""


def calc_median(list_in):
    """
    input:
        list_in (type: list): list of integers

    output:
        median (type: int or float)
    """

    # Task:
    # ToDo: Calculate the median of the given list.
    #       The usage of python packages is not allowed for this task.
    # Hints:
    #     - list might be unsorted
    #     - for an odd number of items the median is part of the list,
    #       e.g. for [0, 9, 2, 3, 1, 4, 7] the function should return 3 (type: int).
    #     - for an even number of items the median is not part of the list but the mean of two middle number,
    #       e.g. for [0, 9, 2, 3, 1, 4, 7, 5] the function should return 3.5 (type: float).
    ########################
    #  Start of your code  #
    ########################

    ########################
    #   End of your code   #
    ########################
    median = 0
    sort_list = sorted(list_in)
    if len(sort_list) % 2 == 0:
        median = (sort_list[int((len(sort_list)) / 2 - 1)] + sort_list[int(len(sort_list) / 2)]) / 2
    elif len(sort_list) % 2 != 0:
        median = sort_list[int((len(sort_list) + 1) / 2 - 1)]

    return median


if __name__ == "__main__":
    # Example with even number of items
    assert calc_median([0, 9, 2, 3, 1, 4, 7]) == 3

    # Example with odd number of items
    assert calc_median([0, 9, 2, 3, 1, 4, 7, 5]) == 3.5
