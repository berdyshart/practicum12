def ten_to_bin(x: int) -> str:
    '''
    Function, converting a number into binary.
    :param x: given number
    :return: number in binary.
    '''

    if x == 1:
        return '1'

    return ten_to_bin(x // 2) + str(x % 2)
