import sys

def toIntArr(line):
    return [int(x) for x in line.split()]

def solution(n, k, w, ls, lc, hs, hc):
    [al, bl, cl, dl] = lc
    [ah, bh, ch, dh] = hc

    al = al % dl
    bl = bl % dl
    cl = cl % dl
    ah = ah % dh
    bh = bh % dh
    ch = ch % dh

    larr = ls
    harr = hs
    for i in range(k, n):
        larr.append((al * larr[i-2] % dl + bl * larr[i-1] % dl + cl) % dl + 1)
        harr.append((ah * harr[i-2] % dh + bh * harr[i-1] % dh + ch) % dh + 1)
    
    currentP = 0
    lastEnter = larr[0]
    plan = {}
    ps = []
    for i in range(n):
        l = larr[i]
        h = harr[i]

        if plan.get(l, 0):
            currentP = currentP + (l + w - lastEnter) * 2 + max(h - plan.get(l, 0) , 0) * 2
        else:
            currentP = currentP + (w + h) * 2

        ps.append(currentP)

        for j in range(l, l + w+1):
            plan[j] = max(plan.get(j, 0), h)
        lastEnter = l + w

    total = 1
    for p in ps:
        total = total * p % 1000000007
    return total
    

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    [n, k, w] = toIntArr(sys.stdin.readline())
    ls = toIntArr(sys.stdin.readline())
    lc = toIntArr(sys.stdin.readline())
    hs = toIntArr(sys.stdin.readline())
    hc = toIntArr(sys.stdin.readline())
    print('Case #{}: {}'.format(
        i+1,
        solution(n, k, w, ls, lc, hs, hc)
    ))