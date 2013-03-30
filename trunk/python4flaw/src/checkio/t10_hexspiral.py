#http://www.checkio.org/mission/task/hex-spiral/

def checkio(data):
    "Find the destination"
    a, b = data

if __name__ == '__main__':
    assert checkio([2, 9]) == 1, "First"
    assert checkio([9, 2]) == 1, "Reverse First"
    assert checkio([6, 19]) == 2, "Second, short way"
    assert checkio([5, 11]) == 3, "Third"
    assert checkio([13, 15]) == 2, "Fourth, One row"
    assert checkio([11, 17]) == 4, "Fifrth, One more test"