#http://www.checkio.org/mission/task/roman-numerals/
def checkio(number):
    'return roman numeral using the specified integer value from range 1...3999'
#I    1
#V    5
#X    10
#L    50
#C    100
#D    500
#M    1,000
    digits = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'], ['M']]

    result = ''
    if number / 1000 > 0:
        result = 'M' * (number / 1000)
    
    number = number % 1000
    level = 2
    while level >= 0:
        cur = number % (10 ** (level + 1)) / (10 ** level)
        if cur == 9:
            result += digits[level][0] + digits[level][2]
        elif cur > 5:
            result += digits[level][1] + digits[level][0]*int(cur - 5)
        elif cur == 5:
            result += digits[level][1]
        elif cur == 4:
            result += digits[level][0] + digits[level][1]
        else:
            result += digits[level][0]*int(cur)
        
        number = number % (10 ** (level))
        level -= 1
    
    return result

if __name__ == '__main__':
    
    print checkio(499)
    
    assert checkio(6) == 'VI', 'First'
    assert checkio(76) == 'LXXVI', 'Second'
    assert checkio(499) == 'CDXCIX', 'Third'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', 'Fourth'
