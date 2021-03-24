#BOJ1197 최소 스패닝 트리 20210324 크루스칼 알고리즘
import sys
import heapq as hq
input = sys.stdin.readline

parent = []

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    parent[x] = y

def main():
    global parent
    n,e = map(int,input().rstrip().split())
    parent = [i for i in range(n+1)]
    q = []
    res = []
    size = 0
    for _ in range(e): 
        a,b,w = map(int,input().rstrip().split())
        hq.heappush(q, (w,(a,b)))
    while q and size != n:
        w,p = hq.heappop(q)
        a,b = p
        if find(a) == find(b): continue
        union(a,b)
        size+=1
        res.append(w)
    print(sum(res))
if __name__ == '__main__':
    main()