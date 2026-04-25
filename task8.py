def fib(k: int) -> int:
    '''
    Function, calculating the k-th term of the Fibonacci sequence
    :param k: term to be calculated
    :return: k-th term of the Fibonacci sequence
    '''

    if k <= 2:
        return 1
    
    return fib(k - 1) + fib(k - 2)
