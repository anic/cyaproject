def checkio(data):
    'Return True if password strong and False if not'
    import re
    
    number_match = re.compile(r'\d').search(data) != None
    lowercase_match = re.compile(r'[a-z]').search(data) != None
    uppercase_match = re.compile(r'[A-Z]').search(data) != None
    return len(data) >= 10 and number_match and lowercase_match and uppercase_match

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, 'First'
    assert checkio('bAse730onE4') == True, 'Second'
    assert checkio('asasasasasasasaas') == False, 'Third'
    assert checkio('QWERTYqwerty') == False, 'Fourth'
    assert checkio('123456123456') == False, 'Fifth'
    assert checkio('QwErTy911poqqqq') == True, 'Sixth'
    print 'All ok'
