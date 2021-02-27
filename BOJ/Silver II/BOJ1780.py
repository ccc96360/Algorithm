#BOJ1780 종이의 개수 20210227
import sys
input = sys.stdin.readline

cnt = {-1:0,0:0,1:0}
def isSameNum(li):
    v = li[0][0]
    for i in li:
        for j in i:
            if j != v:
                return False
    return True
def f(li):
    t = isSameNum(li)
    if t == False:
        n = len(li)
        k = n//3
        parts = [list() for _ in range(9)]
        for i in range(0,k):
            parts[0].append(li[i][:k])
            parts[1].append(li[i][k:k*2])
            parts[2].append(li[i][k*2:])
        for i in range(k, k * 2):
            parts[3].append(li[i][:k])
            parts[4].append(li[i][k:k*2])
            parts[5].append(li[i][k*2:])
        for i in range(k*2, n):
            parts[6].append(li[i][:k])
            parts[7].append(li[i][k:k*2])
            parts[8].append(li[i][k*2:])
        for p in parts:
            f(p)
    else:
        cnt[li[0][0]] += 1

def main():
    n = int(input())
    li = [list(map(int,input().rstrip().split())) for _ in range(n)]
    f(li)
    print(cnt[-1],cnt[0],cnt[1],sep="\n")
if __name__ == '__main__':
    main()