def checkio(number):
    result = ''
    single = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    double = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if number > 100:
        result += single[int(number / 100)] + ' hundred'
        
    number = number % 100
    if number == 0:pass 
    elif number < 10:
        result += addspace(result) + single[number]
    elif number < 20:
        result += addspace(result) + double[number%10]
    else :#number>=20
        result += addspace(result) + tens[int(number / 10)]
        number = number % 10
        if number != 0:
            result += addspace(result) + single[number]
    
    return result

def addspace(str):
    if str != '':
        return ' '
    else:
        return ''

if __name__ == '__main__':
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12) == 'twelve', "Third"
    assert checkio(101) == 'one hundred one', "Fifth"
    assert checkio(212) == 'two hundred twelve', "Sixth"
    assert checkio(40) == 'forty', "Seventh, forty - it is correct"

    print 'All ok'
