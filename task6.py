def degree5(n: int) -> int:
    '''
    Function, calculating the degree in power of which 5 equals to n
    :param n: number
    :return: degree
    '''

    if n == 1:
        return 0
    if n % 5 != 0:
        return -1

    res = degree5(n // 5)
    if res != -1:
        return 1 + res
    return -1
