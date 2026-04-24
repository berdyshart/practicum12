def odd_list(a: list, n: int) -> list:
    '''
    Function, selecting odd elements of a list.
    :param n: length of list
    :param a: given list
    :return: list of odd elements
    '''

    if n == 0:
        return a

    if a[0] % 2 == 0:
        a = a[1:] + [a[0]]
        return odd_list(a, n-1)
    return odd_list(a[1:], n-1)
