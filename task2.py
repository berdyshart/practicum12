def count(n: int) -> int:
    '''
    Function, calculating the amount of numbers in a given number
    :param n: the given number
    :return: amount of numbers in a given number
    '''

    if n < 10:
        return 1
    
    return 1 + count(n//10)
