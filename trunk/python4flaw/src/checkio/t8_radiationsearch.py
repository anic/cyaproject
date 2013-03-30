

def checkio(matr):

    h = len(matr) #height of matrix
    w = 0  #width of matrix
    if h > 0:
        w = len(matr[0])
    
    #current visiting number and count
    curNum = 0
    curCount = 0
    
    #maxium number and its count
    maxNum = 0
    maxCount = 0
    
    #queue
    queue = []

    #unvisitied position left
    left = h * w
    
    #next direction
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for j in range(0, h):
        for i in range(0, w):
            #if position left is less than a maxium count of a number thatt has been visited 
            #stop advanced
            if left < curCount:
                return [ maxCount, maxNum] #find the maxmium
            
            if matr[i][j] == 0: #skip already visited(0)
                continue
            
            #enqueue a unvisited number
            curNum = matr[i][j]
            curCount = 1
            matr[i][j] = 0
            left -= 1
            queue.append((i, j))
            
            #BFS to visit the matrix
            while len(queue) > 0:
                x, y = queue.pop(0)
                
                #try 4 direction
                for d in dir:
                    xnext = x + d[0]
                    ynext = y + d[1]
                    if xnext < w and xnext >= 0 and ynext < h and ynext >= 0 and matr[xnext][ynext] == curNum:
                        curCount += 1
                        matr[xnext][ynext] = 0
                        left -= 1
                        queue.append((xnext, ynext))
            
            #compare with the previous maxium number
            if curCount > maxCount:
                maxNum = curNum
                maxCount = curCount
    
    #happen to be half of A and half of B,return here
    return [ maxCount, maxNum] 

if __name__ == '__main__':
    print checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ])
    
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], 'First'

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], 'Second'

    print 'All ok'
