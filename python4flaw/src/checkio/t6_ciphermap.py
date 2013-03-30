def cmp_xy(X, Y):
    if X[0] != Y[0]:
        return X[0] - Y[0]
    else:
        return X[1] - Y[1]

def get_code(cordin, map):
    result = ''
    for i in range(0, len(cordin)):
#        print cordin[i][0], cordin[i][1], map[cordin[i][0]][cordin[i][1]]
        result += map[cordin[i][0]][cordin[i][1]]
    return result

def switch_cordin(cordin, N):
    for i in range(0, len(cordin)):
        #x' = y; y' = N-1 -x
        x2 = cordin[i][1]
        y2 = N - 1 - cordin[i][0]
        cordin[i] = (x2, y2) #cover origin cordinate
    #sort new cordin
    cordin.sort(cmp_xy)

def checkio(input_data):
    'Return password of given cipher map'
    N = len(input_data[0])
    cordin = []
    for i in range(0, N):
        for j in range(0, N):
            if input_data[0][i][j] != '.':
                cordin.append((i, j))
    
    result = get_code(cordin, input_data[1])
    for i in range(0, 3):
        switch_cordin(cordin, N)
        result += get_code(cordin, input_data[1])
    
    return result

if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'], [
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio([[
    '....',
    'X..X',
    '.X..',
    '...X'], [
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
