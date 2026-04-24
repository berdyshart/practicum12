def fun2(x: int, k=2) -> int:
    '''
    Function, defining if x is prime or not
    :param x: given number
    :param k: current divisor
    :return: 1 if x is prime, 0 if not
    '''

    if k == x:
        return 1
    if x % k == 0:
        return 0

    return 1 * fun2(x, k + 1)


def function1(x: int) -> bool:
    '''
    Function, defining if x is prime or not.
    :param x: given number
    :return: True if x is prime, False if not.
    '''

    if fun2(x) == 1:
        return True
    return False
