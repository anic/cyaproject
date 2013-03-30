def checkio(parameters):
    """Return product of an MxP matrix A with an PxN matrix B."""
    A, B = parameters
    hA = len(A)
    wA = 0
    if hA > 0:
        wA = len(A[0])

    hB = len(B)
    wB = 0
    if hB > 0:
        wB = len(B[0])
        
    result = [[0 for col in range(wB)] for row in range(hA)]
    for j in range(0, hA):
        for i in range(0, wB):
            for y in range(0, wA):
                result[j][i] += A[j][y]*B[y][i]
    
    return result
    
if __name__ == '__main__':
    assert checkio([[
                    [6, 7, 8],
                    [5, 4, 5],
                    [1, 1, 1]
                   ],
                   [
                    [1, 2, 3],
                    [1, 2, 3],
                    [1, 2, 3]
                   ]]) == [
                            [21, 42, 63],
                            [14, 28, 42],
                            [3, 6, 9]
                         ], 'First'
    assert checkio([[
                    [4, 4, -1, 0, -1, 8],
                    [2, 3, 7, 5, 2, 3],
                    [3, 2, 5, 7, 3, 2],
                    [1, 2, 2, 1, 1, 2],
                    [1, 7, 6, 6, 5, 7]
                  ], [
                      [-5, -7, -2, 2, -2, 16, 1],
                      [0, 0, 4, 0, -5, 0, 4],
                      [2, 0, -2, 0, 2, 0, 1],
                      [6, 4, 6, -1, 15, -5, 5],
                      [5, -4, 10, 1, 14, 6, 1],
                      [3, 0, -2, 0, 3, 0, 1]]]) == [
                                                [-3, -24, -16, 7, -20, 58, 26],
                                                [53, -2, 38, 1, 107, 19, 51],
                                                [58, -5, 60, 2, 147, 31, 56],
                                                [16, -7, 14, 2, 27, 17, 19],
                                                [89, -3, 86, 1, 156, 16, 77]
                                            ], 'Second'
    print 'All Ok'
