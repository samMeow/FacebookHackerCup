import sys


def find_max(max_plan, plan, target):
    ava = [ x for x in plan.get(target[0], []) if x[1] != target[1] ]
    if len(ava) == 0:
        return 0
    if max_plan.get(target):
        return max_plan[target]
    max_plan[target] = max([
        t[0] - target[0] + find_max(max_plan, plan, t)
        for t in ava
    ])
    return max_plan[target]


def solution(trees):
    plan = {}
    for i, t in enumerate(trees):
        [p, h] = t
        plan[p-h] = plan.get(p-h, [])
        plan[p-h].append((p, i))
        plan[p] = plan.get(p, [])
        plan[p].append((p+h, i))
    
    max_plan = {}
    cache = {}

    for k, v in reversed(plan.items()):
        max_plan[k] = max([
            x[0] - k + find_max(cache, plan, x) for x in v
        ])
    
    return max(max_plan.values())

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    n = int(sys.stdin.readline())
    buffer = []
    for _ in range(n):
        line = sys.stdin.readline()
        buffer.append([ int(x) for x in line.split() ])
    print('Case #{}: {}'.format(
        i + 1,
        solution(buffer)
    ))