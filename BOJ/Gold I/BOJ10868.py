#BOJ10868 최솟값 20210428
import sys
from math import log2, ceil
input = sys.stdin.readline

INF = 1000000000

def makeSegmentTree(node, start, end, tree, li):
    if start == end:
        tree[node] = li[start]
        return tree[node]
    mid = (start+end) // 2
    left = makeSegmentTree(node*2, start, mid, tree ,li)
    right = makeSegmentTree(node * 2 + 1, mid + 1, end, tree, li)
    tree[node] = min(left, right)
    return tree[node]

def find(node, start, end, left, right, tree):
    if right < start or end < left:
        return INF
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end) // 2
    l = find(node * 2, start, mid, left, right, tree)
    r = find(node * 2 + 1, mid + 1, end, left, right, tree)
    return min(l,r)
    
def main():
    n,m = map(int,input().rstrip().split())
    li = [int(input()) for _ in range(n)]
    tree = [0] * 2**(ceil(log2(n))+1)
    makeSegmentTree(1,0,n-1,tree, li)
    for _ in range(m):
        a,b = map(lambda x: int(x)-1, input().rstrip().split())
        print(find(1,0,n-1,a,b,tree))
if __name__ == '__main__':
    main()