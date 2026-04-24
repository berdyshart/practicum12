def mod_number(a: int, b: int) -> int:
    '''
    Function, calculating the biggest divisor of a and b
    :param b: number b
    :param a: number a
    :return: the biggest divisor of a and b
    '''

    if b == 0:
        return a
    return mod_number(b, a % b)
