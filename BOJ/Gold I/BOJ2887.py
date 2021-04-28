#BOJ2887 행성 터널 20210428
import sys
import heapq as hq
input = sys.stdin.readline

parent = []
def find(v):
    global parent
    if v == parent[v]:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]

def union(a,b):
    global parent
    a = find(a)
    b = find(b)
    parent[a] = b

def getWeight(a,b):
    return min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))

def addEdge(li, q, n):
    for i in range(1,n):
        hq.heappush(q, (getWeight(li[i-1],li[i]),(li[i-1][3],li[i][3])))

def main():
    n = int(input())
    li = [list(map(int,input().rstrip().split())) + [i] for i in range(n)]
    q = []      
    for i in range(3):
        li.sort(key = lambda x: x[i])
        addEdge(li, q, n)

    global parent
    parent = [i for i in range(n)]
    size = 0
    res = 0
    while q and size < n:
        w,v = hq.heappop(q)
        a,b = v
        if find(a) == find(b): continue
        union(a, b)
        size += 1
        res += w
    print(res)

if __name__ == '__main__':
    main()