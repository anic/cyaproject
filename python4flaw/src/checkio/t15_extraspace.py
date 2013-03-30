#http://www.checkio.org/mission/task/sentence-with-extra-spaces/
import re
def checkio(string):
    'return sentence without extra spaces'
    reg = re.compile(r'\s+')
    return reg.sub(' ',string)
    
if __name__ == '__main__':
    assert checkio('I  like   python') == "I like python", 'First'
    print 'All ok'
