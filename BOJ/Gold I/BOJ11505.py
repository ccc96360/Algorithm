#BOJ11505 구간 곱 구하기 20210429
import sys
from math import ceil, log2
input = sys.stdin.readline

OPERAND = 1000000007
def makeSegmentTree(node, start, end, tree, li):
    if start == end:
        tree[node] = li[start]
        return tree[node]
    mid = (start + end) // 2
    left = makeSegmentTree(node * 2, start, mid, tree, li)
    right = makeSegmentTree(node * 2 + 1, mid + 1, end, tree, li)
    tree[node] = (left * right) % OPERAND
    return tree[node]

def update(node, start, end, tree, li, v):
    if not (start <= v <= end):
        return tree[node]
    if start == end:
        tree[node] = li[v]
        return tree[node]
    else:
        mid = (start + end) // 2
        left = update(node * 2, start, mid, tree, li, v)
        right = update(node * 2 + 1, mid + 1, end, tree, li, v)
        tree[node] = (left * right) % OPERAND
        return tree[node]

def getMul(node, start, end, left, right, tree):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    l = getMul(node * 2, start, mid, left, right, tree)
    r = getMul(node * 2 + 1, mid + 1, end, left, right, tree)
    return (l*r) % OPERAND

def main():
    n,m,k = map(int,input().rstrip().split())
    li = [int(input()) for _ in range(n)]
    
    tree = [1] * 2 ** (ceil(log2(n)) + 1)
    makeSegmentTree(1, 0, n-1, tree, li)

    for _ in range(m+k):
        a,b,c = map(int,input().rstrip().split())
        if a == 1:
            li[b-1] = c
            update(1, 0, n-1, tree, li, b-1)
        elif a == 2:
            print(getMul(1, 0, n-1, b-1, c-1, tree))

if __name__ == '__main__':
    main()