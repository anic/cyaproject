#http://www.checkio.org/mission/task/all-in-row/
is_array = lambda var: isinstance(var, (list, tuple))

def fillresult(input,result):
    if not is_array(input):
        result.append(input)
        return
    
    for i in input:
        fillresult(i, result)

def checkio(arr):
    'convert all elements in arr in one row'
    result = []
    fillresult(arr, result)
    return result

if __name__ == '__main__':
    assert checkio([1,2,3]) == [1,2,3], 'First'
    assert checkio([1,[2,2,2],4]) == [1,2,2,2,4], 'Second'
    assert checkio([[[2]],[4,[5,6,[6],6,6,6],7]])\
                              == [2,4,5,6,6,6,6,6,7], 'Third'
    print 'All ok'