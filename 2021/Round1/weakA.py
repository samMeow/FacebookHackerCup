import sys

def toIntArr(line):
    return [int(x) for x in line.split()]

def solution(str):
    last = ''
    change = 0
    for c in str:
        if c == 'X' and last in ['O', '']:
            change += 1
            last = 'X'
        elif c == 'O' and last in ['X', '']:
            change += 1
            last = 'O'
    return max(change - 1, 0)
    

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    sys.stdin.readline()
    str = sys.stdin.readline().rstrip('\n')
    print('Case #{}: {}'.format(
        i+1,
        solution(str)
    ))