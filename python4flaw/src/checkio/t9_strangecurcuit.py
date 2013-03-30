#http://www.checkio.org/mission/task/destination-in-spiral/

import math

#return the cordinate of num in axis
def get_position(num):
    x = 0
    y = 0
    if num == 1:
        return (x, y)
     
    xpoint = num - 1
    n = math.ceil(0.5 * (1 + math.sqrt(1 + 4 * xpoint)))
    
    #delta between xpoint and n*(n+1)
    
    section = n - 1
    section_even = section % 2 == 0 
    delta_in_section = section * (section + 1) - xpoint
    
    
    if section_even:
        sum_section = -1 * section / 2
    else: #section is odd
        sum_section = section / 2.0 + 0.5
    
#    print sum_section, section, delta_in_section

    if delta_in_section >= section:
        #remove section times of -1^(section+1)
        x = sum_section + section * ((-1) ** (section))
        y = sum_section + (delta_in_section - section) * ((-1) ** section)
    else:
        x = sum_section + delta_in_section * ((-1) ** (section))
        y = sum_section 
    
#    print 'pos(' + str(num) + ")=", x, y
    return (x, y)

def checkio(data):
    "Find the destination"
    a, b = data
    xa, ya = get_position(a)
    xb, yb = get_position(b)
    
    return abs(xb - xa) + abs(yb - ya)
    

if __name__ == '__main__':
    
#    for i in range(1,40):
#        get_position(i) 
    
    assert checkio([1, 9]) == 2, "First"
    assert checkio([9, 1]) == 2, "Reverse First"
    assert checkio([10, 25]) == 1, "Neighbours"
    assert checkio([5, 9]) == 4, "Diagonal"
    assert checkio([26, 31]) == 5, "One row"
    assert checkio([50, 16]) == 10, "One more test"
