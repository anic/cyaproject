#http://www.checkio.org/mission/task/the-factorials-of-the-digits-of-number/

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#print factorial(10)

def checkio(data):
    'calculate sum of the factorials for all digits of the specified positive integer number.'
    f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    result = 0
    str_data = str(data)
    for i in range(0, len(str_data)):
        result += f[int(str_data[i])]
    
    return result
    
if __name__ == '__main__':
#    for i in range(1, 11):
#        print factorial(i)
#    
    
    assert checkio(100) == 3, 'First'
    assert checkio(222) == 6, 'Second'
    assert checkio(1234) == 33, 'Third'
    print 'All ok'
