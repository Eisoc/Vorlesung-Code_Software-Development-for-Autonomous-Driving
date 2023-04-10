"""
Goal of Task 1:
    Implement a function that reverses the word order of a string.
"""


def reverse(sentence):
    """
    input:
        sentence (type: str)

    output:
        reversed_sentence (type: str)
    """

    # Task:
    # ToDo: Compute the reversed word order of a string.
    #       The usage of python packages is not allowed for this task.
    ########################
    #  Start of your code  #
    ########################

    to_list = list(sentence.split(" "))
    to_list.reverse()
    reversed_sentence = " ".join(to_list)

    ########################
    #   End of your code   #
    ########################

    return reversed_sentence


if __name__ == "__main__":
    assert reverse("this is a test") == "test a is this"
