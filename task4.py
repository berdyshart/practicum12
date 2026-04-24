def sum_progress(a1: float, r: float, n: int) -> float:
    '''
    Function, calculating the sum of n terms of an arithmetic progression
    :param a1: first term
    :param r: common ratio
    :param n: amount of terms
    :return: amount of numbers in a given number
    '''

    if n == 1:
        return a1
    return a1 + sum_progress(a1 + r, r, n - 1)
