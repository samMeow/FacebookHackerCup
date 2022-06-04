import sys
from collections import Counter
import math

def toIntArr(line):
    return [int(x) for x in line.split()]

def solution(puzzle):
    N = len(puzzle)
    row = [math.inf] * N
    col = [math.inf] * N
    dedup = set()
    for i in range(N):
        accu = 0
        pt = (0,0)
        for j in range(N):
            if puzzle[i][j] == 'O':
                accu  = math.inf
                break
            if puzzle[i][j] == '.':
                accu += 1
                pt = (i, j)
        if accu == 1:
            dedup.add(pt)
        row[i] = accu

    for i in range(N):
        accu = 0
        pt = (0,0)
        for j in range(N):
            if puzzle[j][i] == 'O':
                accu  = math.inf
                break
            if puzzle[j][i] == '.':
                accu += 1
                pt = (j, i)
        if accu == 1:
            dedup.add(pt)
        col[i] = accu

    result = row + col
    lookup = Counter(result)
    mini = min(result)
    if mini == math.inf:
        return 'Impossible'
    if mini == 1:
        return f'1 {len(dedup)}'

    return f'{mini} {lookup[min(result)]}'
    
    
    

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    N = int(sys.stdin.readline().rstrip('\n'))
    buffer = []
    for _ in range(N):
        buffer.append(sys.stdin.readline().rstrip('\n'))
    print('Case #{}: {}'.format(
        i+1,
        solution(buffer)
    ))