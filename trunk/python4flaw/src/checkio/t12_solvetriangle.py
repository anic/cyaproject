#http://www.checkio.org/mission/task/acm91-problema-triangular-vertices/
def checkio(inset):
    return 0

if __name__ == "__main__":
    assert checkio([1,2,3]) == 3, 'triangle'
    assert checkio([11,13,29,31]) == 0, 'not parallelogram'
    assert checkio([26,11,13,24]) == 4, 'parallelogram'
    assert checkio([4,5,9,13,12,7]) == 6, 'hexagon'
    assert checkio([1,2,3,4,5]) == 0, 'it very strange triangle'
    assert checkio([47]) == 0, 'point'
    assert checkio([11,13,23,25]) == 0, 'again not parallelogram'