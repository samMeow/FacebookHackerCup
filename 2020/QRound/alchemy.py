import sys

def solution(seq):
    record = {}
    for c in seq:
        record[c] = record.get(c, 0) + 1
    
    if abs(record.get('A', 0) - record.get('B', 0)) <= 2:
        return 'Y'
    else:
        return 'N'
    

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    sys.stdin.readline()
    seq = sys.stdin.readline().rstrip('\n')
    print('Case #{}: {}'.format(
        i+1,
        solution(seq)
    ))