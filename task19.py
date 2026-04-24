def count(a: int, b: int) -> int:
    '''
    Function, calculating the maximum number of squares could be got from a
    given rectangle.
    :param a: a side of the rectangle
    :param b: b side of the rectangle
    :return: number of squares
    '''

    if a == b:
        return 1

    a, b = min(a, b), max(a, b) - min(a, b)
    return 1 + count(a, b)
