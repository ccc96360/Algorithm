#BOJ11047 동전 0 20210302
import sys
input = sys.stdin.readline

def main():
    n,k = map(int,input().rstrip().split())
    li = [int(input().rstrip()) for _ in range(n)]
    li.reverse()
    cnt = 0
    for v in li:
        if v > k: continue
        cnt += k // v
        k %= v
        if k == 0: break
    print(cnt)
if __name__ == '__main__':
    main()