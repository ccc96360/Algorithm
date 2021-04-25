#BOJ5676 음주 코딩 20210425
import sys
from math import ceil, log2
input = sys.stdin.readline

def makeSegmentTree(node, start, end, tree, li):
    if start == end:
        tree[node] = li[start]
    else:
        left = makeSegmentTree(node*2, start, (start + end) // 2, tree, li)
        right = makeSegmentTree(node*2+1, (start + end) // 2 + 1, end, tree, li)
        tree[node] = left * right
    return tree[node]

ZERO = 0
CHANGE = 1
NOTCHANGE = 2
def update(node, start, end, idx, tree, diff):
    if not(start <= idx <= end):
        return tree[node]
    if start == end:
        tree[node] = diff
    if start != end:
        left = update(node*2, start, (start+end)//2, idx, tree, diff)
        right = update(node*2+1, (start+end)//2+1, end, idx, tree, diff)
        tree[node] = left*right
    return tree[node]

def getSign(node, start, end, l, r, tree):
    if r < start or end < l:
        return 1
    if l <= start and end <= r:
        return tree[node]
    
    left = getSign(node*2, start, (start+end)//2, l, r, tree)
    right = getSign(node*2+1, (start+end)//2+1, end, l, r, tree)
    return left*right

def generalization(x):
    if x > 0: return 1
    elif x < 0: return -1
    else: return 0

def main():
    n,k = map(int,input().rstrip().split())
    li = list(map(lambda x: generalization(int(x)), input().rstrip().split()))
    tree = [0] + [0] * (2 ** (ceil(log2(n))+1))
    makeSegmentTree(1, 0, n-1, tree, li)
    res = []
    for _ in range(k):
        tmp = input().rstrip().split()
        cmd = tmp[0]
        a,b = map(lambda x: int(x)-1, tmp[1:])
        if cmd == "C":
            b += 1
            b = generalization(b)
            update(1, 0, n-1, a, tree, b)
            li[a] = b
        elif cmd == "P":
            tmp = getSign(1, 0, n-1, a, b, tree)
            res.append("+" if tmp > 0 else "-" if tmp < 0 else "0")
    print("".join(res))
if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            break