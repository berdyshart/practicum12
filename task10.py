def maxlist(a: list) -> float:
    '''
    Function, calculating the maximum value of a list.
    :param a: given list
    :return: maximum value
    '''

    if len(a) == 1:
        return a[0]
    if a[0] > a[-1]:
        a = a[1:-1] + [a[0]]
    else:
        a = a[1:]

    return maxlist(a)
