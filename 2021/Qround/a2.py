import sys
import math

def toIntArr(line):
    return [int(x) for x in line.split()]

def solution(str, arrs):
    lookup = [None]*26
    for i, v in enumerate(lookup):
        lookup[i] = [math.inf] * 26
    for pair in arrs:
        A, B = pair[0], pair[1]
        dest = lookup[ord(A)-ord('A')]
        dest[ord(B)-ord('A')] = 1
        lookup[ord(A)-ord('A')] = dest
    for i in range(26):
        lookup[i][i] = 0

    for i in range(26):
        for j in range(26):
            for k in range(26):
                if lookup[i][k] + lookup[k][j] < lookup[i][j]:
                    lookup[i][j] = lookup[i][k] + lookup[k][j]

    for v in lookup:
        print(v)

    occurMap = {}
    for v in str:
       occurMap[v] = occurMap.get(v, 0) + 1 

    mini = math.inf
    for c in range(26):
        accu = 0
        for k, v in occurMap.items():
            accu += lookup[ord(k)-ord('A')][c] * v
        mini = min(mini, accu)
    return -1 if mini == math.inf else mini

    

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    str = sys.stdin.readline().rstrip('\n')
    time = int(sys.stdin.readline().rstrip('\n'))
    buffer = []
    for _ in range(time):
        buffer.append(sys.stdin.readline().rstrip('\n'))
    print('Case #{}: {}'.format(
        i+1,
        solution(str, buffer)
    ))