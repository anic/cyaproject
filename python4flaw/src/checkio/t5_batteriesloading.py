
def calculate(halfsum, cur_sum, stones, next):
    #get stone[next]
    if next == len(stones) or cur_sum >= halfsum:
        diff = abs(halfsum - cur_sum)
        return diff
    
    #try get stone[next]
    diff_get = calculate(halfsum, cur_sum + stones[next], stones, next + 1)
    #print halfsum, cur_sum + stones[next], next + 1, "diff_get", diff_get
    
    diff_none = calculate(halfsum, cur_sum, stones, next + 1)
    #print halfsum, cur_sum , next + 1, "diff_none", diff_none
    
    if diff_get < diff_none:
        return diff_get
    else:
        return diff_none
    
    

def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    stones.sort(reverse=True)
    #print stones
    
    sum = 0
    for i in stones:
        sum += i
    #print sum / 2.0
    
    return calculate(sum / 2.0, stones[0], stones, 1) * 2
    
    

if __name__ == '__main__':
    print checkio([5, 8, 13, 27, 14])
    assert checkio([10, 10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5, 5, 6, 5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print 'All is ok'
