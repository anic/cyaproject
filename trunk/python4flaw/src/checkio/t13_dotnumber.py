#http://www.checkio.org/mission/task/dot-separated-numbers/
import re

def checkio(txt):
    '''
    string with dot separated numbers, which inserted after every third digit from right to left
    '''
    reg = re.compile(r'\d{4,}(?!\w)')
    match = reg.findall(txt)
    for s in  match:
        result = ""
        ls = len(s)
        for i in range(0, ls):
            if i % 3 == 0 and i > 0:
                result = "." + result
            result = s[ls - i - 1] + result
       
        txt = txt.replace(s, result)

#    print txt
    return txt
    
if __name__ == '__main__':
    assert checkio('123456') == '123.456'
    assert checkio('333') == '333'
    assert checkio('9999999') == '9.999.999'
    assert checkio('123456 567890') == '123.456 567.890'
    assert checkio('price is 5799') == 'price is 5.799'
    assert checkio('he was born in 1966th') == 'he was born in 1966th'
    print 'All ok'
