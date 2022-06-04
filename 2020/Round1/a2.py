import sys

def toIntArr(line):
    return [int(x) for x in line.split()]

class Node:
    def __init__(self, v, t):
        self.v = v
        self.t = t
        self.left = None
        self.right = None

    @staticmethod
    def insert(root, v, t):
        if root == None:
            return Node(v, t)
        if root.v < v:
            root.right = Node.insert(root.right, v, t)
        else:
            root.left = Node.insert(root.left, v, t)
        return root

    @staticmethod
    def toList(root, ln):
        if root is not None:
            Node.toList(root.left, ln)
            ln.append((root.v, root.t))
            Node.toList(root.right, ln)

    @staticmethod
    def toBst(arr):
        if not arr: 
            return None
  
        mid = (len(arr)) // 2
        # make the middle element the root 
        root = Node(arr[mid][0], arr[mid][1]) 

        root.left = Node.toBst(arr[:mid]) 
        root.right = Node.toBst(arr[mid+1:]) 
        return root 

def search(arr, v):
    l = 0
    r = len(arr) - 1
    while r >= l:
        mid = l + (r - l) // 2
        if arr[mid][0] == v:
            return mid
        elif arr[mid][0] < v:
            l = mid + 1
        else:
            r = mid - 1
    return r


def solution(n, k, ls, lc, ws, wc, hs, hc):
    [al, bl, cl, dl] = lc
    [aw, bw, cw, dw] = wc
    [ah, bh, ch, dh] = hc

    al = al % dl
    bl = bl % dl
    cl = cl % dl

    aw = aw % dw
    bw = bw % dw
    cw = cw % dw

    ah = ah % dh
    bh = bh % dh
    ch = ch % dh

    larr = ls
    warr = ws
    harr = hs
    for i in range(0, n):
        larr.append((al * larr[i-2] % dl + bl * larr[i-1] % dl + cl) % dl + 1)
        warr.append((aw * warr[i-2] % dw + bw * warr[i-1] % dw + cw) % dw + 1)
        harr.append((ah * harr[i-2] % dh + bh * harr[i-1] % dh + ch) % dh + 1)

    currentP = 0
    rangeTree = None
    ps = []
    for i in range(n):
        l = larr[i]
        w = warr[i]
        h = harr[i]

        arr = []
        Node.toList(rangeTree, arr)
        begin = []

        preIdx = search(arr, l)
        if preIdx < 0:
            begin.append((l, 'S'))
        else:
            pre = arr[preIdx]
            begin = arr[0:preIdx+1]
            if pre[1] == 'E' and pre[0] != l:
                begin.append((l, 'S'))
            
        endIdx = search(arr, l + w)
        if endIdx == len(arr) - 1:
            begin.append((l + w, 'E'))
        elif endIdx <= 0:
            begin.append((l+w, 'E'))
            begin = begin + arr[0:]
        else:
            suc = arr[endIdx + 1]
            if suc == 'S':
                begin.append((l + w, 'E'))
            begin = begin + arr[endIdx+1:]

        if preIdx == endIdx:
            currentP = currentP + (w + h) * 2
        else:
            overlap = 0
            s = l
            valley = 0
            for i in range(preIdx+1, endIdx+1):
                [v, t] = arr[i]
                if t == 'E':
                    overlap = overlap + v - s
                else:
                    valley = valley + 1
                s = v
            
            if arr[endIdx][1] == 'S':
                overlap = overlap + l + w - arr[endIdx][0]

            # print(begin, arr, preIdx, endIdx, overlap)
            currentP = currentP + max(w - overlap, 0) * 2 - valley * 2 * h

             
        ps.append(currentP)
        rangeTree = Node.toBst(begin)

    return ps

    total = 1
    for p in ps:
        total = total * p % 1000000007
    return total
    

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    [n, k] = toIntArr(sys.stdin.readline())
    ls = toIntArr(sys.stdin.readline())
    lc = toIntArr(sys.stdin.readline())
    ws = toIntArr(sys.stdin.readline())
    wc = toIntArr(sys.stdin.readline())
    hs = toIntArr(sys.stdin.readline())
    hc = toIntArr(sys.stdin.readline())
    print('Case #{}: {}'.format(
        i+1,
        solution(n, k, ls, lc, ws, wc, hs, hc)
    ))