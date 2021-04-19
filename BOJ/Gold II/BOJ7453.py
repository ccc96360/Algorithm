#BOJ7453 합이 0인 네 정수 20210419
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def main():
    n = int(input())
    a = []; b = []; c = []; d = []
    li = [a,b,c,d]
    for _ in range(n):
        tmp = list(map(int,input().rstrip().split()))
        i = 0
        for i in range(4):
            li[i].append(tmp[i])
    for v in li: v.sort()
    ab = sorted([ a[i]+b[j] for j in range(n) for i in range(n)])
    cd = sorted([ c[i]+d[j] for j in range(n) for i in range(n)])
    ans = 0
    for v in cd:
        ans += bisect_right(ab,-v)-bisect_left(ab,-v)
    print(ans)
if __name__ == '__main__':
    main()