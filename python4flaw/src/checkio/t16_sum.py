def checkio(n):
    '''
    Let G(S) denote the sum of the elements of set S and F(n) be the sum of G(s) 
    for all subsets of the set consisting of the first n natural numbers. 
    For example, F(3) = (1) + (2) + (3) + (1 + 2) + (1 + 3) + (2 + 3) + (1 + 2 + 3) = 24. 
    Given n, calculate F(1) + F(2) + ... + F(n)
    '''
    if n == 1:
        return 1
    
    cur_fn = 1
    sum_fn = 1
    for i in range(2, n + 1):
        cur_fn = 2 * cur_fn + (2 ** (i - 1)) * (i)
        sum_fn += cur_fn
    
    return sum_fn
    

if __name__ == '__main__':
    assert checkio(2) == 7, "First"
    assert checkio(3) == 31, "Second"
    assert checkio(1) == 1, "Third"
    print 'All ok'
