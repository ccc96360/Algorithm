#BOJ2263 트리의 순회 20210409
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


inorder = []
postorder = []
pos = []
def preorder(inStart, inEnd, poStart, poEnd):
    if inStart >= inEnd:
        return None
    root = postorder[poEnd-1]
    print(root,end=" ")
    idx = pos[root]
    offset = idx - inStart 
    preorder(inStart, idx, poStart, poStart+offset)
    preorder(idx+1, inEnd, poStart+offset, poEnd-1)

def main():
    n = int(input())
    global inorder, postorder, pos
    inorder = list(map(int,input().rstrip().split()))
    postorder = list(map(int,input().rstrip().split()))
    pos = [0] * (n+1)
    for i in range(n):
        pos[inorder[i]] = i
    preorder(0, n, 0, n)
if __name__ == '__main__':
    main()