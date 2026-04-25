def combin(n: int, k: int) -> float:
    '''
    Function, calculating the combination of n choose k.
    :param n: element n
    :param k: element k
    :return: the combination of n choose k
    '''

    if k == 0:
        return 1
    
    return n / k * combin(n - 1, k - 1)
