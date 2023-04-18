"""
Helper functions live here
"""


def find_sum(var_limit):
    """
    This function returns the sum of 1 to x
    """

    num = 0
    for i in range(var_limit+1):
        num += i
    return num
