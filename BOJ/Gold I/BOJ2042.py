#BOJ2042 구간 합 구하기 20210425
import sys
from math import log2,ceil
input = sys.stdin.readline

def makeSegmentTree(node, start, end, li, tree):
    if start == end:
        tree[node] = li[start]
        return tree[node]
    else:
        left = makeSegmentTree(node*2, start, (start+end)//2, li, tree)
        right = makeSegmentTree((node*2)+1, (start+end)//2 + 1, end, li, tree)
        tree[node] = left + right
        return tree[node]

def subSum(node, start, end, l, r, tree):
    if r < start or l > end:
        return 0
    if l <= start and end <= r:
        return tree[node]
    left = subSum(node*2, start, (start+end)//2, l, r, tree)
    right = subSum(node*2+1, (start+end)//2 + 1 , end, l, r, tree)
    return left + right

def update(node, start, end, idx, diff, tree):
    if not(start <= idx <= end):
        return 
    tree[node] += diff
    if start != end:
        update(node*2, start, (start+end)//2, idx, diff, tree)
        update(node*2+1, (start+end)//2 + 1 , end, idx, diff, tree)
        
UPDATE = 1
SUBSUM = 2
def query(what, a, b, tree, n, li):
    if what == UPDATE:
        diff = b - li[a] + 1
        li[a] = b + 1
        update(1, 0, n-1, a, diff, tree)
    elif what == SUBSUM:
        print(subSum(1, 0, n-1, a, b, tree))

def main():
    n,m,k = map(int,input().rstrip().split())
    li = [int(input()) for _ in range(n)]
    tree = [0]+[0] * (2**(ceil(log2(n))+1))
    makeSegmentTree(1,0,n-1,li,tree)
    
    for _ in range(m+k):
        what, a, b = map(int,input().rstrip().split())
        query(what, a-1, b-1, tree, n, li)
if __name__ == '__main__':
    main()