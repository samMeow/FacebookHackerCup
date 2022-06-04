import sys

def toIntArr(line):
    return [int(x) for x in line.split()]

def solution(str):
    lookup = {}
    vowel = 0
    consis = 0
    for c in str:
        lookup[c] = lookup.get(c, 0) + 1
        if c in ['A', 'E', 'I', 'O', 'U']:
            vowel += 1
        else:
            consis += 1

    mini = len(str) * 2
    for k, v in lookup.items():
        if k in ['A', 'E', 'I', 'O', 'U']:
            mini = min(mini, (vowel - v) * 2 + consis, vowel + consis * 2)
        else:
            mini = min(mini, (consis - v) * 2 + vowel, consis + vowel * 2)
    return mini
    

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    str = sys.stdin.readline().rstrip('\n')
    print('Case #{}: {}'.format(
        i+1,
        solution(str)
    ))