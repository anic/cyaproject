#http://www.checkio.org/mission/task/reverse-polish-notation/
def checkio(expression):
    'transform the expression'

if __name__ == '__main__':
    assert checkio('a+b') == 'ab+', 'First'
    assert checkio('((a+b)*(z+x))') == 'ab+zx+*', 'Second'
    assert checkio('((a+t)*((b+(a+c))^(c+d)))') == 'at+bac++cd+^*', 'Third'
    assert checkio('a+b*c+d') == 'abc*+d+' , 'Fourth'
    print 'All ok'