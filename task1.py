def pownum(a: float, n: int) -> float:
    '''
    Function, returning number a in power of n
    :param a: float number
    :param n: power of number
    :return: float number
    '''

    if n == 1:
        return a
    return a * pownum(a, n - 1)
