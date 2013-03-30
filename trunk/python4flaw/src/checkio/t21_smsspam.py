def checkio(line):
    '''
    Output a single number representing the cost of the given slogan, according to Petr's pricing.
    '''

if __name__ == '__main__':
    assert checkio('diamonds are forever') == 38, 'First'
    assert checkio('just do it') == 18, 'Second'
    assert checkio('tastes great, less filling') == 48, 'Third'
    print 'All is ok'