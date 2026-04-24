def progress(a1: float, r: float, n: int) -> float:
    '''
    Function, calculating n-th term of an arithmetic progression
    :param a1: current term
    :param r: common ratio
    :param n: the given number
    :return: amount of numbers in a given number
    '''

    if n == 1:
        return a1
    return progress(a1 + r, r, n - 1)
