def digital_root(value):
    result = value
    while True:
        if result < 10:
            break
    
        tmp = result
        result = 0
        while True:
            result += tmp % 10
            tmp = tmp / 10
            if tmp == 0:
                break
            
    print 'digital_root(', value, ')=', result
    return result
    
def checkio(value):
    'calculate sum of the digital roots of a numbers which are the results of factorization of the specified number'
    result = 0
    for i in range(1, value + 1):
        result += digital_root(i)
        
    return result
    
if __name__ == '__main__':
    print checkio(50)
    
    assert checkio(50) == 32, 'First'
    assert checkio(100) == 75, 'Second'
    assert checkio(999) == 75, 'Third'
    assert checkio(9999) == 117, 'Fourth'
    print 'All ok'
