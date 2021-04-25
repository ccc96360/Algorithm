#BOJ2357 최솟값과 최댓값 20210425
import sys
from math import ceil, log2
input = sys.stdin.readline

INF = 10**9
class Node:
    def __init__(self,min,max):
        self.min = min
        self.max = max

def makeSegmentTree(node, start, end, tree, li):
    if start == end:
        tree[node] = Node(li[start], li[start])
        return tree[node]
    else:
        left = makeSegmentTree(node * 2, start, (start+end)//2, tree, li)
        right = makeSegmentTree(node * 2 + 1, (start+end)//2 + 1, end, tree, li)
        tree[node] = Node(min(left.min, right.min), max(left.max, right.max))
        return tree[node]

def findMinMax(node, start, end, l, r, tree):
    if l > end or r < start:
        return INF, 0
    if l <= start and end <= r:
        return tree[node].min, tree[node].max
    left = findMinMax(node * 2, start, (start+end)//2, l, r, tree)
    right = findMinMax(node * 2 + 1, (start+end)//2 + 1, end, l, r, tree)
    return min(left[0], right[0]), max(left[1], right[1])

def main():
    n,m = map(int,input().rstrip().split())
    li = [int(input()) for _ in range(n)]
    tree = [0] + [0] * (2 ** (ceil(log2(n)) + 1))
    makeSegmentTree(1,0,n-1,tree,li)
    for _ in range(m):
        a,b = map(lambda x: int(x)-1,input().rstrip().split())
        a,b = findMinMax(1,0,n-1,a,b,tree)
        print(a,b)
if __name__ == '__main__':
    main()