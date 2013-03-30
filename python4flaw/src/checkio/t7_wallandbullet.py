def checkio(data):
    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]
    return True

if __name__ == '__main__':
    assert checkio([[0,0], [0,2], [5,1], [3,1]]) == True, "First"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "Reverse First"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "Second"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "Third"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "Fourth, shot in butt of wall :)"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "Fifth, parallel"