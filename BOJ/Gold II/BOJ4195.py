#BOJ4195 친구 네트워크 20210416
import sys
input = sys.stdin.readline

def find(v, parent):
    if parent[v] < 0:
        return v
    else:
        parent[v] = find(parent[v],parent)
        return parent[v]

def union(a,b,parent):
    a = find(a,parent)
    b = find(b,parent)

    if a == b:
        return
    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b
    
def main():
    n = int(input())
    nameToIdx = {}
    cnt = 0
    parent = []
    size = {}
    for _ in range(n):
        a,b = input().rstrip().split()
        if a not in nameToIdx:
            nameToIdx[a] = cnt
            parent.append(-1)
            size[a] = 1
            cnt += 1
        if b not in nameToIdx:
            nameToIdx[b] = cnt
            parent.append(-1)
            size[b] = 1
            cnt += 1
        i = nameToIdx[a]
        j = nameToIdx[b]
        union(i, j, parent)
        print(-parent[find(i,parent)])
if __name__ == '__main__':
    for _ in range(int(input())):
        main()