def mod_number(a: int, b: int) -> int:
    '''
    Function, calculating the remainder of division of number a by number b
    :param b: divisor
    :param a: dividend
    :return: remainder
    '''

    if a < b:
        return a
    
    return mod_number(a - b, b)
