#http://www.checkio.org/mission/task/matrix-transpose/

def checkio(matr):
    'return a transposed matrix'
    h = len(matr)
    if h == 0:
        return []
    
    w = len(matr[0])
    
    result = [[0 for col in range(h)] for row in range(w)]
    for j in range(0, w):
        for i in range(0, h):
            result[j][i] = matr[i][j]
            
    return result
    
if __name__ == '__main__':
    assert checkio([[1, 2],
             [1, 2]]) == [[1, 1],
                          [2, 2]], 'First'
    assert checkio([[1, 0, 3, 4, 0],
                    [2, 0, 4, 5, 6],
                    [3, 4, 9, 0, 6]]) == [[1, 2, 3],
                                      [0, 0, 4],
                                      [3, 4, 9],
                                      [4, 5, 0],
                                      [0, 6, 6]], 'Second'
    print 'All ok'
