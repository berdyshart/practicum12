def numbers(x: int) -> None:
    '''
    Function, writing the elements of numbers in reverse order
    :param x: number
    :return: None
    '''

    if x > 9:
        print(x % 10)
        numbers(x // 10)
    else:
        print(x)
