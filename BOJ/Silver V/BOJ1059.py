#BOJ1059 좋은 구간 20210529
import sys
input = sys.stdin.readline

def main():
    l = int(input())
    li = sorted(list(map(int, input().rstrip().split())))
    n = int(input())
    mn = 1
    mx = li[0]
    for i in range(l-1):
        if li[i] < n < li[i+1]:
            mn = li[i] + 1
            mx = li[i+1]
            break
    cnt = 0
    for i in range(mn, n+1):
        for j in range(n, mx):
            if i == j: continue
            cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()
