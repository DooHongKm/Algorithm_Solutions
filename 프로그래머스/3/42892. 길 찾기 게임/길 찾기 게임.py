import sys

def solution(nodeinfo):

    sys.setrecursionlimit(10000)
    
    rNode = 0
    n = len(nodeinfo)
    m = max(y for _, y in nodeinfo)

    nodeinfo = [[x, y, i + 1] for i, (x, y) in enumerate(nodeinfo)]
    nodeinfoPC = {
        i + 1: {
            "p": -1,
            "lc": -1,
            "rc": -1,
        }
        for i in range(n)
    }

    groupY = {}
    for x, y, node in nodeinfo:
        if y in groupY:
            groupY[y].append([x, node])
        else:
            groupY[y] = [[x, node]]
    groupY = dict(sorted(groupY.items(), key=lambda x: x[0], reverse=True))

    ranges = []
    for y, nodes in groupY.items():
        newRanges= []
        if y == m:
            x, node = nodes[0]
            rNode = node
            ranges += [[-float("inf"), x, node, "lc"], [x, float("inf"), node, "rc"]]
            continue
        for x, node in nodes:
            for l, r, i, temp in ranges:
                if l < x < r:
                    nodeinfoPC[i][temp] = node
                    nodeinfoPC[node]["p"] = i
                    newRanges += [[l, x, node, "lc"], [x, r, node, "rc"]]
        ranges = newRanges

    def preOrder(nodeIdx):
        nonlocal nodeinfoPC
        result = [nodeIdx]
        lc = nodeinfoPC[nodeIdx]["lc"]
        rc = nodeinfoPC[nodeIdx]["rc"]
        if lc != -1:
            result += preOrder(lc)
        if rc != -1:
            result += preOrder(rc)
        return result

    def postOrder(nodeIdx):
        nonlocal nodeinfoPC
        result = []
        lc = nodeinfoPC[nodeIdx]["lc"]
        rc = nodeinfoPC[nodeIdx]["rc"]
        if lc != -1:
            result += postOrder(lc)
        if rc != -1:
            result += postOrder(rc)
        return result + [nodeIdx]

    return [preOrder(rNode), postOrder(rNode)]