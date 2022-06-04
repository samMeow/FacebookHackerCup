import sys

def solution(inbound, outbound):
    total = len(inbound)
    result = [ ['N' for _ in range(total)] for _ in range(total) ]

    for d in range(total):
        for l in range(total):
            if d == 0:
                result[l][l] = 'Y'
                continue
            smaller = l - d
            if smaller >= 0:
                result[l][smaller] = 'N'
                if result[l][smaller+1] == 'Y':
                    if inbound[smaller] == 'Y' and outbound[smaller + 1] == 'Y':
                        result[l][smaller] = 'Y'
            larger = l + d
            if larger < total:
                result[l][larger] = 'N'
                if result[l][larger-1] == 'Y':
                    if inbound[larger] == 'Y' and outbound[larger - 1] == 'Y':
                        result[l][larger] = 'Y'
        
    return result
    

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    sys.stdin.readline()
    inbound = sys.stdin.readline().rstrip('\n')
    outbound = sys.stdin.readline().rstrip('\n')
    answer = solution(inbound, outbound)
    print("Case #{}:".format(i+1))
    for ln in answer:
        print(''.join(ln))