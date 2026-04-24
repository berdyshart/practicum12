def ten_to_n(x: int, n: int) -> str:
    '''
    Function, converting a number into n-ary number system.
    :param n: number of n-ary system, 2 <= n <= 16
    :param x: given number
    :return: number in n-ary system
    '''

    SYSTEM_16 = '0123456789ABCDEF'

    if x < n:
        return str(x)

    return ten_to_n(x // n, n) + str(SYSTEM_16[x % n])
