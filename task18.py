def simmetr(s: str, i: int, j: int) -> bool:
    '''
    Function, defining whether s[i:j] is symmetric or not.
    :param s: given string
    :param i: left index of string
    :param j: right index of string
    :return: True if symmetric, False otherwise
    '''

    if j - i == 0:
        return True

    if s[i] == s[j]:
        return simmetr(s, i + 1, j - 1)
    return False
