"""
Goal of Task 1:
    Implement an automated map-generator.

Hint: Use the already implemented EKF SLAM in EKF_SLAM.py to test your code.
"""


from random import randrange
import numpy as np


def GenerateLandmarks(x_min, x_max, y_min, y_max, n):
    """
    inputs:
        x_min (type: int): lower limit of x-coordinate
        x_max (type: int): upper limit of x-coordinate
        y_min (type: int): lower limit of y-coordinate
        y_max (type: int): upper limit of y-coordinate
        n (type: int): number of landmarks to be generated

    output:
        landmarks (type: np.ndarray, shape (n,2)): [x, y] - points for all n landmarks
    """

    # Task:
    # ToDo: Generate n randomly positioned landmarks within the given range.
    ########################
    #  Start of your code  #
    ########################
    point_list = []
    for num in range(1, n + 1):
        x_point = randrange(x_min, x_max, 1)
        y_point = randrange(y_min, y_max, 1)
        point_list.append((x_point, y_point))
    landmarks = np.array(point_list)
    ########################
    #   End of your code   #
    ########################

    return landmarks
