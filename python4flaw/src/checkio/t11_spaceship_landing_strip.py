#http://www.checkio.org/mission/task/spaceship-landing-strip/

#is G or S
def is_gs(x, y, map):
    return  map[y][x] == 'G' or map[y][x] == 'S'

#find how many G or S from (start_x,cur_y) to bottom 
def find_down(start_x, start_y, cur_y, map, mark):
    if cur_y >= len(map) or not is_gs(start_x, cur_y, map):
        return cur_y #find the bottom or a block below 
    
    max_y = find_down(start_x, start_y, cur_y + 1, map, mark)
    mark[cur_y][start_x] = max_y - cur_y #x,y in mark means the steps map[y][x] can walk to bottom freely  
 
    return max_y

#build the mark matrix
def buildmark(map):   
    h = len(map)
    w = len(map[0])
    
    mark = [[0 for col in range(w)] for row in range(h)]
    print mark
    
    for i in range(0, w):
        next_y = 0
        while True:
            next_y = find_down(i, next_y, next_y, map, mark) + 1
            if next_y >= h:
                break
    
    return mark        
 
#find the max rectangle
def find_max_rectangle(x, y, mark):
    result = 1
    min_height = len(mark)
    for i in range(x, len(mark[0])):
        if mark[y][i] == 0: #find a block just break
            break
        
        if mark[y][i] < min_height:
            min_height = mark[y][i] 
    
        tmp = (i - x + 1) * min_height
        if tmp > result:
            result = tmp 
    return result

def checkio(map):
    
    mark = buildmark(map)
    print mark
    
    h = len(map)
    w = len(map[0])
    
    result = 0
    for j in range(0, h):
        for i in range(0, w):
            tmp = find_max_rectangle(i, j, mark)
            if tmp > result:
                result = tmp
                
    return result 

if __name__ == '__main__':
    
    checkio(['GGTGG', 'TGGGG', 'GSSGT', 'GGGGT', 'GWGGG', 'RGTRT', 'RTGWT', 'WTWGR'])
    
    assert checkio(['G']) == 1, 'First'
    assert checkio(['GS', 'GS']) == 4, 'Second'
    assert checkio(['GT', 'GG']) == 2, 'Third'
    assert checkio(['GGTGG', 'TGGGG', 'GSSGT', 'GGGGT', 'GWGGG', 'RGTRT', 'RTGWT', 'WTWGR']) == 9, 'Fourth'
    print 'All is ok'
