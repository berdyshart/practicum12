def search(a: list, x: int) -> int:
    '''
    Function, finding num x in a list a.
    :param x: number to find
    :param a: given list
    :return: 1, if x in a, else 0
    '''

    if len(a) == 0:
        return 0
    if x == a[0]:
        return 1

    return search(a[1:], x)
