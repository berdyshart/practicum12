def find_rec(string1: str, string2: str, length: int) -> str:
    '''
    Function to find the biggest common substring between two strings
    :param length: assumed length of biggest common substring
    :param string1: string with smaller length
    :param string2: string with bigger length
    :return: the biggest common substring
    '''

    if length == 0:
        return ''

    for i in range(len(string1) - length + 1):
        cur_string = string1[i:i + length]
        if cur_string in string2:
            return cur_string

    return find_rec(string1, string2, length - 1)


def comp(a: str, b: str, m: int, n: int) -> str:
    '''
    Function to find the biggest common substring between two strings
    :param a: string a
    :param b: string b
    :param m: length of string a
    :param n: length of string b
    :return: the biggest common substring
    '''

    if m < n:
        return find_rec(a, b, m)
    return find_rec(b, a, n)
