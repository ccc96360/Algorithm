#BOJ16562 친구비 20210522
import sys
input = sys.stdin.readline

def find(v, parent):
    if v == parent[v]:
        return v
    else:
        parent[v] = find(parent[v], parent)
        return parent[v]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[b] = a 


def main():
    n, m, k = map(int, input().rstrip().split())
    parent = [i for i in range(n+1)]
    costs = [0] + list(map(int, input().rstrip().split()))
    for _ in range(m):
        a,b = map(int, input().rstrip().split())
        union(a,b,parent)
    for i in range(1, n+1):
        find(i, parent)
    minCost = {}
    for i in range(1, n+1):
        group = parent[i]
        if group not in minCost:
            minCost[group] = costs[i]
        else:
            minCost[group] = min(minCost[group], costs[i])
    ret = sum(minCost.values())
    if ret > k:
        print("Oh no")
    else:
        print(ret)
if __name__ == '__main__':
    main()